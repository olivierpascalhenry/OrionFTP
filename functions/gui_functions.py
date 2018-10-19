import logging
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from functions.gui_elements import MyQFileIconProvider, MyQFileSystemModel, MyQTreeWidgetItem
from functions.thread_functions import FindFilesAndPopulate, SetDefaultLocalPath


def activate_ftp_icons(self):
    self.actionRefresh.setEnabled(True)
    self.actionClose.setEnabled(True)


def activate_ftp_connection(self):
    self.main_profile_cb.setEnabled(True)
    self.main_connect_bt.setEnabled(True)


def deactivate_ftp_connection(self):
    self.main_profile_cb.setEnabled(False)
    self.main_connect_bt.setEnabled(False)


def deactivate_ftp_icons(self):
    self.actionRefresh.setEnabled(False)
    self.actionClose.setEnabled(False)


def clean_remote_widgets(self):
    self.main_remote_tr_1.model().clear()
    self.main_remote_tr_2.clear()
    self.main_remote_ln.setText('')
    set_remote_tree(self, True)


def prepare_tree_widgets(self):
    logging.debug('gui_functions.py - prepare_tree_widgets')
    self.main_local_tr_2.setColumnWidth(0, 320)
    self.main_local_tr_2.setColumnWidth(1, 130)
    self.main_remote_tr_2.setColumnWidth(0, 319)
    self.main_remote_tr_2.setColumnWidth(1, 130)
    self.main_local_tr_2.sortItems(0, QtCore.Qt.AscendingOrder)
    self.main_remote_tr_2.sortItems(0, QtCore.Qt.AscendingOrder)
    self.transfert_tree.setColumnWidth(0, 150)
    self.transfert_tree.setColumnWidth(1, 500)
    self.transfert_tree.setColumnWidth(2, 120)
    self.transfert_tree.setColumnWidth(3, 120)
    self.connexion_browser.setColumnWidth(0, 90)
    self.connexion_browser.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


def set_one_two_local(self):
    logging.debug('gui_functions.py - set_one_two_local')
    if self.config_dict['INTERFACE'].getboolean('local_tree_one_widget'):
        if self.main_local_tr_2.isEnabled():
            self.main_local_tr_2.clear()
            self.main_local_tr_2.setEnabled(False)
            self.main_local_tr_2.hide()
    else:
        if not self.main_local_tr_2.isEnabled():
            self.main_local_tr_2.show()
            self.main_local_tr_2.setEnabled(True)
            self.main_local_tr_2.clear()


def set_one_two_remote(self):
    logging.debug('gui_functions.py - set_one_two_remote')
    if self.config_dict['INTERFACE'].getboolean('remote_tree_one_widget'):
        if self.main_remote_tr_2.isEnabled():
            self.main_remote_tr_2.clear()
            self.main_remote_tr_2.hide()
            self.main_remote_tr_2.setEnabled(False)
    else:
        if not self.main_remote_tr_2.isEnabled():
            self.main_remote_tr_2.show()
            self.main_remote_tr_2.setEnabled(True)
            self.main_remote_tr_2.clear()


def display_file_folder_local_tree(self):
    logging.debug('gui_functions.py - display_file_folder_local_tree')
    if self.config_dict['INTERFACE'].getboolean('local_tree_one_widget'):
        self.local_model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.Files | QtCore.QDir.NoDotAndDotDot)
    else:
        self.local_model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)


def set_local_icon_provider(self):
    logging.debug('gui_functions.py - set_local_icon_provider')
    my_icon_provider = MyQFileIconProvider(self.config_dict['INTERFACE'].getboolean('display_icons_local_tree'))
    self.local_model.setIconProvider(my_icon_provider)
    if not self.config_dict['INTERFACE'].getboolean('display_icons_local_tree'):
        self.main_local_tr_1.setIconSize(QtCore.QSize(0, 0))
    else:
        self.main_local_tr_1.setIconSize(QtCore.QSize(-1, -1))


def set_connection_local_tree(self):
    logging.debug('gui_functions.py - set_connection_local_tree')
    if not self.config_dict['INTERFACE'].getboolean('local_tree_one_widget'):
        try:
            self.main_local_tr_1.disconnect()
        except TypeError:
            pass
        self.main_local_tr_1.clicked.connect(lambda index: set_local_files(self, index))
        self.main_local_tr_1.clicked.connect(lambda: activate_download_button(self))
    else:
        try:
            self.main_local_tr_1.disconnect()
        except TypeError:
            pass
        self.main_local_tr_1.clicked.connect(lambda index: set_local_path(self, index))


