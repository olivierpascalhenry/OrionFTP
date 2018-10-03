# -*- coding: utf-8 -*-

import logging
import base64
import platform
import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_managerwindow import Ui_managerWindow
from ui.Ui_aboutlogwindow import Ui_aboutlogWindow
from ui.Ui_optionwindow import Ui_optionWindow
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_updatewindow import Ui_updateWindow
from ui.Ui_storewindow import Ui_storeWindow
from functions.utilities import translate_elements, clear_layout
from functions.material_functions import profile_window_objects_initialization
from functions.thread_functions import DownloadFile, CheckOrionFTPOnline


class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, infoText):
        logging.debug('gui - other_window_functions.py - MyInfo - __init__ : infoText ' + str(infoText))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)
        logging.info('gui - other_window_functions.py - MyInfo ready')

    def closeWindow(self):
        logging.debug('gui - other_window_functions.py - MyInfo - closeWindow')
        self.close()


class MyManager(QtWidgets.QDialog, Ui_managerWindow):
    def __init__(self, config_dict, translations_dict, ftp_profiles):
        logging.info('window_functions.py - MyManager - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.config_dict = config_dict
        self.translations_dict = translations_dict
        self.ftp_profiles = ftp_profiles
        self.current_name = ''
        self.save = False
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.mw_combobox.setItemDelegate(itemDelegate)
        profile_window_objects_initialization(self)
        self.resize(900, 360)
        translate_elements(self, config_dict['OPTIONS'].get('language'), translations_dict)
        self.parse_ftp_profiles()
        self.mw_cancel_button.clicked.connect(self.close_window)
        self.mw_ok_button.clicked.connect(self.save_profiles)
        self.mw_add_button.clicked.connect(self.add_profile_item)
        self.mw_del_button.clicked.connect(self.del_profile_item)
        self.mw_profile_list.currentTextChanged.connect(self.display_profile_data)
        self.mw_profile_list.itemChanged.connect(self.change_profile_name)
        
    def change_profile_name(self, val):
        try:
            self.ftp_profiles[str(val.text())] = self.ftp_profiles.pop(self.current_name)
            self.current_name = str(val.text())
        except KeyError:
            self.current_name = str(val.text())
        
    def set_data_in_dict(self, val):
        try:
            self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]
        except KeyError:
            profile = {'protocol': 'ftp', 'host':'', 'port':'', 'username':'', 'password':''}
            self.ftp_profiles[str(self.mw_profile_list.currentItem().text())] = profile
        if isinstance(self.sender(), QtWidgets.QComboBox):
            self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]['protocol'] = self.ftp_protocols_dict[str(self.sender().currentText())]
        elif isinstance(self.sender(), QtWidgets.QLineEdit):
            if '1' in self.sender().objectName():
                self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]['host'] = str(self.sender().text())
            elif '2' in self.sender().objectName():
                self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]['port'] = str(self.sender().text())
            elif '3' in self.sender().objectName():
                self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]['username'] = str(self.sender().text())
            elif '4' in self.sender().objectName():
                self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]['password'] = base64.b64encode(str.encode(self.sender().text()))
    
    def parse_ftp_profiles(self):
        for key in self.ftp_profiles:
            item = QtWidgets.QListWidgetItem()
            item.setText(key)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
            self.mw_profile_list.addItem(item)
        if self.mw_profile_list.count() > 0:
            self.mw_ok_button.setEnabled(True)
    
    def add_profile_item(self):
        i = self.mw_profile_list.count() + 1
        item = QtWidgets.QListWidgetItem()
        item.setText('new_server_' + str(i))
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        self.mw_profile_list.addItem(item)
        self.mw_profile_list.setCurrentItem(item)
        self.mw_profile_list.editItem(item)
        self.mw_ok_button.setEnabled(True)
    
    def del_profile_item(self):
        profile = str(self.mw_profile_list.currentItem().text())
        try:
            self.ftp_profiles.pop(profile)
        except KeyError:
            pass
        item = self.mw_profile_list.takeItem(self.mw_profile_list.currentRow())
        item = None
        self.deactivate_profile_fields()
            
    def display_profile_data(self, val):
        self.current_name = str(val)
        try:
            self.mw_combobox.currentIndexChanged.disconnect(self.set_data_in_dict)
            self.mw_line_1.textChanged.disconnect(self.set_data_in_dict)
            self.mw_line_2.textChanged.disconnect(self.set_data_in_dict)
            self.mw_line_3.textChanged.disconnect(self.set_data_in_dict)
            self.mw_line_4.textChanged.disconnect(self.set_data_in_dict)
        except:
            pass
        self.activate_profile_fields()
        try:
            profile = self.ftp_profiles[val]
            try:
                self.mw_combobox.setCurrentIndex(self.mw_combobox.findText(self.inv_ftp_protocols_dict[profile['protocol']]))
            except:
                pass
            try:
                self.mw_line_1.setText(profile['host'])
            except:
                pass
            try:
                self.mw_line_2.setText(profile['port'])
            except:
                pass
            try:
                self.mw_line_3.setText(profile['username'])
            except:
                pass
            try:
                self.mw_line_4.setText(base64.b64decode(profile['password']).decode('utf-8'))
            except:
                pass
            
        except KeyError:
            pass
        self.mw_combobox.currentIndexChanged.connect(self.set_data_in_dict)
        self.mw_line_1.textChanged.connect(self.set_data_in_dict)
        self.mw_line_2.textChanged.connect(self.set_data_in_dict)
        self.mw_line_3.textChanged.connect(self.set_data_in_dict)
        self.mw_line_4.textChanged.connect(self.set_data_in_dict)
        
    def activate_profile_fields(self):
        self.mw_combobox.setEnabled(True)
        self.mw_line_1.setEnabled(True)
        self.mw_line_2.setEnabled(True)
        self.mw_line_3.setEnabled(True)
        self.mw_line_4.setEnabled(True)
        self.mw_del_button.setEnabled(True)
        self.mw_combobox.setCurrentIndex(0)
        self.mw_line_1.setText('')
        self.mw_line_2.setText('')
        self.mw_line_3.setText('')
        self.mw_line_4.setText('')
    
    def deactivate_profile_fields(self):
        if self.mw_profile_list.count() == 0:
            self.mw_combobox.setEnabled(False)
            self.mw_line_1.setEnabled(False)
            self.mw_line_2.setEnabled(False)
            self.mw_line_3.setEnabled(False)
            self.mw_line_4.setEnabled(False)
            self.mw_del_button.setEnabled(False)
            self.mw_combobox.setCurrentIndex(0)
            self.mw_line_1.setText('')
            self.mw_line_2.setText('')
            self.mw_line_3.setText('')
            self.mw_line_4.setText('')
    
    def save_profiles(self):
        self.save = True
        self.close_window()
    
    def close_window(self):
        logging.debug('window_functions.py - MyManager - close_window')
        self.close()
    
    def closeEvent(self, event):
        if not self.save:
            self.ftp_profiles = None

        
