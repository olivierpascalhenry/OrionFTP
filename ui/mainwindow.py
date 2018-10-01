import logging
import os


from ui._version import _gui_version, _python_version, _qt_version
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.Ui_mainwindow import Ui_MainWindow
from functions.utilities import translate_elements, set_size
from functions.material_functions import objects_initialization
from functions.window_functions import MyManager, MyAbout, MyOptions
from functions.ftp_xml import read_profile_xml, create_profile_xml
from functions.gui_elements import MyQFileIconProvider, MyQFileSystemModel
from functions.thread_functions import FindFilesAndPopulate



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
        self.set_local_tree()
        self.set_profile_list()
        self.main_local_tr_2.setColumnWidth(0, 320)
        self.main_local_tr_2.setColumnWidth(1, 130)
        self.main_remote_tr_2.setColumnWidth(0, 319)
        self.main_remote_tr_2.setColumnWidth(1, 130)
        self.main_local_tr_2.sortItems(0, QtCore.Qt.AscendingOrder)
        self.main_remote_tr_2.sortItems(0, QtCore.Qt.AscendingOrder)
        #self.verticalLayout_2.takeAt(0)
        self.main_profile_cb.currentIndexChanged.connect(self.activate_connexion_button)
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
        print('No function yet.')
    
    
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
        self.optionsWindow = MyOptions(self.config_dict, self.translations_dict, ftp_profile_list)
        self.optionsWindow.exec_()
        if not self.optionsWindow.cancel:
            self.config_dict = self.optionsWindow.config_dict
            ini_file = open(os.path.join(self.gui_path, 'orion_ftp.ini'), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()
    
    def set_local_tree(self):
        self.model = MyQFileSystemModel(text=self.translations_dict['qtreeview_firstcolumn'][self.config_dict['OPTIONS'].get('language')])
        self.model.setRootPath('')
        self.model.setFilter(QtCore.QDir.AllDirs|QtCore.QDir.NoDotAndDotDot)
        self.model.setIconProvider(MyQFileIconProvider())
        self.main_local_tr_1.setModel(self.model)
        self.main_local_tr_1.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.main_local_tr_1.setColumnWidth(0, 540)
        self.main_local_tr_1.hideColumn(1)
        self.main_local_tr_1.hideColumn(2)
        self.main_local_tr_1.hideColumn(3)
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
            self.files_tree_thread = FindFilesAndPopulate(path, self.main_local_tr_2)
            self.files_tree_thread.start()
            
    
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
            
    
    def closeEvent(self, event):
        logging.debug('OrionFTP - mainwindow.py - MainWindow - closeEvent')
        logging.info('**********************************')
        logging.info('OrionFTP is closing ...')
        logging.info('**********************************')
        
        