def set_remote_tree(self, update=False):
    logging.debug('gui_functions.py - set_remote_tree')
    first_column = self.translations_dict['qtreeview'][self.config_dict['OPTIONS'].get('language')][0]
    self.main_remote_tr_1.clicked.connect(lambda: unset_selection_remote_trees(self))
    self.main_remote_tr_2.clicked.connect(lambda: unset_selection_remote_trees(self))
    self.main_remote_tr_1.clicked.connect(lambda: activate_download_button(self))
    self.main_remote_tr_2.clicked.connect(lambda: activate_download_button(self))
    if not update:
        self.remote_model = QtGui.QStandardItemModel()
    self.remote_model.setColumnCount(3)
    self.remote_model.setHeaderData(0, QtCore.Qt.Horizontal, first_column)
    self.main_remote_tr_1.setModel(self.remote_model)
    if not self.config_dict['INTERFACE'].getboolean('display_icons_remote_tree'):
        self.main_remote_tr_1.setIconSize(QtCore.QSize(0, 0))
    else:
        self.main_remote_tr_1.setIconSize(QtCore.QSize(-1, -1))
    self.main_remote_tr_1.sortByColumn(0, QtCore.Qt.AscendingOrder)
    self.main_remote_tr_1.header().setStretchLastSection(True)
    self.main_remote_tr_1.hideColumn(1)
    self.main_remote_tr_1.hideColumn(2)
    if not update:
        self.main_remote_tr_1.clicked.connect(lambda index: set_remote_files_folders(self, index))
        self.main_remote_tr_1.header().setStyleSheet("QHeaderView::section {\n"
                                                     "    background-color: rgb(253,253,253);\n"
                                                     "    color: rgb(45,45,45);\n"
                                                     "    border-top: 1px solid lightgray;\n"
                                                     "    border-bottom: 1px solid lightgray;\n"
                                                     "    border-right: 1px solid lightgray;\n"
                                                     "    padding-left: 10px;\n"
                                                     "    padding-bottom: 3px;\n"
                                                     "    height: 30px;\n"
                                                     "    font-family: \"fonts/SourceSansPro-Regular.ttf\";\n"
                                                     "    font-size: 15px;\n"
                                                     "}")


def set_local_tree(self):
    logging.debug('gui_functions.py - set_local_tree')
    first_column = self.translations_dict['qtreeview'][self.config_dict['OPTIONS'].get('language')][0]
    self.main_local_ln.setText('')
    self.local_model = MyQFileSystemModel(first_column, '', '')
    self.local_model.setRootPath('')
    self.local_model.setReadOnly(True)
    display_file_folder_local_tree(self)
    set_local_icon_provider(self)
    set_connection_local_tree(self)
    self.main_local_tr_1.setModel(self.local_model)
    self.main_local_tr_1.sortByColumn(0, QtCore.Qt.AscendingOrder)
    self.main_local_tr_1.header().setStretchLastSection(True)
    self.main_local_tr_1.hideColumn(1)
    self.main_local_tr_1.hideColumn(2)
    self.main_local_tr_1.hideColumn(3)
    self.main_local_tr_1.header().setStyleSheet("QHeaderView::section {\n"
                                                "    background-color: rgb(253,253,253);\n"
                                                "    color: rgb(45,45,45);\n"
                                                "    border-top: 1px solid lightgray;\n"
                                                "    border-bottom: 1px solid lightgray;\n"
                                                "    border-right: 1px solid lightgray;\n"
                                                "    padding-left: 10px;\n"
                                                "    padding-bottom: 3px;\n"
                                                "    height: 30px;\n"
                                                "    font-family: \"fonts/SourceSansPro-Regular.ttf\";\n"
                                                "    font-size: 15px;\n"
                                                "}")


def set_remote_files_folders(self, index):
    logging.debug('gui_functions.py - set_remote_files_folders')
    item = self.main_remote_tr_1.model().itemFromIndex(index)
    if item.statusTip() == 'folder':
        self.protocol.change_path(index)


