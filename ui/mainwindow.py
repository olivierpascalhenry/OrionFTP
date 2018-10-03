import logging
import os
import io
import configparser
import sys
import platform
import time
from ui._version import _gui_version, _python_version, _qt_version
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.Ui_mainwindow import Ui_MainWindow
from functions.utilities import translate_elements, set_size
from functions.material_functions import objects_initialization
from functions.window_functions import MyManager, MyAbout, MyOptions, MyWarningUpdate, MyUpdate
from functions.ftp_xml import read_profile_xml, create_profile_xml
from functions.gui_elements import MyQFileIconProvider, MyQFileSystemModel, MyQTreeWidgetItem
from functions.thread_functions import FindFilesAndPopulate, CheckOrionFTPOnline


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, config_dict, translations, parent=None):
        logging.debug('OrionFTP - mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.gui_path = path
        self.config_dict = config_dict
        self.translations_dict = translations
        self.setupUi(self)
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.main_profile_cb.setItemDelegate(itemDelegate)
        objects_initialization(self)
        translate_elements(self, self.config_dict['OPTIONS'].get('language'), self.translations_dict)
        self.transfert_tree.setHeaderHidden(False)
        self.set_ftp_profiles()
        
        self.set_profile_list()
        
        self.main_local_tr_2.setColumnWidth(0, 320)
        self.main_local_tr_2.setColumnWidth(1, 130)
        self.main_remote_tr_2.setColumnWidth(0, 319)
        self.main_remote_tr_2.setColumnWidth(1, 130)
        self.main_local_tr_2.sortItems(0, QtCore.Qt.AscendingOrder)
        self.main_remote_tr_2.sortItems(0, QtCore.Qt.AscendingOrder)
        self.main_profile_cb.currentIndexChanged.connect(self.activate_connexion_button)
        
        
        self.display_local_path()
        self.display_one_two_tree(startup=True)
        self.check_orionftp_update()
        
        logging.info('OrionFTP - mainwindow.py - MainWindow ready')
        
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
        self.managerWindow = MyManager(self.config_dict, self.translations_dict, self.ftp_profiles)
        self.managerWindow.exec_()
        if self.managerWindow.ftp_profiles is not None:
            create_profile_xml(self,'ftp_profiles.xml', self.managerWindow.ftp_profiles)
        
        
    
    def open_about(self):
        self.aboutWindow = MyAbout(self.config_dict, self.translations_dict)
        self.aboutWindow.exec_()
    
    def open_options(self):
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
            self.config_dict = self.optionsWindow.ow_config_dict
            ini_file = open(os.path.join(self.gui_path, 'orion_ftp.ini'), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()
            logging.getLogger().setLevel(self.config_dict.get('LOG', 'level'))
            if self.config_dict['OPTIONS'].get('language') != old_language:
                translate_elements(self, self.config_dict['OPTIONS'].get('language'), self.translations_dict)
                self.model.setText(self.translations_dict['qtreeview_firstcolumn'][self.config_dict['OPTIONS'].get('language')])
            if self.config_dict['OPTIONS'].getboolean('check_update'):
                self.check_orionftp_update()
            self.display_local_path()
            self.display_one_two_tree()
        if self.optionsWindow.link_latest_version is not None:
            self.parse_orionftp_update(self.optionsWindow.link_latest_version)   
    
    def display_one_two_tree(self, startup=False):
        if self.config_dict['INTERFACE'].getboolean('local_tree_one_widget'):
            if self.main_local_tr_2.isEnabled():
                self.main_local_tr_2.setEnabled(False)
                self.main_local_tr_2.hide()
                self.set_local_tree()
        else:
            if not self.main_local_tr_2.isEnabled():
                self.main_local_tr_2.show()
                self.main_local_tr_2.setEnabled(True)
                self.main_local_tr_2.clear()
                self.set_local_tree()
            if startup:
                self.set_local_tree()
        if self.config_dict['INTERFACE'].getboolean('remote_tree_one_widget'):
            if self.main_remote_tr_2.isEnabled():
                self.main_remote_tr_2.hide()
                self.main_remote_tr_2.setEnabled(False)
        else:
            if not self.main_remote_tr_2.isEnabled():
                self.main_remote_tr_2.show()
                self.main_remote_tr_2.setEnabled(True)
                self.main_remote_tr_2.clear()
    
    def set_local_tree(self):
        first_column = self.translations_dict['qtreeview'][self.config_dict['OPTIONS'].get('language')][0]
        second_column = self.translations_dict['qtreeview'][self.config_dict['OPTIONS'].get('language')][1]
        third_column = self.translations_dict['qtreeview'][self.config_dict['OPTIONS'].get('language')][2]
        self.model = MyQFileSystemModel(first_column, second_column, third_column)
        self.model.setRootPath('')
        if self.config_dict['INTERFACE'].getboolean('local_tree_one_widget'):
            self.model.setFilter(QtCore.QDir.AllDirs|QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
            
        else:
            self.model.setFilter(QtCore.QDir.AllDirs|QtCore.QDir.NoDotAndDotDot)
        
        self.model.setIconProvider(MyQFileIconProvider(self.config_dict['INTERFACE'].getboolean('display_icons_local_tree')))
        self.main_local_tr_1.setModel(self.model)
        
        if not self.config_dict['INTERFACE'].getboolean('display_icons_local_tree'):
            self.main_local_tr_1.setIconSize(QtCore.QSize(0,0))
        
        #self.main_local_tr_1.setIconSize(QtCore.QSize(-1,-1))
        
        self.main_local_tr_1.sortByColumn(0, QtCore.Qt.AscendingOrder)
        
        self.main_local_tr_1.setColumnWidth(0, 540)
        self.main_local_tr_1.hideColumn(1)
        self.main_local_tr_1.hideColumn(2)
        self.main_local_tr_1.hideColumn(3)
        if not self.config_dict['INTERFACE'].getboolean('local_tree_one_widget'):
            self.main_local_tr_1.clicked.connect(self.set_local_files)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_local_tr_1.header().setFont(font)
    
    def set_local_files(self, index):
        path = self.sender().model().filePath(index)
        if path != self.old_local_path:
            self.old_local_path = path
            self.main_local_ln.setText(path)
            self.main_local_tr_2.clear()
            self.files_tree_thread = FindFilesAndPopulate(path)
            self.files_tree_thread.finished.connect(self.populate_local_files)
            self.files_tree_thread.start()
        
    def populate_local_files(self, file_list):
        for file_set in file_list:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(file_set[4]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item = MyQTreeWidgetItem()
            item.setText(0, file_set[0])
            item.setSortData(1, file_set[1])
            item.setText(1, file_set[2])
            item.setText(2, file_set[3])
            item.setIcon(0, icon)
            self.main_local_tr_2.addTopLevelItem(item)
    
    def set_ftp_profiles(self):
        if os.path.isfile('ftp_profiles.xml'):
            self.ftp_profiles = read_profile_xml(self, 'ftp_profiles.xml')
    
    def set_profile_list(self):
        ftp_profile_list = [key for key in self.ftp_profiles]
        if ftp_profile_list:
            self.main_profile_cb.clear()
            self.main_profile_cb.addItem(self.translations_dict['makeachoice'][self.config_dict['OPTIONS'].get('language')])
            self.main_profile_cb.addItems(ftp_profile_list)
            if self.config_dict['OPTIONS'].get('default_profile'):
                self.main_profile_cb.setCurrentIndex(self.main_profile_cb.findText(self.config_dict['OPTIONS'].get('default_profile')))
                self.main_connect_bt.setEnabled(True)
            
    def activate_connexion_button(self, index):
        if index != 0:
            self.main_connect_bt.setEnabled(True)
        else:
            self.main_connect_bt.setEnabled(False)
    
    def display_local_path(self):
        if not self.config_dict['INTERFACE'].getboolean('display_path_local_tree'):
            try:
                self.hidden_items['local_path']
            except KeyError:
                self.hidden_items['local_path'] = {'object': self.verticalLayout_2.takeAt(0), 'parent': self.verticalLayout_2,
                                                   'index': 0, 'hidden': True}
        else:
            try:
                self.verticalLayout_2.insertItem(0, self.hidden_items['local_path']['object'])
                self.hidden_items.pop('local_path')
            except KeyError:
                pass
        if not self.config_dict['INTERFACE'].getboolean('display_path_remote_tree'):
            try:
                self.hidden_items['remote_path']
            except KeyError:
                self.hidden_items['remote_path'] = {'object': self.verticalLayout_3.takeAt(0), 'parent': self.verticalLayout_3,
                                                    'index': 0, 'hidden': True}
        else:
            try:
                self.verticalLayout_3.insertItem(0, self.hidden_items['remote_path']['object'])
                self.hidden_items.pop('remote_path')
            except KeyError:
                pass
        
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
    
    def closeEvent(self, event):
        logging.debug('OrionFTP - mainwindow.py - MainWindow - closeEvent')
        logging.info('**********************************')
        logging.info('OrionFTP is closing ...')
        logging.info('**********************************')
        
        
