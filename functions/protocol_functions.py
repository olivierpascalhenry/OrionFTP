import logging
import ftplib
import base64
import socket
import os
from pathlib import Path
from functions.window_functions import MyCredentials, MyInfo, MyQuestion
from functions.gui_elements import MyQTreeWidgetItem, CustomTreeItem
from functions.utilities import set_size
from functions.material_functions import tree_objects_init
from functions.thread_functions import DownloadFTPFile
from PyQt5 import QtGui, QtWidgets, QtCore


class FTPProtocol(QtCore.QObject):
    download_finished = QtCore.pyqtSignal()
    update_local_file_list = QtCore.pyqtSignal()

    def __init__(self, ftp_profile, widgets, config_dict, translations_dict):
        QtCore.QObject.__init__(self)
        logging.debug('protocol_functions.py - FTPProtocol - __init__')
        self.config_dict = config_dict
        self.translations_dict = translations_dict
        self.one_tree_option = self.config_dict['INTERFACE'].getboolean('remote_tree_one_widget')
        self.display_icon = self.config_dict['INTERFACE'].getboolean('display_icons_remote_tree')
        self.ftp_profile = ftp_profile
        self.username = self.ftp_profile['username']
        self.password = base64.b64decode(self.ftp_profile['password']).decode('utf-8')
        self.host = self.ftp_profile['host']
        self.port = self.ftp_profile['port']
        self.encryption = self.ftp_profile['encryption']
        self.ftp_protocol = None
        self.file_list = list()
        self.folder_list = list()
        self.gui_connect_list = list()
        self.remote_path = ''
        self.old_remote_path = ''
        self.first_path = ''
        self.gui_path = widgets[0]
        self.gui_tree_up = widgets[1]
        self.gui_tree_up_model = widgets[1].model()
        self.gui_tree_down = widgets[2]
        self.gui_connect_widget = widgets[3]
        self.gui_transfer_widget = widgets[4]
        self.credential_window = None
        self.var_scroll = None
        self.item_scroll = None
        self.file_types, self.type_icons = tree_objects_init()
        self.thread = None
        self.label_1 = []

    def connection(self):
        logging.debug('protocol_functions.py - FTPProtocol - connection')
        if not self.username or not self.password:
            self.credential_window = MyCredentials(self.host, self.username, self.password,
                                                   self.config_dict, self.translations_dict)
            self.credential_window.exec_()
            if self.credential_window.username is not None and self.credential_window.password is not None:
                self.username = self.credential_window.username
                self.password = self.credential_window.password
        if self.username is not None or self.password is not None:
            try:
                self.ftp_protocol = self._ftp_connection()
                self._update_connection_widget([1, 'PWD'])
                self.first_path = self.ftp_protocol.pwd()
                self._update_connection_widget([2, '"' + self.first_path + '" is the current directory'])
                self._list_folders_files(first_listing=True, first_path=self.first_path)
                return True
            except ftplib.error_perm as e:
                logging.exception('protocol_functions.py - FTPProtocol - connection - error')
                if '550' in str(e):
                    self._update_connection_widget([3, 'SSL/TLS required on the control channel'])
                elif '500' in str(e):
                    self._update_connection_widget([3, 'AUTH not understood'])
                else:
                    self._update_connection_widget([3, 'Login incorrect'])
                return False
            except socket.timeout:
                logging.exception('protocol_functions.py - FTPProtocol - connection - error')
                self._update_connection_widget([3, 'The connection was refused by ' + self.host])
                return False
            except ConnectionRefusedError:
                logging.exception('protocol_functions.py - FTPProtocol - connection - error')
                self._update_connection_widget([3, 'Timed out, no response from ' + self.host])
                return False

    def change_path(self, index):
        logging.debug('protocol_functions.py - FTPProtocol - change_path')
        item_text = self.gui_tree_up_model.itemFromIndex(index).text()
        if item_text != '/':
            self.remote_path = self._build_remote_path(index) + item_text
            if self.old_remote_path != self.remote_path:
                self.old_remote_path = self.remote_path
                try:
                    self._update_connection_widget([1, 'CWD ' + self.remote_path])
                    message = self.ftp_protocol.cwd(self.remote_path)
                    self._update_connection_widget([2, message])
                    self._list_folders_files(parent_index=index)
                except ftplib.error_perm:
                    logging.exception('protocol_functions.py - FTPProtocol - connection - error')
                    self._update_connection_widget([3, 'Permission denied for the following folder: '
                                                    + self.remote_path])
                except ftplib.error_temp:
                    logging.exception('protocol_functions.py - FTPProtocol - connection - error')
                    self._update_connection_widget([3, 'No transfer timeout (300 seconds): closing control connection'])
                    self.ftp_protocol = self._ftp_connection()
                    self.old_remote_path = ''
                    self.change_path(index)

    def refresh(self, index):
        logging.debug('protocol_functions.py - FTPProtocol - refresh')
        item = self.gui_tree_up_model.itemFromIndex(index)
        if self.one_tree_option:
            if item.statusTip() != 'folder':
                item = item.parent()
                index = self.gui_tree_up_model.indexFromItem(item)
        for i in reversed(range(0, item.rowCount())):
            item.takeRow(i)
        self.old_remote_path = ''
        self.change_path(index)

    def download_selection(self, local_path):
        logging.debug('protocol_functions.py - FTPProtocol - download_selection')
        try:
            self._update_connection_widget([1, 'NOOP'])
            message = self.ftp_protocol.voidcmd("NOOP")
            self._update_connection_widget([2, message])
            self.var_scroll = None
            self.item_scroll = None
            file_list = self._set_file_folder_list(local_path)
            if file_list is None:
                self.download_finished.emit()
            elif not file_list:
                text = self.translations_dict['nofolderdownload'][self.config_dict['OPTIONS'].get('language')]
                self.infoWindow = MyInfo(text)
                self.infoWindow.resize(450, 200)
                self.infoWindow.exec_()
                self.download_finished.emit()
            else:
                self._add_files_to_frame(file_list)
                self.thread = DownloadFTPFile(self.ftp_protocol, file_list, local_path,
                                              self.translations_dict, self.config_dict)
                self.thread.download_update.connect(self._update_progress_bar)
                self.thread.update_status.connect(self._update_connection_widget)
                self.thread.update_down_widget.connect(self._update_local_down_widget)
                self.thread.download_done.connect(self._download_finished)
                self.thread.download_canceled.connect(self._download_canceled)
                self.thread.all_download_canceled.connect(self._all_download_canceled)
                self.thread.download_failed.connect(self._download_failed)
                self.thread.start()
        except ftplib.error_temp:
            logging.exception('protocol_functions.py - FTPProtocol - connection - error')
            self._update_connection_widget([3, 'No transfer timeout (300 seconds): closing control connection'])
            self.ftp_protocol = self._ftp_connection()
            self.download_selection(local_path)

    def cancel_download(self):
        logging.debug('protocol_functions.py - FTPProtocol - cancel_download')
        try:
            self.thread.cancel_download()
            self.ftp_protocol.quit()
            self.ftp_protocol = None
            self.ftp_protocol = self._ftp_connection()
            self.thread.ftp = self.ftp_protocol
            self.thread.connected = True
        except AttributeError:
            pass

    def cancel_all_download(self):
        logging.debug('protocol_functions.py - FTPProtocol - cancel_all_download')
        try:
            self.thread.cancel_all_download()
            self.ftp_protocol.quit()
            self.ftp_protocol = None
            self.ftp_protocol = self._ftp_connection()
            self.thread.ftp = self.ftp_protocol
            self.thread.connected = True
        except AttributeError:
            pass

    def remove_from_list(self):
        logging.debug('protocol_functions.py - FTPProtocol - remove_from_list')
        items = self.gui_transfer_widget.selectedItems()
        for item in reversed(items):
            index = self.gui_transfer_widget.indexFromItem(item).row()
            text = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][2]
            if text in self.label_1[index].text():
                if index > 0 and self.progress[index - 1].value() < 95:
                    self.thread.file_list.pop(index)
                    self.label_1.pop(index)
                    self.label_2.pop(index)
                    self.label_3.pop(index)
                    self.progress.pop(index)
                    self.gui_transfer_widget.takeTopLevelItem(index)
                elif index == 0:
                    self.thread.file_list.pop(index)
                    self.label_1.pop(index)
                    self.label_2.pop(index)
                    self.label_3.pop(index)
                    self.progress.pop(index)
                    self.gui_transfer_widget.takeTopLevelItem(index)

    def reset_tree(self):
        logging.debug('protocol_functions.py - FTPProtocol - reset_tree')
        self._reset_up_down_tree()
        self.remote_path = self.first_path
        self.old_remote_path = ''
        item = self.gui_tree_up_model.item(0, 0)
        index = self.gui_tree_up_model.indexFromItem(item)
        self.change_path(index)

    def close_ftp(self):
        logging.debug('protocol_functions.py - FTPProtocol - close_ftp')
        try:
            self._update_connection_widget([1, 'QUIT'])
            message = self.ftp_protocol.quit()
            self._update_connection_widget([2, message])
            self._update_connection_widget([0, 'Connection to ' + self.host + ':' + self.port + ' closed.'])
            self._all_download_canceled()
            logging.debug('protocol_functions.py - FTPProtocol - close_ftp - connection closed')
        except (ftplib.error_temp, OSError, AttributeError):
            logging.exception('protocol_functions.py - FTPProtocol - connection - error')
            self._update_connection_widget([3, 'No transfer timeout (300 seconds): closing control connection'])
            self._update_connection_widget([0, 'Connection to ' + self.host + ':' + self.port + ' closed.'])

    def clear_transfers(self):
        self.gui_transfer_widget.clear()
        self.label_1 = []

    def _update_progress_bar(self, val):
        if val[0] != self.var_scroll:
            self.var_scroll = val[0]
            if val[0] == 0:
                self.item_scroll = self.gui_transfer_widget.itemAt(0, 0)
            else:
                self.item_scroll = self.gui_transfer_widget.itemBelow(self.item_scroll)
            self.gui_transfer_widget.scrollToItem(self.item_scroll, QtWidgets.QAbstractItemView.PositionAtBottom)
        self.label_1[val[0]].setText(val[1])
        if val[3]:
            self.label_4[val[0]].setText(val[3])
        self.progress[val[0]].setValue(val[4])
        if val[2]:
            self.label_1[val[0] - 1].setText(val[2])

    def _download_finished(self, val):
        logging.debug('protocol_functions.py - FTPProtocol - _download_finished')
        self._update_progress_bar(val)
        self.update_local_file_list.emit()
        self.download_finished.emit()

    def _all_download_canceled(self):
        logging.debug('protocol_functions.py - FTPProtocol - _all_download_canceled')
        text = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][3]
        find_text = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][1]
        for i in range(0, len(self.label_1)):
            if self.label_1[i].text() != find_text:
                self._update_progress_bar([i, text, '', '', 0])
        self.download_finished.emit()

    def _download_canceled(self, val):
        logging.debug('protocol_functions.py - FTPProtocol - _download_canceled')
        text = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][3]
        self._update_progress_bar([val, text, '', '', 0])
        self.download_finished.emit()

    def _download_failed(self):
        logging.debug('protocol_functions.py - FTPProtocol - _download_failed')
        text = self.translations_dict['downloadfailedtext'][self.config_dict['OPTIONS'].get('language')]
        self.infoWindow = MyInfo(text)
        self.infoWindow.exec_()
        self.download_finished.emit()

    def _add_files_to_frame(self, file_list):
        logging.debug('protocol_functions.py - FTPProtocol - _add_files_to_frame')
        self.gui_transfer_widget.clear()
        self.label_1 = []
        self.label_2 = []
        self.label_3 = []
        self.label_4 = []
        self.progress = []
        self.file_num = 0
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        for file in file_list:
            self.label_1.append(QtWidgets.QLabel())
            self.label_1[self.file_num].setMinimumSize(QtCore.QSize(0, 37))
            self.label_1[self.file_num].setMaximumSize(QtCore.QSize(16777215, 37))
            self.label_1[self.file_num].setFont(font)
            self.label_1[self.file_num].setStyleSheet("QLabel {\n"
                                                      "   margin: 5px;\n"
                                                      "   background: transparent;\n"
                                                      "   color: rgb(45,45,45);\n"
                                                      "}")
            self.label_1[self.file_num].setObjectName("label_1_" + str(self.file_num))
            text = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][2]
            self.label_1[self.file_num].setText(text)
            self.label_2.append(QtWidgets.QLabel())
            self.label_2[self.file_num].setMinimumSize(QtCore.QSize(0, 37))
            self.label_2[self.file_num].setMaximumSize(QtCore.QSize(16777215, 37))
            self.label_2[self.file_num].setFont(font)
            self.label_2[self.file_num].setStyleSheet("QLabel {\n"
                                                      "   margin: 5px;\n"
                                                      "   background: transparent;\n"
                                                      "   color: rgb(45,45,45);\n"
                                                      "}")
            self.label_2[self.file_num].setObjectName("label_2_" + str(self.file_num))
            self.label_2[self.file_num].setText(file['file'])
            self.label_2[self.file_num].setWordWrap(True)
            self.label_3.append(QtWidgets.QLabel())
            self.label_3[self.file_num].setMinimumSize(QtCore.QSize(0, 37))
            self.label_3[self.file_num].setMaximumSize(QtCore.QSize(16777215, 37))
            self.label_3[self.file_num].setFont(font)
            self.label_3[self.file_num].setStyleSheet("QLabel {\n"
                                                      "   margin: 5px;\n"
                                                      "   background: transparent;\n"
                                                      "   color: rgb(45,45,45);\n"
                                                      "}")
            self.label_3[self.file_num].setObjectName("label_3_" + str(self.file_num))
            self.label_3[self.file_num].setText(file['size'])
            self.label_3[self.file_num].setWordWrap(True)
            self.label_4.append(QtWidgets.QLabel())
            self.label_4[self.file_num].setMinimumSize(QtCore.QSize(0, 37))
            self.label_4[self.file_num].setMaximumSize(QtCore.QSize(16777215, 37))
            self.label_4[self.file_num].setFont(font)
            self.label_4[self.file_num].setStyleSheet("QLabel {\n"
                                                      "   margin: 5px;\n"
                                                      "   background: transparent;\n"
                                                      "   color: rgb(45,45,45);\n"
                                                      "}")
            self.label_4[self.file_num].setObjectName("label_4_" + str(self.file_num))
            self.progress.append(QtWidgets.QProgressBar())
            self.progress[self.file_num].setMinimumSize(QtCore.QSize(0, 35))
            self.progress[self.file_num].setMaximumSize(QtCore.QSize(16777215, 35))
            self.progress[self.file_num].setFont(font)
            self.progress[self.file_num].setMinimum(0)
            self.progress[self.file_num].setMaximum(100)
            self.progress[self.file_num].setValue(0)
            self.progress[self.file_num].setValue(0)
            self.progress[self.file_num].setTextVisible(True)
            self.progress[self.file_num].setObjectName("progress_" + str(self.file_num))
            self.progress[self.file_num].setStyleSheet("QProgressBar {\n"
                                                       "   margin: 5px;\n"
                                                       "   border: 0px solid black;\n"
                                                       "   border-radius: 3px;\n"
                                                       "   background: rgb(220,220,220);\n"
                                                       "   color: rgb(45,45,45);\n"
                                                       "   text-align: center;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QProgressBar::chunk {\n"
                                                       "   border: 0px solid black;\n"
                                                       "   border-radius: 3px;\n"
                                                       "   background: rgb(0,200,0);\n"
                                                       "}")
            CustomTreeItem(self.gui_transfer_widget,
                           self.label_1[self.file_num],
                           self.label_2[self.file_num],
                           self.label_3[self.file_num],
                           self.label_4[self.file_num],
                           self.progress[self.file_num])
            self.file_num += 1

    def _list_folders_files(self, first_listing=False, first_path=None, parent_index=None):
        logging.debug('protocol_functions.py - FTPProtocol - _list_folders_files')
        if first_listing:
            self.remote_path = str(first_path)
        listing = []
        self._update_connection_widget([1, 'LIST'])
        message = self.ftp_protocol.retrlines('LIST', listing.append)
        self._update_connection_widget([2, message])
        file_folder_list = self._parse_listing(listing)
        self._populate_path()
        self._populate_tree_up(file_folder_list, first_listing=first_listing, parent_index=parent_index)
        self._populate_tree_down(file_folder_list)

    def _build_remote_path(self, index):
        logging.debug('protocol_functions.py - FTPProtocol - _build_remote_path')
        path_list = list()
        while True:
            try:
                parent = self.gui_tree_up_model.itemFromIndex(index).parent()
                path_list.append(parent.text())
                index = parent.index()
            except AttributeError:
                break
        path = '/'.join(reversed(path_list))
        if path[:2] == '//':
            path = path[1:]
        if path[-1:] != '/':
            path += '/'
        return path

    def _populate_path(self):
        logging.debug('protocol_functions.py - FTPProtocol - _populate_path')
        if self.gui_path is not None:
            self.gui_path.setText(self.remote_path)

    def _populate_tree_up(self, file_folder_list, first_listing=False, parent_index=None):
        logging.debug('protocol_functions.py - FTPProtocol - _populate_tree_up')
        if first_listing:
            parent_item = self.gui_tree_up_model.invisibleRootItem()
            if self.display_icon:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap('icons/hdd_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                first_child = QtGui.QStandardItem(icon, '/')
            else:
                first_child = QtGui.QStandardItem('/')
            first_child.setEditable(False)
            parent_item.appendRow(first_child)
            for item in file_folder_list:
                if item[3] == 'folder':
                    if self.display_icon:
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap(item[4]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        child_item = QtGui.QStandardItem(icon, item[0])
                    else:
                        child_item = QtGui.QStandardItem(item[0])
                    child_item.setStatusTip('folder')
                    child_item.setEditable(False)
                    first_child.appendRow(child_item)
                else:
                    if self.one_tree_option:
                        if self.display_icon:
                            icon = QtGui.QIcon()
                            icon.addPixmap(QtGui.QPixmap(item[4]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                            child_item = QtGui.QStandardItem(icon, item[0])
                        else:
                            child_item = QtGui.QStandardItem(item[0])
                        child_item.setStatusTip('file')
                        child_item.setToolTip('Size: ' + item[2])
                        child_item.setEditable(False)
                        first_child.appendRow(child_item)
        else:
            if isinstance(parent_index, int):
                parent_index = self.gui_tree_up_model.index(parent_index, 0)
            parent_item = self.gui_tree_up_model.itemFromIndex(parent_index)
            if not parent_item.hasChildren():
                for item in file_folder_list:
                    if item[3] == 'folder':
                        if self.display_icon:
                            icon = QtGui.QIcon()
                            icon.addPixmap(QtGui.QPixmap(item[4]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                            child_item = QtGui.QStandardItem(icon, item[0])
                        else:
                            child_item = QtGui.QStandardItem(item[0])
                        child_item.setStatusTip('folder')
                        child_item.setEditable(False)
                        parent_item.appendRow(child_item)
                    else:
                        if self.one_tree_option:
                            if self.display_icon:
                                icon = QtGui.QIcon()
                                icon.addPixmap(QtGui.QPixmap(item[4]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                                child_item = QtGui.QStandardItem(icon, item[0])
                            else:
                                child_item = QtGui.QStandardItem(item[0])
                            child_item.setToolTip('Size: ' + item[2])
                            child_item.setStatusTip('file')
                            child_item.setEditable(False)
                            parent_item.appendRow(child_item)

    def _populate_tree_down(self, file_folder_list):
        logging.debug('protocol_functions.py - FTPProtocol - _populate_tree_down')
        self.gui_tree_down.clear()
        for item in file_folder_list:
            if item[3] != 'folder':
                widget = MyQTreeWidgetItem()
                widget.setText(0, item[0])
                widget.setSortData(1, item[1])
                widget.setText(1, item[2])
                widget.setText(2, item[3])
                if self.display_icon:
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(item[4]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    widget.setIcon(0, icon)
                self.gui_tree_down.addTopLevelItem(widget)

    def _update_connection_widget(self, message_list):
        logging.debug('protocol_functions.py - FTPProtocol - _update_connection_widget')
        item, message = message_list[0], message_list[1]
        color = None
        if item == 0:
            item = 'Status:'
            color = QtGui.QColor(45, 45, 45)
        elif item == 1:
            item = 'Command:'
            color = QtGui.QColor(0, 0, 200)
        elif item == 2:
            item = 'Response:'
            color = QtGui.QColor(0, 200, 0)
        elif item == 3:
            item = 'Error:'
            color = QtGui.QColor(200, 0, 0)
        index = self.gui_connect_widget.rowCount()
        self.gui_connect_widget.insertRow(index)
        status_item = QtWidgets.QTableWidgetItem(item)
        message_item = QtWidgets.QTableWidgetItem(message)
        status_item.setForeground(color)
        message_item.setForeground(QtGui.QColor(45, 45, 45))
        self.gui_connect_widget.setItem(index, 0, status_item)
        self.gui_connect_widget.setItem(index, 1, message_item)

    def _parse_listing(self, listing):
        logging.debug('protocol_functions.py - FTPProtocol - _parse_listing')
        clean_listing = list()
        folder_listing = list()
        file_listing = list()
        for l in listing:
            filename = ' '.join(l.split()[8:])
            filesize = int(l.split()[4])
            filesize_str = set_size(int(l.split()[4]))
            if l.split()[0][0] == 'd':
                filetype = 'folder'
                if self.display_icon:
                    iconfile = 'folder_icon.png'
                else:
                    iconfile = 'tree_none_icon.bmp'
                if self.one_tree_option:
                    folder_listing.append([filename, filesize, filesize_str, filetype, 'icons/' + iconfile])
            else:
                ext = filename[filename.rfind('.')+1:]
                if ext:
                    try:
                        filetype = self.file_types[ext]
                        iconfile = self.type_icons[filetype]
                    except KeyError:
                        filetype = ext + ' File'
                        iconfile = 'file_icon.png'
                else:
                    filetype = 'File'
                    iconfile = 'file_icon.png'
                if not self.display_icon:
                    iconfile = 'tree_none_icon.bmp'
                if self.one_tree_option:
                    file_listing.append([filename, filesize, filesize_str, filetype, 'icons/' + iconfile])
            if self.one_tree_option:
                folder_listing = sorted(folder_listing, key=lambda x: (x[0].upper()))
                file_listing = sorted(file_listing, key=lambda x: (x[0].upper()))
                clean_listing = folder_listing + file_listing
            else:
                clean_listing.append([filename, filesize, filesize_str, filetype, 'icons/' + iconfile])
        return clean_listing

    def _set_file_folder_list(self, local_path):
        file_list = list()
        if self.gui_tree_up.selectedIndexes():
            for index in self.gui_tree_up.selectedIndexes():
                if self.gui_tree_up_model.itemFromIndex(index).statusTip() != 'folder':
                    local_name = self._check_file_exist(self.gui_tree_up_model.itemFromIndex(index).text(), local_path)
                    if local_name is not None:
                        file_dict = {'path': self._build_remote_path(index),
                                     'file': self.gui_tree_up_model.itemFromIndex(index).text(),
                                     'size': self.gui_tree_up_model.itemFromIndex(index).toolTip(),
                                     'local_name': local_name}
                    else:
                        file_dict = None
                    file_list.append(file_dict)
        elif self.gui_tree_down.selectedItems():
            for item in self.gui_tree_down.selectedItems():
                local_name = self._check_file_exist(item.text(0), local_path)
                if local_name is not None:
                    file_dict = {'path': self.remote_path + '/',
                                 'file': item.text(0),
                                 'size': item.text(1),
                                 'local_name': local_name}
                else:
                    file_dict = None
                file_list.append(file_dict)

        if file_list:
            if all(item is None for item in file_list):
                file_list = None

        return file_list

    def _ftp_connection(self):
        self._update_connection_widget([0, 'Connecting to ' + self.host + ':' + self.port + '...'])
        if self.encryption == 'plain':
            ftp_protocol = ftplib.FTP(timeout=5)
        else:
            ftp_protocol = MyFTP_TLS(timeout=5)
        message = ftp_protocol.connect(self.host, int(self.port))
        self._update_connection_widget([2, message])
        if self.encryption != 'plain':
            self._update_connection_widget([1, 'AUTH TLS'])
            message = ftp_protocol.auth()
            self._update_connection_widget([2, message])
            self._update_connection_widget([1, 'PROT P'])
            message = ftp_protocol.prot_p()
            self._update_connection_widget([2, message])
        self._update_connection_widget([1, 'USER ' + self.username + ' ; PASS **************'])
        message = ftp_protocol.login(self.username, self.password)
        self._update_connection_widget([2, message])
        self._update_connection_widget([1, 'OPTS UTF8 ON'])
        message = ftp_protocol.sendcmd("OPTS UTF8 ON")
        self._update_connection_widget([2, message])
        ftp_protocol.encoding = 'utf-8'
        return ftp_protocol

    def _reset_up_down_tree(self):
        logging.debug('protocol_functions.py - FTPProtocol - reset_tree')
        self.gui_tree_down.clear()
        self.gui_tree_up_model.clear()
        first_column = self.translations_dict['qtreeview'][self.config_dict['OPTIONS'].get('language')][0]
        self.gui_tree_up_model.setColumnCount(3)
        self.gui_tree_up_model.setHeaderData(0, QtCore.Qt.Horizontal, first_column)
        self.gui_tree_up.hideColumn(1)
        self.gui_tree_up.hideColumn(2)

    def _check_file_exist(self, file, local_path):
        check_file = Path(local_path + '/' + file)
        try:
            if check_file.is_file():
                result = self._file_exist_question(file)
                if result is not None:
                    if result == 1:
                        return file
                    elif result == 2:
                        name, ext = os.path.splitext(file)
                        return name + '_copy' + ext
                    elif result == 3:
                        return None
                else:
                    raise AttributeError('The answer chosen by the user can\'t be None.')
            else:
                return file
        except AttributeError:
            logging.exception('protocol_functions.py - FTPProtocol - connection - The answer chosen by the user can\'t'
                              + 'be None.')
            self._update_connection_widget([3, 'The answer chosen by the user can\'t be None.'])
            self.download_finished.emit()

    def _file_exist_question(self, filename):
        if int(self.config_dict['TRANSFER'].get('file_exist_download')) == 0:
            self.myQuestion = MyQuestion(filename, self.config_dict, self.translations_dict)
            self.myQuestion.exec_()
            return self.myQuestion.result
        else:
            return self.ask_option

    def _update_local_down_widget(self):
        self.update_local_file_list.emit()


class MyFTP_TLS(ftplib.FTP_TLS):
    def ntransfercmd(self, cmd, rest=None):
        conn, size = ftplib.FTP.ntransfercmd(self, cmd, rest)
        if self._prot_p:
            conn = self.context.wrap_socket(conn, server_hostname=self.host, session=self.sock.session)
        return conn, size