def set_local_path(self, index):
    if self.sender().model().isDir(index):
        self.local_path = self.sender().model().filePath(index)
    else:
        self.local_path = os.path.dirname(self.sender().model().filePath(index))
    if self.local_path != self.old_local_path:
        self.old_local_path = self.local_path
    self.main_local_ln.setText(self.local_path)


def set_local_files(self, index=None):
    logging.debug('gui_functions.py - set_local_files')
    try:
        update = False
        if index is None:
            update = True
            index = self.main_local_tr_1.selectedIndexes()[0]
            if not self.main_local_tr_1.model().isDir(index):
                index = self.main_local_tr_1.model().parent(index)
            self.local_path = self.main_local_tr_1.model().filePath(index)
        else:
            self.local_path = self.sender().model().filePath(index)
        if update:
            self.main_local_tr_2.clear()
            self.files_tree_thread = FindFilesAndPopulate(self.local_path)
            self.files_tree_thread.finished.connect(lambda file_list: populate_local_files(self, file_list))
            self.files_tree_thread.start()
        else:
            if self.local_path != self.old_local_path:
                self.old_local_path = self.local_path
                self.main_local_ln.setText(self.local_path)
                self.main_local_tr_2.clear()
                self.files_tree_thread = FindFilesAndPopulate(self.local_path)
                self.files_tree_thread.finished.connect(lambda file_list: populate_local_files(self, file_list))
                self.files_tree_thread.start()
    except IndexError:
        logging.exception('gui_functions.py - set_local_files - exception - OrionFTP can\'t find the default path '
                          + 'saved in options.')


def populate_local_files(self, file_list):
    logging.debug('gui_functions.py - populate_local_files')
    for file_set in file_list:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(file_set[4]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = MyQTreeWidgetItem()
        item.setText(0, file_set[0])
        item.setSortData(1, file_set[1])
        item.setText(1, file_set[2])
        item.setText(2, file_set[3])
        if self.config_dict['INTERFACE'].getboolean('display_icons_local_tree'):
            item.setIcon(0, icon)
        self.main_local_tr_2.addTopLevelItem(item)


def set_profile_list(self):
    logging.debug('gui_functions.py - set_profile_list')
    ftp_profile_list = [key for key in self.ftp_profiles]
    if ftp_profile_list:
        self.main_profile_cb.clear()
        self.main_profile_cb.addItem(self.translations_dict['makeachoice'][self.config_dict['OPTIONS'].get('language')])
        self.main_profile_cb.addItems(ftp_profile_list)
        if self.config_dict['OPTIONS'].get('default_profile'):
            self.main_profile_cb.setCurrentIndex(self.main_profile_cb.findText(self.config_dict['OPTIONS']
                                                                               .get('default_profile')))
            self.main_connect_bt.setEnabled(True)


def display_local_path(self):
    logging.debug('gui_functions.py - display_local_path')
    if not self.config_dict['INTERFACE'].getboolean('display_path_local_tree'):
        try:
            self.hidden_items['local_path']
        except KeyError:
            self.hidden_items['local_path'] = {'object': self.verticalLayout_2.takeAt(0),
                                               'parent': self.verticalLayout_2,
                                               'index': 0,
                                               'hidden': True}
    else:
        try:
            self.verticalLayout_2.insertItem(0, self.hidden_items['local_path']['object'])
            self.hidden_items.pop('local_path')
        except KeyError:
            pass


def display_remote_path(self):
    logging.debug('gui_functions.py - display_remote_path')
    if not self.config_dict['INTERFACE'].getboolean('display_path_remote_tree'):
        try:
            self.hidden_items['remote_path']
        except KeyError:
            self.hidden_items['remote_path'] = {'object': self.verticalLayout_3.takeAt(0),
                                                'parent': self.verticalLayout_3,
                                                'index': 0,
                                                'hidden': True}
    else:
        try:
            self.verticalLayout_3.insertItem(0, self.hidden_items['remote_path']['object'])
            self.hidden_items.pop('remote_path')
        except KeyError:
            pass


def activate_connexion_button(self, index):
    logging.debug('gui_functions.py - activate_connexion_button')
    if index != 0:
        self.main_connect_bt.setEnabled(True)
    else:
        self.main_connect_bt.setEnabled(False)


def set_default_path_local_tree(self):
    if self.config_dict['OPTIONS'].get('local_home'):
        self.path_thread = SetDefaultLocalPath(self.config_dict['OPTIONS'].get('local_home'), self.main_local_tr_1)
        self.path_thread.finished.connect(lambda: set_local_files(self))
        self.path_thread.start()
        self.main_local_ln.setText(self.config_dict['OPTIONS'].get('local_home'))


def unset_selection_remote_trees(self):
    if self.sender().objectName() == 'main_remote_tr_1':
        self.main_remote_tr_2.selectionModel().clearSelection()
    elif self.sender().objectName() == 'main_remote_tr_2':
        self.main_remote_tr_1.selectionModel().clearSelection()


def activate_download_button(self):
    logging.debug('gui_functions.py - activate_download_button')
    item_selected, no_download, local_path, protocol = False, False, False, False
    up_selected_indexes = self.main_remote_tr_1.selectedIndexes()
    down_selected_items = self.main_remote_tr_2.selectedItems()
    if self.protocol is not None:
        protocol = True
    if up_selected_indexes or down_selected_items:
        item_selected = True
    if not self.downloading:
        no_download = True
    if self.local_path:
        local_path = True
    if item_selected and no_download and local_path and protocol:
        self.main_download_bt.setEnabled(True)
    else:
        self.main_download_bt.setEnabled(False)


def set_download_finished(self):
    logging.debug('gui_functions.py - set_download_finished')
    self.downloading = False
    activate_download_button(self)


def transfer_tree_menu(self, position):
    logging.debug('gui_functions.py - transfer_tree_menu')
    try:
        if self.downloading:
            items = self.transfert_tree.selectedItems()
            item_status = self.transfert_tree.itemWidget(items[0], 0).text()
            menu = QtWidgets.QMenu()
            queued_text = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][2]
            downloading_text = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][0]
            if queued_text in item_status:
                menu.addAction(self.translations_dict['transfermenu'][self.config_dict['OPTIONS'].get('language')][2])
            elif downloading_text in item_status:
                menu.addAction(menu.addAction(self.translations_dict['transfermenu'][self.config_dict['OPTIONS']
                                              .get('language')][0]))
            menu.addAction(menu.addAction(self.translations_dict['transfermenu'][self.config_dict['OPTIONS']
                                          .get('language')][1]))
            menu.triggered[QtWidgets.QAction].connect(lambda action: transfer_process_trigger(self, action))
            menu.exec_(self.transfert_tree.viewport().mapToGlobal(position))
        else:
            if self.transfert_tree.topLevelItemCount() > 0:
                menu = QtWidgets.QMenu()
                menu.addAction(self.translations_dict['transfermenu'][self.config_dict['OPTIONS'].get('language')][3])
                menu.triggered[QtWidgets.QAction].connect(lambda action: transfer_process_trigger(self, action))
                menu.exec_(self.transfert_tree.viewport().mapToGlobal(position))
    except IndexError:
        pass


