import logging
from PyQt5 import QtWidgets, QtCore, QtGui
from functions.gui_elements import MyQFileIconProvider, MyQFileSystemModel, MyQTreeWidgetItem
from functions.thread_functions import FindFilesAndPopulate


def prepare_tree_widgets(self):
    logging.debug('gui_functions.py - prepare_tree_widgets')
    self.main_local_tr_2.setColumnWidth(0, 320)
    self.main_local_tr_2.setColumnWidth(1, 130)
    self.main_remote_tr_2.setColumnWidth(0, 319)
    self.main_remote_tr_2.setColumnWidth(1, 130)
    self.main_local_tr_2.sortItems(0, QtCore.Qt.AscendingOrder)
    self.main_remote_tr_2.sortItems(0, QtCore.Qt.AscendingOrder)


def display_one_two_tree(self, startup=False):
    logging.debug('gui_functions.py - display_one_two_tree')
    if self.config_dict['INTERFACE'].getboolean('local_tree_one_widget'):
        if self.main_local_tr_2.isEnabled():
            self.main_local_tr_2.setEnabled(False)
            self.main_local_tr_2.hide()
        set_local_tree(self)
    else:
        if not self.main_local_tr_2.isEnabled():
            self.main_local_tr_2.show()
            self.main_local_tr_2.setEnabled(True)
            self.main_local_tr_2.clear()
        set_local_tree(self)
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
    logging.debug('gui_functions.py - set_local_tree')
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
    else:
        self.main_local_tr_1.setIconSize(QtCore.QSize(-1,-1))  
    self.main_local_tr_1.sortByColumn(0, QtCore.Qt.AscendingOrder)  
    self.main_local_tr_1.setColumnWidth(0, 540)
    self.main_local_tr_1.hideColumn(1)
    self.main_local_tr_1.hideColumn(2)
    self.main_local_tr_1.hideColumn(3)
    if not self.config_dict['INTERFACE'].getboolean('local_tree_one_widget'):
        self.main_local_tr_1.clicked.connect(lambda index: set_local_files(self, index))
    else:
        self.main_local_tr_1.disconnect()
    font = QtGui.QFont()
    font.setFamily("fonts/SourceSansPro-Regular.ttf")
    font.setPointSize(12)
    font.setBold(False)
    font.setWeight(50)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.main_local_tr_1.header().setFont(font)


def set_local_files(self, index):
    logging.debug('gui_functions.py - set_local_files')
    path = self.sender().model().filePath(index)
    if path != self.old_local_path:
        self.old_local_path = path
        self.main_local_ln.setText(path)
        self.main_local_tr_2.clear()
        self.files_tree_thread = FindFilesAndPopulate(path)
        self.files_tree_thread.finished.connect(lambda file_list: populate_local_files(self, file_list))
        self.files_tree_thread.start()


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
            self.main_profile_cb.setCurrentIndex(self.main_profile_cb.findText(self.config_dict['OPTIONS'].get('default_profile')))
            self.main_connect_bt.setEnabled(True)


def display_local_path(self):
    logging.debug('gui_functions.py - display_local_path')
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


def activate_connexion_button(self, index):
    logging.debug('gui_functions.py - activate_connexion_button')
    if index != 0:
        self.main_connect_bt.setEnabled(True)
    else:
        self.main_connect_bt.setEnabled(False)


