import logging
import os
import io
import configparser
import sys
import platform
import time
import copy
import tempfile
import shutil
import collections
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.Ui_mainwindow import Ui_MainWindow
from functions.utilities import translate_elements, copy_config_dict
from functions.window_functions import MyManager, MyAbout, MyOptions, MyWarningUpdate, MyUpdate, MyMainInfo, MyInfo
from functions.ftp_xml import create_profile_xml
from functions.thread_functions import CheckOrionFTPOnline
from functions.other_functions import set_ftp_profiles
from functions.protocol_functions import FTPProtocol, SFTPProtocol
from functions.gui_functions import prepare_tree_widgets, display_local_path, set_local_tree, set_remote_tree
from functions.gui_functions import activate_connexion_button, set_profile_list, activate_ftp_icons
from functions.gui_functions import deactivate_ftp_icons, clean_remote_widgets, deactivate_ftp_connection
from functions.gui_functions import activate_ftp_connection, set_one_two_local, set_one_two_remote
from functions.gui_functions import display_remote_path, set_local_icon_provider, set_connection_local_tree
from functions.gui_functions import display_file_folder_local_tree, set_local_files, set_default_path_local_tree
from functions.gui_functions import set_download_finished, transfer_tree_menu, connection_browser_menu
from functions.gui_functions import activate_download_button, set_splitter_position


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, config_dict, translations, parent=None):
        logging.debug('mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.gui_path = path
        self.config_dict = config_dict
        self.translations_dict = translations
        self.setupUi(self)
        self.link_latest_version = None
        self.check_downloader = None
        self.optionsWindow = None
        self.aboutWindow = None
        self.managerWindow = None
        self.updateWindow = None
        self.downloadWindow = None
        self.infoWindow = None
        self.protocol = None
        self.downloading = False
        self.ftp_profiles = collections.OrderedDict()
        self.hidden_items = {}
        self.old_local_path = ''
        self.local_path = ''
        self.transfert_tree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.transfert_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.transfert_tree.customContextMenuRequested.connect(lambda position: transfer_tree_menu(self, position))
        self.connexion_browser.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connexion_browser.customContextMenuRequested.connect(lambda position: connection_browser_menu(self,
                                                                                                           position))
        self.main_splitter_1.splitterMoved.connect(lambda left, right: set_splitter_position(self, left, right))
        self.main_splitter_3.setSizes([605, 605])
        translate_elements(self, self.config_dict['OPTIONS'].get('language'), self.translations_dict)
        set_ftp_profiles(self)
        set_profile_list(self)
        prepare_tree_widgets(self)
        display_local_path(self)
        display_remote_path(self)
        set_one_two_local(self)
        set_one_two_remote(self)
        set_local_tree(self)
        set_remote_tree(self)
        self.check_orionftp_update()
        self.info_button_1.clicked.connect(self.display_information)
        self.main_download_bt.clicked.connect(self.download_selection)
        self.main_connect_bt.clicked.connect(self.initiate_connection)
        self.main_profile_cb.currentIndexChanged.connect(lambda index: activate_connexion_button(self, index))
        self.main_profile_cb.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.transfert_tree.setHeaderHidden(False)
        set_default_path_local_tree(self)
        self.action_quit_bt.clicked.connect(self.close_window)
        self.action_option_bt.clicked.connect(self.open_options)
        self.action_about_bt.clicked.connect(self.open_about)
        self.action_update_bt.clicked.connect(self.download_and_install_update)
        self.action_refresh_bt.clicked.connect(self.refresh_remote_folder)
        self.action_close_bt.clicked.connect(self.close_connection)
        self.action_manager_bt.clicked.connect(self.open_manager)
        logging.info('mainwindow.py - MainWindow ready')

    def open_manager(self):
        logging.debug('mainwindow.py - open_manager')
        self.managerWindow = MyManager(self.config_dict, self.translations_dict, copy.deepcopy(self.ftp_profiles))
        self.managerWindow.exec_()
        if self.managerWindow.ftp_profiles is not None:
            self.ftp_profiles = self.managerWindow.ftp_profiles
            create_profile_xml('ftp_profiles.xml', self.managerWindow.ftp_profiles)
            set_profile_list(self)

    def open_about(self):
        logging.debug('mainwindow.py - open_about')
        self.aboutWindow = MyAbout(self.config_dict, self.translations_dict)
        self.aboutWindow.exec_()

    def open_options(self):
        logging.debug('mainwindow.py - open_options')
        old_config_dict = copy_config_dict(self.config_dict)
        ftp_profile_list = [key for key in self.ftp_profiles]
        config_string = io.StringIO()
        self.config_dict.write(config_string)
        config_string.seek(0)
        config_dict_copy = configparser.ConfigParser()
        config_dict_copy.read_file(config_string)
        self.optionsWindow = MyOptions(config_dict_copy, self.translations_dict, ftp_profile_list)
        self.optionsWindow.available_update.connect(self.parse_orionftp_update)
        self.optionsWindow.exec_()
        if self.optionsWindow.ow_config_dict is not None:
            logging.debug('mainwindow.py - open_options - saving config dict')
            self.config_dict = self.optionsWindow.ow_config_dict
            ini_file = open(os.path.join(self.gui_path, 'orion_ftp.ini'), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()
            self.apply_options(old_config_dict)

    def check_orionftp_update(self):
        logging.debug('mainwindow.py - check_orionftp_update')
        self.action_update_bt.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/orionftp_update_off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_update_bt.setIcon(icon)
        self.action_update_bt.setToolTip('')
        if self.config_dict['OPTIONS'].getboolean('check_update'):
            self.check_downloader = CheckOrionFTPOnline()
            self.check_downloader.start()
            self.check_downloader.finished.connect(self.parse_orionftp_update)
        else:
            logging.info('mainwindow.py - check_orionftp_update - from options, no update check')

    def parse_orionftp_update(self, val):
        logging.debug('mainwindow.py - parse_orionftp_update - val ' + str(val))
        if val == 'no new version':
            self.action_update_bt.setEnabled(False)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/orionftp_update_off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.action_update_bt.setIcon(icon)
            self.action_update_bt.setToolTip(self.translations_dict['nonewupdate'][self.config_dict['OPTIONS']
                                             .get('language')])
        elif 'http' in val:
            self.action_update_bt.setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/orionftp_update_on.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.action_update_bt.setIcon(icon)
            if getattr(sys, 'frozen', False):
                self.action_update_bt.setToolTip(self.translations_dict['newupdatefrozen'][self.config_dict['OPTIONS']
                                                 .get('language')])
            else:
                self.action_update_bt.setToolTip(self.translations_dict['newupdatesources'][self.config_dict['OPTIONS']
                                                 .get('language')])
            self.link_latest_version = val

    def download_and_install_update(self):
        logging.debug('mainwindow.py - download_and_install_update - link_latest_version '
                      + str(self.link_latest_version))
        if self.link_latest_version:
            frozen = False
            if getattr(sys, 'frozen', False):
                frozen = True
            self.updateWindow = MyWarningUpdate(frozen, self.config_dict, self.translations_dict)
            self.updateWindow.exec_()
            temp_folder = None
            if self.updateWindow.update:
                if frozen:
                    temp_folder = tempfile.gettempdir()
                else:
                    if platform.system() == 'Windows':
                        temp_folder = os.path.expanduser("~") + "\\Downloads\\"
                    elif platform.system() == 'Linux':
                        temp_folder = os.path.expanduser("~") + "/Downloads/"
                self.downloadWindow = MyUpdate(self.link_latest_version,
                                               temp_folder,
                                               self.config_dict,
                                               self.translations_dict)
                self.downloadWindow.exec_()
                logging.debug('mainwindow.py - download_and_install_update - download finished')
                if frozen:
                    filename = self.link_latest_version[self.link_latest_version.rfind('/') + 1:]
                    if platform.system() == 'Windows':
                        os.startfile(temp_folder + '\\' + filename)
                        time.sleep(0.1)
                        self.close()
                    elif platform.system() == 'Linux':
                        shutil.copy('functions/unzip_update.py', temp_folder)
                        install_folder = self.config_path + '/'
                        command = ('python3 ' + temp_folder + '/unzip_update.py ' + temp_folder
                                   + '/' + filename + ' ' + install_folder)
                        os.system('x-terminal-emulator -e ' + command)
                        time.sleep(0.1)
                        self.close()
                else:
                    time.sleep(0.1)
                    self.close()

    def display_information(self):
        logging.debug('mainwindow.py - Mainwindow - display_information')
        self.infoWindow = MyMainInfo(self.config_dict, self.translations_dict)
        self.infoWindow.exec_()

    def initiate_connection(self):
        logging.debug('mainwindow.py - Mainwindow - initiate_connection')
        if self.main_profile_cb.currentIndex() != 0:
            widget_list = [self.main_remote_ln, self.main_remote_tr_1, self.main_remote_tr_2,
                           self.connexion_browser, self.transfert_tree]
            if self.ftp_profiles[str(self.main_profile_cb.currentText())]['protocol'] == 'ftp':
                self.protocol = FTPProtocol(self.ftp_profiles[str(self.main_profile_cb.currentText())],
                                            widget_list,
                                            self.config_dict,
                                            self.translations_dict)
            elif self.ftp_profiles[str(self.main_profile_cb.currentText())]['protocol'] == 'sftp':
                self.protocol = SFTPProtocol(self.ftp_profiles[str(self.main_profile_cb.currentText())],
                                             widget_list,
                                             self.config_dict,
                                             self.translations_dict)
            self.protocol.update_local_file_list.connect(lambda: set_local_files(self))
            self.protocol.connection_success.connect(self.successful_connection)
            self.protocol.connection_failure.connect(self.unsuccessful_connection)
            self.protocol.connection_issue.connect(self.connection_issue)
            self.protocol.connection_closed.connect(self.connection_closed)
            self.protocol.download_finished.connect(lambda: set_download_finished(self))
            self.protocol.connection_start()

    def successful_connection(self):
        logging.debug('mainwindow.py - Mainwindow - successful_connection')
        activate_ftp_icons(self)
        deactivate_ftp_connection(self)
        self.main_local_ln.setSelection(0, 0)

    def unsuccessful_connection(self):
        logging.debug('mainwindow.py - Mainwindow - unsuccessful_connection')
        deactivate_ftp_icons(self)
        activate_ftp_connection(self)
        self.protocol = None
        text = self.translations_dict['connectiontimeout'][self.config_dict['OPTIONS'].get('language')]
        self.infoWindow = MyInfo(text)
        self.infoWindow.resize(450, 200)
        self.infoWindow.exec_()

    def connection_issue(self):
        logging.debug('mainwindow.py - Mainwindow - connection_issue')
        text = self.translations_dict['connectionissue'][self.config_dict['OPTIONS'].get('language')]
        self.infoWindow = MyInfo(text)
        self.infoWindow.resize(450, 200)
        self.infoWindow.exec_()

    def close_connection(self):
        logging.debug('mainwindow.py - MainWindow - close_connection')
        if self.protocol is not None:
            self.protocol.close_ftp()

    def connection_closed(self):
        logging.debug('mainwindow.py - Mainwindow - connection_closed')
        deactivate_ftp_icons(self)
        activate_ftp_connection(self)
        clean_remote_widgets(self)
        self.protocol = None
        set_download_finished(self)

    def refresh_remote_folder(self):
        logging.debug('mainwindow.py - MainWindow - refresh_remote_folder')
        if self.protocol is not None:
            try:
                index = self.main_remote_tr_1.selectedIndexes()[0]
                self.protocol.refresh(index)
            except IndexError:
                pass

    def download_selection(self):
        logging.debug('mainwindow.py - MainWindow - download_selection')
        if self.protocol is not None:
            self.main_tabwidget.setCurrentIndex(1)
            self.downloading = True
            self.protocol.download_selection(self.local_path)
            activate_download_button(self)

    def apply_options(self, config_dict):
        logging.debug('mainwindow.py - MainWindow - apply_options')
        if self.config_dict['OPTIONS'].get('language') != config_dict['language']:
            logging.debug('mainwindow.py - MainWindow - apply_options - language set')
            translate_elements(self, self.config_dict['OPTIONS'].get('language'), self.translations_dict)
            self.local_model.setText(self.translations_dict['qtreeview']
                                     [self.config_dict['OPTIONS'].get('language')][0])
            self.remote_model.setHeaderData(0,
                                            QtCore.Qt.Horizontal,
                                            self.translations_dict['qtreeview']
                                            [self.config_dict['OPTIONS'].get('language')][0])

        if self.config_dict['OPTIONS'].getboolean('check_update') and self.config_dict['OPTIONS'].getboolean(
                'check_update') != config_dict['check_update']:
            logging.debug('mainwindow.py - MainWindow - apply_options - update_check set')
            self.check_orionftp_update()

        if self.config_dict['LOG'].get('level') != config_dict['level']:
            logging.debug('mainwindow.py - MainWindow - apply_options - level set')
            logging.getLogger().setLevel(self.config_dict.get('LOG', 'level'))

        if (self.config_dict['INTERFACE'].getboolean('local_tree_one_widget') !=
                config_dict['local_tree_one_widget']):
            set_one_two_local(self)
            display_file_folder_local_tree(self)
            set_connection_local_tree(self)
            if not self.config_dict['INTERFACE'].getboolean('local_tree_one_widget'):
                set_local_files(self)

        if (self.config_dict['INTERFACE'].getboolean('display_icons_local_tree') !=
                config_dict['display_icons_local_tree']):
            set_local_icon_provider(self)
            if not self.config_dict['INTERFACE'].getboolean('local_tree_one_widget'):
                set_local_files(self)

        if (self.config_dict['INTERFACE'].getboolean('display_path_local_tree') !=
                config_dict['display_path_local_tree']):
            display_local_path(self)

        if (self.config_dict['INTERFACE'].getboolean('remote_tree_one_widget') !=
                config_dict['remote_tree_one_widget']):
            set_one_two_remote(self)
            if self.protocol is not None:
                self.protocol.one_tree_option = self.config_dict['INTERFACE'].getboolean('remote_tree_one_widget')
                self.protocol.reset_tree()

        if (self.config_dict['INTERFACE'].getboolean('display_icons_remote_tree') !=
                config_dict['display_icons_remote_tree']):
            if self.protocol is not None:
                self.protocol.display_icon = self.config_dict['INTERFACE'].getboolean('display_icons_remote_tree')
                self.protocol.reset_tree()

        if (self.config_dict['INTERFACE'].getboolean('display_path_remote_tree') !=
                config_dict['display_path_remote_tree']):
            display_remote_path(self)

    def close_window(self):
        logging.debug('mainwindow.py - MainWindow - close_window')
        self.close_connection()
        self.close()

    def closeEvent(self, event):
        logging.debug('mainwindow.py - MainWindow - closeEvent')
        logging.info('**********************************')
        logging.info('OrionFTP is closing ...')
        logging.info('**********************************')