def connection_browser_menu(self, position):
    logging.debug('gui_functions.py - transfer_tree_menu')
    menu = QtWidgets.QMenu()
    text = self.translations_dict['connectionmenu'][self.config_dict['OPTIONS'].get('language')]
    menu.addAction(text)
    menu.triggered[QtWidgets.QAction].connect(lambda action: connection_process_trigger(self, action))
    menu.exec_(self.connexion_browser.viewport().mapToGlobal(position))


def transfer_process_trigger(self, action):
    logging.debug('gui_functions.py - transfer_process_trigger')
    if self.protocol is not None:
        if action.text() == self.translations_dict['transfermenu'][self.config_dict['OPTIONS'].get('language')][0]:
            self.protocol.cancel_download()
        elif action.text() == self.translations_dict['transfermenu'][self.config_dict['OPTIONS'].get('language')][1]:
            self.protocol.cancel_all_download()
        elif action.text() == self.translations_dict['transfermenu'][self.config_dict['OPTIONS'].get('language')][2]:
            self.protocol.remove_from_list()
    if action.text() == self.translations_dict['transfermenu'][self.config_dict['OPTIONS'].get('language')][3]:
        self.protocol.clear_transfers()


def connection_process_trigger(self, action):
    logging.debug('gui_functions.py - connection_process_trigger')
    if action.text() == self.translations_dict['connectionmenu'][self.config_dict['OPTIONS'].get('language')]:
        self.connexion_browser.clear()
        for i in reversed(range(self.connexion_browser.rowCount())):
            self.connexion_browser.removeRow(i)