class MyAbout(QtWidgets.QDialog, Ui_aboutlogWindow):
    def __init__(self, config_dict, translations_dict):
        logging.info('window_functions.py - MyAbout - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        translate_elements(self, config_dict['OPTIONS'].get('language'), translations_dict)
        self.aw_browser_2.setPlainText(open("documentation/changelog.txt").read())
        self.aw_button.clicked.connect(self.close_window)

    def close_window(self):
        logging.debug('window_functions.py - MyAbout - close_window')
        self.close()


class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    def __init__(self, ow_config_dict, translations_dict, ftp_profile_list):
        logging.info('window_functions.py - MyOptions - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.ow_config_dict = ow_config_dict
        self.translations_dict = translations_dict
        self.ftp_profile_list = ftp_profile_list
        self.ow_splitter.setSizes([150,700])
        for i in range(4):
            self.ow_section_list.item(i).setText(self.translations_dict['ow_section_list'][self.ow_config_dict['OPTIONS'].get('language')][i])
        self.ow_cancel_button.setText(self.translations_dict['ow_cancel_button'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_ok_button.clicked.connect(self.close_window)
        self.ow_cancel_button.clicked.connect(self.cancel_and_close)
        self.ow_section_list.itemSelectionChanged.connect(self.populate_options)
        self.ow_section_list.setCurrentRow(0)
        self.link_latest_version = None
    
    def populate_options(self):
        clear_layout(self.ow_vertical_layout)
        if self.ow_section_list.currentItem().text() == self.translations_dict['ow_section_list'][self.ow_config_dict['OPTIONS'].get('language')][0]:
            self.populate_general_options()
        if self.ow_section_list.currentItem().text() == self.translations_dict['ow_section_list'][self.ow_config_dict['OPTIONS'].get('language')][1]:
            self.populate_interface_options()
        if self.ow_section_list.currentItem().text() == self.translations_dict['ow_section_list'][self.ow_config_dict['OPTIONS'].get('language')][2]:
            self.populate_connection_options()
        if self.ow_section_list.currentItem().text() == self.translations_dict['ow_section_list'][self.ow_config_dict['OPTIONS'].get('language')][3]:
            self.populate_transfer_options()
    
    def populate_general_options(self):
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("FreeSans")
        font2.setPointSize(10)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.ow_combobox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.ow_combobox_2.setMinimumSize(QtCore.QSize(100, 27))
        self.ow_combobox_2.setMaximumSize(QtCore.QSize(100, 27))
        self.ow_combobox_2.setFont(font)
        self.ow_combobox_2.setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: rgb(45,45,45);\n"
        "}\n"
        "\n"
        "QComboBox:disabled {\n"
        "    background-color:  rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QComboBox:hover {\n"
        "    border: 1px solid #7eb4ea;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
        "}\n"
        "\n"
        "QComboBox::drop-down {\n"
        "    subcontrol-origin: padding;\n"
        "    subcontrol-position: top right;\n"
        "    width: 27px;\n"
        "    border-left-width: 1px;\n"
        "    border-left-color: darkgray;\n"
        "    border-left-style: solid;\n"
        "    border-top-right-radius: 3px;\n"
        "    border-bottom-right-radius: 3px;\n"
        "}\n"
        "\n"
        "QComboBox::down-arrow {\n"
        "    image: url(icons/down_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView {\n"
        "    selection-background-color: rgb(200,200,200);\n"
        "    selection-color: black;\n"
        "    background: #f0f0f0;\n"
        "    border: 0px solid #f0f0f0;\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView::item {\n"
        "    margin: 5px 5px 5px 5px;\n"
        "}")
        self.ow_combobox_2.setObjectName("ow_combobox_2")
        self.ow_combobox_2.addItem("")
        self.ow_combobox_2.addItem("")
        self.horizontalLayout_11.addWidget(self.ow_combobox_2)
        self.horizontalLayout_11.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ow_infoButton_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_1.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_1.setText("")
        self.ow_infoButton_1.setIcon(icon1)
        self.ow_infoButton_1.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_1.setAutoRaise(False)
        self.ow_infoButton_1.setObjectName("ow_infoButton_1")
        self.horizontalLayout_11.addWidget(self.ow_infoButton_1)
        self.horizontalLayout_11.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 3, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addItem(QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.line_1 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_1.setStyleSheet("QFrame {\n"
        "    background: rgb(190,190,190);\n"
        "    height: 5px;\n"
        "    border: 0px solid black;\n"
        "    margin-left: 10px;\n"
        "}")
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.verticalLayout_2.addWidget(self.line_1)
        self.verticalLayout_2.addItem(QtWidgets.QSpacerItem(14, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.gridLayout_3.addLayout(self.verticalLayout_2, 6, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addItem(QtWidgets.QSpacerItem(14, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setStyleSheet("QFrame {\n"
        "    background: rgb(190,190,190);\n"
        "    height: 5px;\n"
        "    border: 0px solid black;\n"
        "    margin-left: 10px;\n"
        "}")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.verticalLayout.addItem(QtWidgets.QSpacerItem(14, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.gridLayout_3.addLayout(self.verticalLayout, 2, 0, 1, 2)
        self.ow_label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_3.setMaximumSize(QtCore.QSize(16777215, 27))        
        self.ow_label_3.setFont(font2)
        self.ow_label_3.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "    margin-left: 10px;\n"
        "}")
        self.ow_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_3.setObjectName("ow_label_3")
        self.gridLayout_3.addWidget(self.ow_label_3, 3, 0, 1, 1)
        self.ow_label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_label_1.setFont(font2)
        self.ow_label_1.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "    margin-left: 10px;\n"
        "}")
        self.ow_label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_1.setObjectName("ow_label_1")
        self.gridLayout_3.addWidget(self.ow_label_1, 0, 0, 1, 1)
        self.ow_label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_label_4.setFont(font2)
        self.ow_label_4.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "    margin-left: 10px;\n"
        "}")
        self.ow_label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_4.setObjectName("ow_label_4")
        self.gridLayout_3.addWidget(self.ow_label_4, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ow_combobox_1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.ow_combobox_1.setMinimumSize(QtCore.QSize(100, 27))
        self.ow_combobox_1.setMaximumSize(QtCore.QSize(100, 27))
        self.ow_combobox_1.setFont(font)
        self.ow_combobox_1.setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: rgb(45,45,45);\n"
        "}\n"
        "\n"
        "QComboBox:disabled {\n"
        "    background-color:  rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QComboBox:hover {\n"
        "    border: 1px solid #7eb4ea;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
        "}\n"
        "\n"
        "QComboBox::drop-down {\n"
        "    subcontrol-origin: padding;\n"
        "    subcontrol-position: top right;\n"
        "    width: 27px;\n"
        "    border-left-width: 1px;\n"
        "    border-left-color: darkgray;\n"
        "    border-left-style: solid;\n"
        "    border-top-right-radius: 3px;\n"
        "    border-bottom-right-radius: 3px;\n"
        "}\n"
        "\n"
        "QComboBox::down-arrow {\n"
        "    image: url(icons/down_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView {\n"
        "    selection-background-color: rgb(200,200,200);\n"
        "    selection-color: black;\n"
        "    background: #f0f0f0;\n"
        "    border: 0px solid #f0f0f0;\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView::item {\n"
        "    margin: 5px 5px 5px 5px;\n"
        "}")
        self.ow_combobox_1.setObjectName("ow_combobox_1")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.horizontalLayout_7.addWidget(self.ow_combobox_1)
        self.horizontalLayout_7.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ow_infoButton_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_2.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_2.setText("")
        self.ow_infoButton_2.setIcon(icon1)
        self.ow_infoButton_2.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_2.setAutoRaise(False)
        self.ow_infoButton_2.setObjectName("ow_infoButton_2")
        self.horizontalLayout_7.addWidget(self.ow_infoButton_2)
        self.horizontalLayout_7.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.ow_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_label_2.setFont(font2)
        self.ow_label_2.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "    margin-left: 10px;\n"
        "}")
        self.ow_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_2.setObjectName("ow_label_2")
        self.gridLayout_3.addWidget(self.ow_label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ow_line_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.ow_line_1.setMinimumSize(QtCore.QSize(400, 27))
        self.ow_line_1.setMaximumSize(QtCore.QSize(400, 27))
        self.ow_line_1.setFont(font)
        self.ow_line_1.setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.ow_line_1.setObjectName("ow_line_1")
        self.horizontalLayout.addWidget(self.ow_line_1)
        self.ow_openButton_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_openButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_openButton_1.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_openButton_1.setText("")
        self.ow_openButton_1.setIcon(icon2)
        self.ow_openButton_1.setIconSize(QtCore.QSize(23, 23))
        self.ow_openButton_1.setAutoRaise(False)
        self.ow_openButton_1.setObjectName("ow_openButton_1")
        self.horizontalLayout.addWidget(self.ow_openButton_1)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ow_infoButton_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_3.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_3.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_3.setText("")
        self.ow_infoButton_3.setIcon(icon1)
        self.ow_infoButton_3.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_3.setAutoRaise(False)
        self.ow_infoButton_3.setObjectName("ow_infoButton_3")
        self.horizontalLayout.addWidget(self.ow_infoButton_3)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ow_line_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.ow_line_2.setMinimumSize(QtCore.QSize(400, 27))
        self.ow_line_2.setMaximumSize(QtCore.QSize(400, 27))
        self.ow_line_2.setFont(font)
        self.ow_line_2.setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.ow_line_2.setObjectName("ow_line_2")
        self.horizontalLayout_9.addWidget(self.ow_line_2)
        self.ow_openButton_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_openButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_openButton_2.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_openButton_2.setText("")
        self.ow_openButton_2.setIcon(icon2)
        self.ow_openButton_2.setIconSize(QtCore.QSize(23, 23))
        self.ow_openButton_2.setAutoRaise(False)
        self.ow_openButton_2.setObjectName("ow_openButton_2")
        self.horizontalLayout_9.addWidget(self.ow_openButton_2)
        self.horizontalLayout_9.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ow_infoButton_4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_4.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_4.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_4.setText("")
        self.ow_infoButton_4.setIcon(icon1)
        self.ow_infoButton_4.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_4.setAutoRaise(False)
        self.ow_infoButton_4.setObjectName("ow_infoButton_4")
        self.horizontalLayout_9.addWidget(self.ow_infoButton_4)
        self.horizontalLayout_9.addItem(QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 4, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ow_checkbox_1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_checkbox_1.setFont(font2)
        self.ow_checkbox_1.setStyleSheet("QCheckBox {\n"
        "    color: rgb(45,45,45);\n"
        "    margin-left: 10px;\n"
        "}")
        self.ow_checkbox_1.setObjectName("ow_checkbox_1")
        self.horizontalLayout_6.addWidget(self.ow_checkbox_1)
        self.horizontalLayout_6.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ow_check_button = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_check_button.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_check_button.setMaximumSize(QtCore.QSize(250, 27))
        self.ow_check_button.setFont(font2)
        self.ow_check_button.setStyleSheet("QToolButton {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
        "                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
        "    color: rgb(45,45,45);\n"
        "}\n"
        "\n"
        "QToolButton:hover {\n"
        "    border: 1px solid #7eb4ea;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
        "                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
        "}\n"
        "\n"
        "QToolButton:pressed {\n"
        "    border: 1px solid #579de5;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
        "                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
        "}")
        self.ow_check_button.setObjectName("ow_check_button")
        self.horizontalLayout_6.addWidget(self.ow_check_button)
        self.horizontalLayout_6.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ow_infoButton_5 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_5.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_5.setText("")
        self.ow_infoButton_5.setIcon(icon1)
        self.ow_infoButton_5.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_5.setAutoRaise(False)
        self.ow_infoButton_5.setObjectName("ow_infoButton_5")
        self.horizontalLayout_6.addWidget(self.ow_infoButton_5)
        self.horizontalLayout_6.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 7, 0, 1, 2)
        self.ow_label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_label_5.setFont(font2)
        self.ow_label_5.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "    margin-left: 10px;\n"
        "}")
        self.ow_label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_5.setObjectName("ow_label_5")
        self.gridLayout_3.addWidget(self.ow_label_5, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ow_combobox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.ow_combobox_3.setMinimumSize(QtCore.QSize(200, 27))
        self.ow_combobox_3.setMaximumSize(QtCore.QSize(200, 27))
        self.ow_combobox_3.setFont(font)
        self.ow_combobox_3.setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: rgb(45,45,45);\n"
        "}\n"
        "\n"
        "QComboBox:disabled {\n"
        "    background-color:  rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QComboBox:hover {\n"
        "    border: 1px solid #7eb4ea;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
        "}\n"
        "\n"
        "QComboBox::drop-down {\n"
        "    subcontrol-origin: padding;\n"
        "    subcontrol-position: top right;\n"
        "    width: 27px;\n"
        "    border-left-width: 1px;\n"
        "    border-left-color: darkgray;\n"
        "    border-left-style: solid;\n"
        "    border-top-right-radius: 3px;\n"
        "    border-bottom-right-radius: 3px;\n"
        "}\n"
        "\n"
        "QComboBox::down-arrow {\n"
        "    image: url(icons/down_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView {\n"
        "    selection-background-color: rgb(200,200,200);\n"
        "    selection-color: black;\n"
        "    background: #f0f0f0;\n"
        "    border: 0px solid #f0f0f0;\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView::item {\n"
        "    margin: 5px 5px 5px 5px;\n"
        "}")
        self.ow_combobox_3.setObjectName("ow_combobox_3")
        self.ow_combobox_3.addItem("")
        self.horizontalLayout_3.addWidget(self.ow_combobox_3)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ow_infoButton_6 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_6.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_6.setText("")
        self.ow_infoButton_6.setIcon(icon1)
        self.ow_infoButton_6.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_6.setAutoRaise(False)
        self.ow_infoButton_6.setObjectName("ow_infoButton_6")
        self.horizontalLayout_3.addWidget(self.ow_infoButton_6)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        self.ow_vertical_layout.addLayout(self.gridLayout_3)
        self.ow_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.ow_combobox_2.setItemText(0, "English")
        self.ow_combobox_2.setItemText(1, "Français")
        self.ow_label_3.setText(self.translations_dict['ow_label_3'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_label_1.setText(self.translations_dict['ow_label_1'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_label_4.setText(self.translations_dict['ow_label_4'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_combobox_1.setItemText(0, "DEBUG")
        self.ow_combobox_1.setItemText(1, "INFO")
        self.ow_combobox_1.setItemText(2, "WARNING")
        self.ow_combobox_1.setItemText(3, "CRITICAL")
        self.ow_combobox_1.setItemText(4, "ERROR")
        self.ow_label_2.setText(self.translations_dict['ow_label_2'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_checkbox_1.setText(self.translations_dict['ow_checkbox_1'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_check_button.setText(self.translations_dict['ow_check_button'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_label_5.setText(self.translations_dict['ow_label_5'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_combobox_3.setItemText(0, self.translations_dict['ow_combobox_3'][self.ow_config_dict['OPTIONS'].get('language')])
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.ow_combobox_1.setItemDelegate(itemDelegate)
        self.ow_combobox_2.setItemDelegate(itemDelegate)
        self.ow_combobox_3.setItemDelegate(itemDelegate)
        self.ow_openButton_1.clicked.connect(self.get_directory)
        self.ow_openButton_2.clicked.connect(self.get_directory)
        '''all_info_boxes = self.findChildren(QtWidgets.QToolButton)
        for widget in all_info_boxes:
            if 'infoButton' in widget.objectName():
                widget.clicked.connect(lambda: self.info_button())'''
        self.setTabOrder(self.ow_line_1,self.ow_line_2)
        self.set_ftp_profile_list()
        self.read_general_options()
        self.ow_combobox_1.currentIndexChanged.connect(self.set_combobox_options)
        self.ow_combobox_2.currentIndexChanged.connect(self.set_combobox_options)
        self.ow_combobox_3.currentIndexChanged.connect(self.set_combobox_options)
        self.ow_checkbox_1.stateChanged.connect(self.set_checkbox_options)
        self.ow_line_1.textChanged.connect(self.set_lineedit_options)
        self.ow_line_2.textChanged.connect(self.set_lineedit_options)
        self.ow_combobox_2.currentIndexChanged.connect(self.change_language)
        self.ow_check_button.clicked.connect(self.check_orionftp_update)
    
    def populate_interface_options(self):
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ow_label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_label_6.setFont(font2)
        self.ow_label_6.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "    margin-left: 10px;\n"
        "}")
        self.ow_label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_6.setObjectName("ow_label_6")
        self.horizontalLayout_4.addWidget(self.ow_label_6)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.ow_vertical_layout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.addItem(QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ow_checkbox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_checkbox_2.setFont(font)
        self.ow_checkbox_2.setStyleSheet("QCheckBox {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.ow_checkbox_2.setObjectName("ow_checkbox_2")
        self.gridLayout_3.addWidget(self.ow_checkbox_2, 0, 0, 1, 1)
        self.ow_infoButton_7 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_7.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_7.setText("")
        self.ow_infoButton_7.setIcon(icon1)
        self.ow_infoButton_7.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_7.setAutoRaise(False)
        self.ow_infoButton_7.setObjectName("ow_infoButton_7")
        self.gridLayout_3.addWidget(self.ow_infoButton_7, 0, 1, 1, 1)
        self.ow_checkbox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_checkbox_4.setFont(font)
        self.ow_checkbox_4.setStyleSheet("QCheckBox {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.ow_checkbox_4.setObjectName("ow_checkbox_4")
        self.gridLayout_3.addWidget(self.ow_checkbox_4, 1, 0, 1, 1)
        self.ow_infoButton_8 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_8.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_8.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_8.setText("")
        self.ow_infoButton_8.setIcon(icon1)
        self.ow_infoButton_8.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_8.setAutoRaise(False)
        self.ow_infoButton_8.setObjectName("ow_infoButton_8")
        self.gridLayout_3.addWidget(self.ow_infoButton_8, 1, 1, 1, 1)
        self.ow_checkbox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_6.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_6.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_checkbox_6.setFont(font)
        self.ow_checkbox_6.setStyleSheet("QCheckBox {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.ow_checkbox_6.setObjectName("ow_checkbox_6")
        self.gridLayout_3.addWidget(self.ow_checkbox_6, 2, 0, 1, 1)
        self.ow_infoButton_9 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_9.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_9.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_9.setText("")
        self.ow_infoButton_9.setIcon(icon1)
        self.ow_infoButton_9.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_9.setAutoRaise(False)
        self.ow_infoButton_9.setObjectName("ow_infoButton_9")
        self.gridLayout_3.addWidget(self.ow_infoButton_9, 2, 1, 1, 1)
        self.horizontalLayout_8.addLayout(self.gridLayout_3)
        self.horizontalLayout_8.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.ow_vertical_layout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.addItem(QtWidgets.QSpacerItem(14, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_4.setStyleSheet("QFrame {\n"
        "    background: rgb(190,190,190);\n"
        "    height: 5px;\n"
        "    border: 0px solid black;\n"
        "    margin-left: 10px;\n"
        "}")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.verticalLayout_3.addItem(QtWidgets.QSpacerItem(14, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.ow_vertical_layout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ow_label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_7.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_label_7.setFont(font2)
        self.ow_label_7.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "    margin-left: 10px;\n"
        "}")
        self.ow_label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_7.setObjectName("ow_label_7")
        self.horizontalLayout_5.addWidget(self.ow_label_7)
        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.ow_vertical_layout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.addItem(QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ow_checkbox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_checkbox_3.setFont(font)
        self.ow_checkbox_3.setStyleSheet("QCheckBox {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.ow_checkbox_3.setObjectName("ow_checkbox_3")
        self.gridLayout_4.addWidget(self.ow_checkbox_3, 0, 0, 1, 1)
        self.ow_infoButton_10 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_10.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_10.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_10.setText("")
        self.ow_infoButton_10.setIcon(icon1)
        self.ow_infoButton_10.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_10.setAutoRaise(False)
        self.ow_infoButton_10.setObjectName("ow_infoButton_10")
        self.gridLayout_4.addWidget(self.ow_infoButton_10, 0, 1, 1, 1)
        self.ow_checkbox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_5.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_checkbox_5.setFont(font)
        self.ow_checkbox_5.setStyleSheet("QCheckBox {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.ow_checkbox_5.setObjectName("ow_checkbox_5")
        self.gridLayout_4.addWidget(self.ow_checkbox_5, 1, 0, 1, 1)
        self.ow_infoButton_11 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_11.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_11.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_11.setText("")
        self.ow_infoButton_11.setIcon(icon1)
        self.ow_infoButton_11.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_11.setAutoRaise(False)
        self.ow_infoButton_11.setObjectName("ow_infoButton_11")
        self.gridLayout_4.addWidget(self.ow_infoButton_11, 1, 1, 1, 1)
        self.ow_checkbox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_7.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_7.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_checkbox_7.setFont(font)
        self.ow_checkbox_7.setStyleSheet("QCheckBox {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.ow_checkbox_7.setObjectName("ow_checkbox_7")
        self.gridLayout_4.addWidget(self.ow_checkbox_7, 2, 0, 1, 1)
        self.ow_infoButton_12 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_12.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_12.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_12.setText("")
        self.ow_infoButton_12.setIcon(icon1)
        self.ow_infoButton_12.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_12.setAutoRaise(False)
        self.ow_infoButton_12.setObjectName("ow_infoButton_12")
        self.gridLayout_4.addWidget(self.ow_infoButton_12, 2, 1, 1, 1)
        self.horizontalLayout_10.addLayout(self.gridLayout_4)
        self.horizontalLayout_10.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.ow_vertical_layout.addLayout(self.horizontalLayout_10)
        self.ow_label_6.setText(self.translations_dict['ow_label_6'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_checkbox_2.setText(self.translations_dict['ow_checkbox_2'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_checkbox_4.setText(self.translations_dict['ow_checkbox_4'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_checkbox_6.setText(self.translations_dict['ow_checkbox_6'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_label_7.setText(self.translations_dict['ow_label_7'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_checkbox_3.setText(self.translations_dict['ow_checkbox_3'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_checkbox_5.setText(self.translations_dict['ow_checkbox_5'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_checkbox_7.setText(self.translations_dict['ow_checkbox_7'][self.ow_config_dict['OPTIONS'].get('language')])
        self.read_interface_options()
        self.ow_checkbox_2.stateChanged.connect(self.set_checkbox_options)
        self.ow_checkbox_3.stateChanged.connect(self.set_checkbox_options)
        self.ow_checkbox_4.stateChanged.connect(self.set_checkbox_options)
        self.ow_checkbox_5.stateChanged.connect(self.set_checkbox_options)
        self.ow_checkbox_6.stateChanged.connect(self.set_checkbox_options)
        self.ow_checkbox_7.stateChanged.connect(self.set_checkbox_options)
    
    def populate_connection_options(self):
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ow_label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_8.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_8.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_label_8.setFont(font)
        self.ow_label_8.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.ow_label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_8.setObjectName("ow_label_8")
        self.gridLayout_3.addWidget(self.ow_label_8, 0, 0, 1, 1)
        self.gridLayout_3.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 0, 1, 1, 1)
        self.ow_combobox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.ow_combobox_4.setMinimumSize(QtCore.QSize(110, 27))
        self.ow_combobox_4.setMaximumSize(QtCore.QSize(110, 27))
        self.ow_combobox_4.setFont(font2)
        self.ow_combobox_4.setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: rgb(45,45,45);\n"
        "}\n"
        "\n"
        "QComboBox:disabled {\n"
        "    background-color:  rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QComboBox:hover {\n"
        "    border: 1px solid #7eb4ea;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
        "}\n"
        "\n"
        "QComboBox::drop-down {\n"
        "    subcontrol-origin: padding;\n"
        "    subcontrol-position: top right;\n"
        "    width: 27px;\n"
        "    border-left-width: 1px;\n"
        "    border-left-color: darkgray;\n"
        "    border-left-style: solid;\n"
        "    border-top-right-radius: 3px;\n"
        "    border-bottom-right-radius: 3px;\n"
        "}\n"
        "\n"
        "QComboBox::down-arrow {\n"
        "    image: url(icons/down_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView {\n"
        "    selection-background-color: rgb(200,200,200);\n"
        "    selection-color: black;\n"
        "    background: #f0f0f0;\n"
        "    border: 0px solid #f0f0f0;\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView::item {\n"
        "    margin: 5px 5px 5px 5px;\n"
        "}")
        self.ow_combobox_4.setObjectName("ow_combobox_4")
        self.ow_combobox_4.addItem("")
        self.ow_combobox_4.addItem("")
        self.gridLayout_3.addWidget(self.ow_combobox_4, 0, 2, 1, 1)
        self.gridLayout_3.addItem(QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 0, 3, 1, 2)
        self.ow_infoButton_13 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_13.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_13.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_13.setText("")
        self.ow_infoButton_13.setIcon(icon1)
        self.ow_infoButton_13.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_13.setAutoRaise(False)
        self.ow_infoButton_13.setObjectName("ow_infoButton_13")
        self.gridLayout_3.addWidget(self.ow_infoButton_13, 0, 5, 1, 1)
        self.ow_checkbox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_8.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_8.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_checkbox_8.setFont(font)
        self.ow_checkbox_8.setStyleSheet("QCheckBox {\n"
        "    color: rgb(45,45,45);\n"
        "    margin-right: 20px;\n"
        "}")
        self.ow_checkbox_8.setObjectName("ow_checkbox_8")
        self.gridLayout_3.addWidget(self.ow_checkbox_8, 1, 0, 1, 5)
        self.ow_infoButton_14 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_14.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_14.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_14.setText("")
        self.ow_infoButton_14.setIcon(icon1)
        self.ow_infoButton_14.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_14.setAutoRaise(False)
        self.ow_infoButton_14.setObjectName("ow_infoButton_14")
        self.gridLayout_3.addWidget(self.ow_infoButton_14, 1, 5, 1, 1)
        self.ow_label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_9.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_9.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_label_9.setFont(font)
        self.ow_label_9.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "}")
        self.ow_label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_9.setObjectName("ow_label_9")
        self.gridLayout_3.addWidget(self.ow_label_9, 2, 0, 1, 1)
        self.gridLayout_3.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum), 2, 1, 1, 1)
        self.ow_combobox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.ow_combobox_5.setMinimumSize(QtCore.QSize(130, 27))
        self.ow_combobox_5.setMaximumSize(QtCore.QSize(130, 27))
        self.ow_combobox_5.setFont(font2)
        self.ow_combobox_5.setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: rgb(45,45,45);\n"
        "}\n"
        "\n"
        "QComboBox:disabled {\n"
        "    background-color:  rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QComboBox:hover {\n"
        "    border: 1px solid #7eb4ea;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
        "}\n"
        "\n"
        "QComboBox::drop-down {\n"
        "    subcontrol-origin: padding;\n"
        "    subcontrol-position: top right;\n"
        "    width: 27px;\n"
        "    border-left-width: 1px;\n"
        "    border-left-color: darkgray;\n"
        "    border-left-style: solid;\n"
        "    border-top-right-radius: 3px;\n"
        "    border-bottom-right-radius: 3px;\n"
        "}\n"
        "\n"
        "QComboBox::down-arrow {\n"
        "    image: url(icons/down_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView {\n"
        "    selection-background-color: rgb(200,200,200);\n"
        "    selection-color: black;\n"
        "    background: #f0f0f0;\n"
        "    border: 0px solid #f0f0f0;\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView::item {\n"
        "    margin: 5px 5px 5px 5px;\n"
        "}")
        self.ow_combobox_5.setObjectName("ow_combobox_5")
        self.ow_combobox_5.addItem("")
        self.ow_combobox_5.addItem("")
        self.ow_combobox_5.addItem("")
        self.gridLayout_3.addWidget(self.ow_combobox_5, 2, 2, 1, 2)
        self.gridLayout_3.addItem(QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 2, 4, 1, 1)
        self.ow_infoButton_15 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_15.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_15.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_15.setText("")
        self.ow_infoButton_15.setIcon(icon1)
        self.ow_infoButton_15.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_15.setAutoRaise(False)
        self.ow_infoButton_15.setObjectName("ow_infoButton_15")
        self.gridLayout_3.addWidget(self.ow_infoButton_15, 2, 5, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.ow_vertical_layout.addLayout(self.horizontalLayout)
        self.ow_label_8.setText(self.translations_dict['ow_label_8'][self.ow_config_dict['OPTIONS'].get('language')])
        for i in range(2):
            self.ow_combobox_4.setItemText(i, self.translations_dict['ow_combobox_4'][self.ow_config_dict['OPTIONS'].get('language')][i])
        self.ow_checkbox_8.setText(self.translations_dict['ow_checkbox_8'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_label_9.setText(self.translations_dict['ow_label_9'][self.ow_config_dict['OPTIONS'].get('language')])
        for i in range(3):
            self.ow_combobox_5.setItemText(i, self.translations_dict['ow_combobox_5'][self.ow_config_dict['OPTIONS'].get('language')][i])
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.ow_combobox_4.setItemDelegate(itemDelegate)
        self.ow_combobox_5.setItemDelegate(itemDelegate)
        self.read_connection_options()
        self.ow_combobox_4.currentIndexChanged.connect(self.set_combobox_options)
        self.ow_combobox_5.currentIndexChanged.connect(self.set_combobox_options)
        self.ow_checkbox_8.stateChanged.connect(self.set_checkbox_options)
        
    def populate_transfer_options(self):
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ow_label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_11.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_11.setMaximumSize(QtCore.QSize(16777215, 27))
        self.ow_label_11.setFont(font)
        self.ow_label_11.setStyleSheet("QLabel {\n"
        "    color: rgb(45,45,45);\n"
        "    margin-left: 10px;\n"
        "}")
        self.ow_label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_11.setObjectName("ow_label_11")
        self.horizontalLayout.addWidget(self.ow_label_11)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ow_combobox_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.ow_combobox_6.setMinimumSize(QtCore.QSize(200, 27))
        self.ow_combobox_6.setMaximumSize(QtCore.QSize(300, 27))
        self.ow_combobox_6.setFont(font2)
        self.ow_combobox_6.setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "    color: rgb(45,45,45);\n"
        "}\n"
        "\n"
        "QComboBox:disabled {\n"
        "    background-color:  rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QComboBox:hover {\n"
        "    border: 1px solid #7eb4ea;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
        "}\n"
        "\n"
        "QComboBox::drop-down {\n"
        "    subcontrol-origin: padding;\n"
        "    subcontrol-position: top right;\n"
        "    width: 27px;\n"
        "    border-left-width: 1px;\n"
        "    border-left-color: darkgray;\n"
        "    border-left-style: solid;\n"
        "    border-top-right-radius: 3px;\n"
        "    border-bottom-right-radius: 3px;\n"
        "}\n"
        "\n"
        "QComboBox::down-arrow {\n"
        "    image: url(icons/down_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView {\n"
        "    selection-background-color: rgb(200,200,200);\n"
        "    selection-color: black;\n"
        "    background: #f0f0f0;\n"
        "    border: 0px solid #f0f0f0;\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView::item {\n"
        "    margin: 5px 5px 5px 5px;\n"
        "}")
        self.ow_combobox_6.setObjectName("ow_combobox_6")
        self.ow_combobox_6.addItem("")
        self.ow_combobox_6.addItem("")
        self.ow_combobox_6.addItem("")
        self.ow_combobox_6.addItem("")
        self.horizontalLayout.addWidget(self.ow_combobox_6)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ow_infoButton_16 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_infoButton_16.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_infoButton_16.setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ow_infoButton_16.setText("")
        self.ow_infoButton_16.setIcon(icon1)
        self.ow_infoButton_16.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_16.setAutoRaise(False)
        self.ow_infoButton_16.setObjectName("ow_infoButton_16")
        self.horizontalLayout.addWidget(self.ow_infoButton_16)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.ow_vertical_layout.addLayout(self.horizontalLayout) 
        self.ow_label_11.setText(self.translations_dict['ow_label_11'][self.ow_config_dict['OPTIONS'].get('language')])
        for i in range(4):
            self.ow_combobox_6.setItemText(i, self.translations_dict['ow_combobox_6'][self.ow_config_dict['OPTIONS'].get('language')][i])
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.ow_combobox_6.setItemDelegate(itemDelegate)
        self.read_transfer_options()
        self.ow_combobox_6.currentIndexChanged.connect(self.set_combobox_options)

    def change_language(self):
        for i in range(4):
            self.ow_section_list.item(i).setText(self.translations_dict['ow_section_list'][self.ow_config_dict['OPTIONS'].get('language')][i])
        self.ow_cancel_button.setText(self.translations_dict['ow_cancel_button'][self.ow_config_dict['OPTIONS'].get('language')])
        self.ow_section_list.setCurrentRow(1)
        self.ow_section_list.setCurrentRow(0)

    def set_combobox_options(self, val):
        logging.debug('window_functions.py - MyOptions - set_combobox_options')
        if self.sender().objectName() == 'ow_combobox_6':
            self.ow_config_dict.set('TRANSFER', 'file_exist_download', str(val))
        if self.sender().objectName() == 'ow_combobox_5':
            self.ow_config_dict.set('CONNECTION', 'default_transfer_type', str(val))
        if self.sender().objectName() == 'ow_combobox_4':
            self.ow_config_dict.set('CONNECTION', 'default_transfer_mode', str(val))
        if self.sender().objectName() == 'ow_combobox_3':
            if self.sender().currentIndex() == 0:
                self.ow_config_dict.set('OPTIONS', 'default_profile', '')
            else:
                self.ow_config_dict.set('OPTIONS', 'default_profile', str(self.sender().currentText()))
        if self.sender().objectName() == 'ow_combobox_2':
            self.ow_config_dict.set('OPTIONS', 'language', str(self.sender().currentText()).lower())
        if self.sender().objectName() == 'ow_combobox_1':
            self.ow_config_dict.set('LOG', 'level', str(self.sender().currentText()))
    
    def set_checkbox_options(self, val):
        logging.debug('window_functions.py - MyOptions - set_checkbox_options')
        if self.sender().objectName() == 'ow_checkbox_1':
            self.ow_config_dict.set('OPTIONS', 'check_update', str(self.sender().isChecked()))
        if self.sender().objectName() == 'ow_checkbox_2':
            self.ow_config_dict.set('INTERFACE', 'local_tree_one_widget', str(self.sender().isChecked()))
        if self.sender().objectName() == 'ow_checkbox_3':
            self.ow_config_dict.set('INTERFACE', 'remote_tree_one_widget', str(self.sender().isChecked()))
        if self.sender().objectName() == 'ow_checkbox_4':
            self.ow_config_dict.set('INTERFACE', 'display_icons_local_tree', str(self.sender().isChecked()))
        if self.sender().objectName() == 'ow_checkbox_5':
            self.ow_config_dict.set('INTERFACE', 'display_icons_remote_tree', str(self.sender().isChecked()))
        if self.sender().objectName() == 'ow_checkbox_6':
            self.ow_config_dict.set('INTERFACE', 'display_path_local_tree', str(self.sender().isChecked()))
        if self.sender().objectName() == 'ow_checkbox_7':
            self.ow_config_dict.set('INTERFACE', 'display_path_remote_tree', str(self.sender().isChecked()))
        if self.sender().objectName() == 'ow_checkbox_8':
            self.ow_config_dict.set('CONNECTION', 'transfer_mode_fall_back', str(self.sender().isChecked()))
    
    def set_lineedit_options(self, val):
        logging.debug('window_functions.py - MyOptions - set_lineedit_options')
        if self.sender().objectName() == 'ow_line_1':
            self.ow_config_dict.set('LOG', 'path', str(val))
        if self.sender().objectName() == 'ow_line_2':
            self.ow_config_dict.set('OPTIONS', 'local_home', str(val))
    
    def set_ftp_profile_list(self):
        logging.debug('window_functions.py - MyOptions - set_ftp_profile_list')
        if self.ftp_profile_list:
            self.ow_combobox_3.clear()
            self.ow_combobox_3.addItem(self.translations_dict['makeachoice'][self.ow_config_dict['OPTIONS'].get('language')])
            self.ow_combobox_3.addItems(self.ftp_profile_list)
    
    def read_general_options(self):
        logging.debug('window_functions.py - MyOptions - read_general_options')
        self.ow_combobox_1.setCurrentIndex(self.ow_combobox_1.findText(self.ow_config_dict.get('LOG', 'level')))
        self.ow_combobox_2.setCurrentIndex(self.ow_combobox_2.findText(self.ow_config_dict.get('OPTIONS', 'language').title()))
        self.ow_line_1.setText(self.ow_config_dict.get('LOG', 'path'))
        self.ow_line_2.setText(self.ow_config_dict.get('OPTIONS', 'local_home'))
        self.ow_checkbox_1.setChecked(self.ow_config_dict['OPTIONS'].getboolean('check_update'))
        if self.ow_config_dict.get('OPTIONS', 'default_profile'):
            self.ow_combobox_3.setCurrentIndex(self.ow_combobox_3.findText(self.ow_config_dict.get('OPTIONS', 'default_profile')))
        
    def read_interface_options(self):
        logging.debug('window_functions.py - MyOptions - read_interface_options')
        self.ow_checkbox_2.setChecked(self.ow_config_dict['INTERFACE'].getboolean('local_tree_one_widget'))
        self.ow_checkbox_3.setChecked(self.ow_config_dict['INTERFACE'].getboolean('remote_tree_one_widget'))
        self.ow_checkbox_4.setChecked(self.ow_config_dict['INTERFACE'].getboolean('display_icons_local_tree'))
        self.ow_checkbox_5.setChecked(self.ow_config_dict['INTERFACE'].getboolean('display_icons_remote_tree'))
        self.ow_checkbox_6.setChecked(self.ow_config_dict['INTERFACE'].getboolean('display_path_local_tree'))
        self.ow_checkbox_7.setChecked(self.ow_config_dict['INTERFACE'].getboolean('display_path_remote_tree'))
        
    def read_connection_options(self):
        logging.debug('window_functions.py - MyOptions - read_connection_options')
        self.ow_combobox_4.setCurrentIndex(int(self.ow_config_dict['CONNECTION'].get('default_transfer_mode')))
        self.ow_combobox_5.setCurrentIndex(int(self.ow_config_dict['CONNECTION'].get('default_transfer_type')))
        self.ow_checkbox_8.setChecked(self.ow_config_dict['CONNECTION'].getboolean('transfer_mode_fall_back'))
        
    def read_transfer_options(self):
        logging.debug('window_functions.py - MyOptions - read_transfer_options')
        self.ow_combobox_6.setCurrentIndex(int(self.ow_config_dict['TRANSFER'].get('file_exist_download')))
    
    def check_orionftp_update(self):
        self.check_downloader = CheckOrionFTPOnline()
        self.check_downloader.start()
        self.check_downloader.finished.connect(self.parse_orionftp_update)
    
    def parse_orionftp_update(self, val):
        if val == 'no new version':
            self.infoWindow = MyInfo(self.translations_dict['nonewupdateoption'][self.ow_config_dict['OPTIONS'].get('language')])
            self.infoWindow.resize(450, 150)
            self.infoWindow.exec_()
        elif 'http' in val:
            self.infoWindow = MyInfo(self.translations_dict['newupdateoption'][self.ow_config_dict['OPTIONS'].get('language')])
            self.infoWindow.resize(450, 150)
            self.infoWindow.exec_()
            self.link_latest_version = val
    
    def get_directory(self):
        logging.debug('window_functions.py - MyOptions - get_directory')
        file_dialog = QtWidgets.QFileDialog()
        out_dir = file_dialog.getExistingDirectory(self, "Select Directory")
        if self.sender().objectName() == 'ow_openButton_1':
            self.ow_line_1.setText(str(out_dir.replace('/','\\')))
        elif self.sender().objectName() == 'ow_openButton_2':
            self.ow_line_2.setText(str(out_dir.replace('/','\\')))
    
    def cancel_and_close(self):
        logging.debug('window_functions.py - MyOptions - save_and_close')
        self.ow_config_dict = None
        self.close_window()
    
    '''def info_button(self):
        logging.debug('window_functions.py - MyOptions - info_button - self.sender().objectName() ' + self.sender().objectName())
        if 'infoButton' in self.sender().objectName():
            self.infoWindow = MyInfo(self.info_text[self.sender().objectName()])
            self.infoWindow.move(QtGui.QCursor.pos().x() - 275, QtGui.QCursor.pos().y() + 20)
            self.infoWindow.exec_()'''
    
    def close_window(self):
        logging.info('window_functions.py - MyOptions - close_window')
        self.close()


class MyWarningUpdate(QtWidgets.QDialog, Ui_updateWindow):
    def __init__(self, frozen, config_dict, translations_dict):
        logging.info('window_functions.py - MyWarningUpdate - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        translate_elements(self, config_dict['OPTIONS'].get('language'), translations_dict)
        if not frozen:
            self.uw_label_1.setText(translations_dict['uw_label_1_sources'][config_dict['OPTIONS'].get('language')])
            self.uw_update_button.setText(translations_dict['uw_update_button_download'][config_dict['OPTIONS'].get('language')])
        else:
            self.uw_label_1.setText(translations_dict['uw_label_1_frozen'][config_dict['OPTIONS'].get('language')])
            self.uw_update_button.setText(translations_dict['uw_update_button_update'][config_dict['OPTIONS'].get('language')])
        self.uw_update_button.clicked.connect(self.agree_update)
        self.uw_cancel_button.clicked.connect(self.close_window)
        self.update = False
    
    def agree_update(self):
        logging.info('window_functions.py - MyWarningUpdate - agree_update')
        self.update = True
        self.close_window()
    
    def close_window(self):
        logging.info('window_functions.py - MyWarningUpdate - close_window')
        self.close()


class MyUpdate(QtWidgets.QDialog, Ui_storeWindow):
    def __init__(self, url, folder, config_dict, translations_dict):
        logging.info('window_functions.py - MyUpdate - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.config_dict = config_dict
        self.translations_dict = translations_dict
        translate_elements(self, config_dict['OPTIONS'].get('language'), translations_dict)
        self.temp_folder = folder
        self.url = url
        if platform.system() == 'Windows':
            self.update_file = self.temp_folder + self.url[self.url.rfind('/')+1:]
        elif platform.system() == 'Linux':
            self.update_file = self.temp_folder + self.url[self.url.rfind('/')+1:]
        self.sw_button.clicked.connect(self.cancel_download)
        self.cancel = False
        self.download_update()
    
    def update_progress_bar(self, val):
        if isinstance(val, list):
            self.sw_progressbar.setValue(val[0])
            self.sw_label.setText(val[1])
        else:
            self.sw_progressbar.setValue(val)
    
    def download_update(self):
        logging.debug('window_functions.py - MyUpdate - download_update')
        self.thread = DownloadFile(self.url, self.update_file, self.config_dict, self.translations_dict)
        self.thread.download_update.connect(self.update_progress_bar)
        self.thread.download_done.connect(self.close)
        self.thread.download_failed.connect(self.download_failed)
        self.thread.start()
    
    def cancel_download(self):
        logging.debug('window_functions.py - MyUpdate - cancel_download')
        self.thread.cancel_download()
        self.cancel = True
        time.sleep(0.25)
        self.close()
        
    def download_failed(self):
        logging.debug('window_functions.py - MyUpdate - download_failed')
        self.update_progress_bar(0)
        self.sw_label.setText(self.translations_dict['downloadfailed'][self.config_dict['OPTIONS'].get('language')])
        self.cancel_download()
        
    def closeEvent(self, event):
        logging.info('window_functions.py - MyUpdate - closeEvent')
        self.thread.download_update.disconnect(self.update_progress_bar)
        if self.cancel:
            try:
                os.remove(self.update_file)
            except PermissionError:
                pass



        
        
'''class MyCredentials(QtWidgets.QDialog, Ui_credentialsWindow):
    def __init__(self, user, password):
        QtWidgets.QWidget.__init__(self)
        logging.info('mainwindow.py - MyCredentials - __init__')
        self.setupUi(self)
        if user:
            self.edit_1.setText(user)
        if password:
            self.edit_2.setText(password)
        self.username = ''
        self.password = ''
        self.submit.clicked.connect(self.set_username_password)
        self.cancel.clicked.connect(self.closeWindow)

    def set_username_password(self):
        logging.debug('window_functions.py - MyCredentials - set_username_password')
        self.username = str(self.edit_1.text())
        self.password = str(self.edit_2.text())
        self.closeWindow()

    def closeWindow(self):
        logging.info('window_functions.py - MyCredentials - closeWindow')
        self.close()'''
        
        



'''class CustomTreeItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent, status_object, file_object, progress_object):
        super(CustomTreeItem, self).__init__(parent)
        parent.setItemWidget(self, 0, status_object)
        parent.setItemWidget(self, 1, file_object)
        parent.setItemWidget(self, 2, progress_object)'''


