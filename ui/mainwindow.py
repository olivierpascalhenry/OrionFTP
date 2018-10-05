import logging
import os
import io
import configparser
import sys
import platform
import time
import copy
from ui._version import _gui_version, _python_version, _qt_version
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.Ui_mainwindow import Ui_MainWindow
from functions.utilities import translate_elements, set_size
from functions.material_functions import objects_initialization
from functions.window_functions import MyManager, MyAbout, MyOptions, MyWarningUpdate, MyUpdate, MyMainInfo
from functions.ftp_xml import read_profile_xml, create_profile_xml
from functions.thread_functions import FindFilesAndPopulate, CheckOrionFTPOnline
from functions.gui_functions import display_one_two_tree, prepare_tree_widgets, display_local_path, activate_connexion_button, set_profile_list
from functions.other_functions import set_ftp_profiles


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, config_dict, translations, parent=None):
        logging.debug('mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.gui_path = path
        self.config_dict = config_dict
        self.translations_dict = translations
        self.setupUi(self)
        objects_initialization(self)
        translate_elements(self, self.config_dict['OPTIONS'].get('language'), self.translations_dict)
        set_ftp_profiles(self)
        set_profile_list(self)
        prepare_tree_widgets(self)
        display_local_path(self)
        display_one_two_tree(self, startup=True)
        self.check_orionftp_update()
        self.info_button_1.clicked.connect(self.display_information)
        self.main_profile_cb.currentIndexChanged.connect(lambda index: activate_connexion_button(self, index))
        self.main_profile_cb.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.transfert_tree.setHeaderHidden(False)
        logging.info('mainwindow.py - MainWindow ready')
        
    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()
    
    @QtCore.pyqtSlot()
    def on_actionManager_triggered(self):
        self.open_manager()
    
    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        self.open_about()
        
    @QtCore.pyqtSlot()
    def on_actionOptions_triggered(self):
        self.open_options()
    
    @QtCore.pyqtSlot()
    def on_actionClose_triggered(self):
        print('No function yet.')
    
    @QtCore.pyqtSlot()
    def on_actionHome_triggered(self):
        print('No function yet.')
    
    @QtCore.pyqtSlot()
    def on_actionRefresh_triggered(self):
        print('No function yet.')
    
    @QtCore.pyqtSlot()
    def on_actionUpdate_triggered(self):
        self.download_and_install_update()
    
    def open_manager(self):
        logging.debug('mainwindow.py - open_manager')
        self.managerWindow = MyManager(self.config_dict, self.translations_dict, copy.deepcopy(self.ftp_profiles))
        self.managerWindow.exec_()
        if self.managerWindow.ftp_profiles is not None:
            self.ftp_profiles = self.managerWindow.ftp_profiles
            create_profile_xml(self,'ftp_profiles.xml', self.managerWindow.ftp_profiles)
            set_profile_list(self)
    
    def open_about(self):
        logging.debug('mainwindow.py - open_about')
        self.aboutWindow = MyAbout(self.config_dict, self.translations_dict)
        self.aboutWindow.exec_()
    
    def open_options(self):
        logging.debug('mainwindow.py - open_options')
        ftp_profile_list = [key for key in self.ftp_profiles]
        old_language = self.config_dict['OPTIONS'].get('language')
        config_string = io.StringIO()
        self.config_dict.write(config_string)
        config_string.seek(0) 
        config_dict_copy = configparser.ConfigParser()
        config_dict_copy.read_file(config_string)
        self.optionsWindow = MyOptions(config_dict_copy, self.translations_dict, ftp_profile_list)
        self.optionsWindow.exec_()
        if self.optionsWindow.ow_config_dict is not None:
            logging.debug('mainwindow.py - open_options - saving config dict')
            self.config_dict = self.optionsWindow.ow_config_dict
            ini_file = open(os.path.join(self.gui_path, 'orion_ftp.ini'), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()
            logging.getLogger().setLevel(self.config_dict.get('LOG', 'level'))
            if self.config_dict['OPTIONS'].get('language') != old_language:
                translate_elements(self, self.config_dict['OPTIONS'].get('language'), self.translations_dict)
                self.model.setText(self.translations_dict['qtreeview'][self.config_dict['OPTIONS'].get('language')])
            if self.config_dict['OPTIONS'].getboolean('check_update'):
                self.check_orionftp_update()
            display_local_path(self)
            display_one_two_tree(self)
        if self.optionsWindow.link_latest_version is not None:
            self.parse_orionftp_update(self.optionsWindow.link_latest_version)   
        
    def check_orionftp_update(self):
        logging.debug('mainwindow.py - check_orionftp_update')
        self.actionUpdate.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/orionftp_update_off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate.setIcon(icon)
        self.actionUpdate.setToolTip('')
        if self.config_dict['OPTIONS'].getboolean('check_update'):
            self.check_downloader = CheckOrionFTPOnline()
            self.check_downloader.start()
            self.check_downloader.finished.connect(self.parse_orionftp_update)
        else:
            logging.info('mainwindow.py - check_orionftp_update - from options, no update check')
    
    def parse_orionftp_update(self, val):
        logging.debug('mainwindow.py - parse_orionftp_update - val ' + str(val))
        if val == 'no new version':
            self.actionUpdate.setEnabled(False)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/orionftp_update_off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionUpdate.setIcon(icon)
            self.actionUpdate.setToolTip(self.translations_dict['nonewupdate'][self.config_dict['OPTIONS'].get('language')])
        elif 'http' in val:
            self.actionUpdate.setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/orionftp_update_on.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionUpdate.setIcon(icon)
            if getattr(sys, 'frozen', False ) :
                self.actionUpdate.setToolTip(self.translations_dict['newupdatefrozen'][self.config_dict['OPTIONS'].get('language')])
            else:
                self.actionUpdate.setToolTip(self.translations_dict['newupdatesources'][self.config_dict['OPTIONS'].get('language')])
            self.link_latest_version = val
    
    def download_and_install_update(self):
        logging.debug('mainwindow.py - download_and_install_update - link_latest_version ' + str(self.link_latest_version))
        if self.link_latest_version:
            frozen = False
            height = 250
            if getattr(sys, 'frozen', False) :
                frozen = True
                height = 200
            self.updateWindow = MyWarningUpdate(frozen, self.config_dict, self.translations_dict)
            self.updateWindow.exec_()
            if self.updateWindow.update:
                if getattr(sys, 'frozen', False) :
                    temp_folder = tempfile.gettempdir()
                else:
                    if platform.system() == 'Windows':
                        temp_folder = os.path.expanduser("~") + "\\Downloads\\"
                    elif platform.system() == 'Linux':
                        temp_folder = os.path.expanduser("~") + "/Downloads/"
                self.downloadWindow = MyUpdate(self.link_latest_version, temp_folder, self.config_dict, self.translations_dict)
                self.downloadWindow.exec_()
                logging.debug('mainwindow.py - download_and_install_update - download finished')
                if getattr(sys, 'frozen', False) :
                    filename = self.link_latest_version[self.link_latest_version.rfind('/')+1:]
                    if platform.system() == 'Windows':
                        os.startfile(temp_folder + '\\' + filename)
                        time.sleep(0.1)
                        self.close()
                    elif platform.system() == 'Linux':
                        shutil.copy('functions/unzip_update.py', temp_folder)
                        install_folder = self.config_path + '/'
                        command = 'python3 ' + temp_folder + '/unzip_update.py ' + temp_folder + '/' + filename + ' ' + install_folder
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
    
    def closeEvent(self, event):
        logging.debug('mainwindow.py - MainWindow - closeEvent')
        logging.info('**********************************')
        logging.info('OrionFTP is closing ...')
        logging.info('**********************************')
        
        
