# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_optionWindow(object):
    def setupUi(self, optionWindow):
        optionWindow.setObjectName("optionWindow")
        optionWindow.resize(677, 374)
        optionWindow.setMinimumSize(QtCore.QSize(0, 0))
        optionWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        optionWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        optionWindow.setWindowIcon(icon)
        optionWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(optionWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.ow_combobox_2 = QtWidgets.QComboBox(optionWindow)
        self.ow_combobox_2.setMinimumSize(QtCore.QSize(100, 27))
        self.ow_combobox_2.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
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
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.ow_infoButton_3 = QtWidgets.QToolButton(optionWindow)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_infoButton_3.setIcon(icon1)
        self.ow_infoButton_3.setIconSize(QtCore.QSize(23, 23))
        self.ow_infoButton_3.setAutoRaise(False)
        self.ow_infoButton_3.setObjectName("ow_infoButton_3")
        self.horizontalLayout_11.addWidget(self.ow_infoButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_11, 3, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.line = QtWidgets.QFrame(optionWindow)
        self.line.setStyleSheet("QFrame {\n"
"    background: rgb(190,190,190);\n"
"    height: 5px;\n"
"    border: 0px solid black;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem3 = QtWidgets.QSpacerItem(14, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_2, 6, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(14, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.line_3 = QtWidgets.QFrame(optionWindow)
        self.line_3.setStyleSheet("QFrame {\n"
"    background: rgb(190,190,190);\n"
"    height: 5px;\n"
"    border: 0px solid black;\n"
"}")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        spacerItem5 = QtWidgets.QSpacerItem(14, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 2)
        self.ow_label_3 = QtWidgets.QLabel(optionWindow)
        self.ow_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_3.setFont(font)
        self.ow_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_3.setObjectName("ow_label_3")
        self.gridLayout.addWidget(self.ow_label_3, 3, 0, 1, 1)
        self.ow_label_1 = QtWidgets.QLabel(optionWindow)
        self.ow_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_1.setFont(font)
        self.ow_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_1.setObjectName("ow_label_1")
        self.gridLayout.addWidget(self.ow_label_1, 0, 0, 1, 1)
        self.ow_label_4 = QtWidgets.QLabel(optionWindow)
        self.ow_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_4.setFont(font)
        self.ow_label_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_4.setObjectName("ow_label_4")
        self.gridLayout.addWidget(self.ow_label_4, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ow_combobox_1 = QtWidgets.QComboBox(optionWindow)
        self.ow_combobox_1.setMinimumSize(QtCore.QSize(100, 27))
        self.ow_combobox_1.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
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
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.ow_infoButton_1 = QtWidgets.QToolButton(optionWindow)
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
        self.horizontalLayout_7.addWidget(self.ow_infoButton_1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.ow_label_2 = QtWidgets.QLabel(optionWindow)
        self.ow_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_2.setFont(font)
        self.ow_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_2.setObjectName("ow_label_2")
        self.gridLayout.addWidget(self.ow_label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ow_line_1 = QtWidgets.QLineEdit(optionWindow)
        self.ow_line_1.setMinimumSize(QtCore.QSize(400, 27))
        self.ow_line_1.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_1.setFont(font)
        self.ow_line_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_1.setObjectName("ow_line_1")
        self.horizontalLayout.addWidget(self.ow_line_1)
        self.ow_openButton_1 = QtWidgets.QToolButton(optionWindow)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_openButton_1.setIcon(icon2)
        self.ow_openButton_1.setIconSize(QtCore.QSize(23, 23))
        self.ow_openButton_1.setAutoRaise(False)
        self.ow_openButton_1.setObjectName("ow_openButton_1")
        self.horizontalLayout.addWidget(self.ow_openButton_1)
        spacerItem8 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.ow_infoButton_2 = QtWidgets.QToolButton(optionWindow)
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
        self.horizontalLayout.addWidget(self.ow_infoButton_2)
        spacerItem9 = QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ow_line_2 = QtWidgets.QLineEdit(optionWindow)
        self.ow_line_2.setMinimumSize(QtCore.QSize(400, 27))
        self.ow_line_2.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_2.setFont(font)
        self.ow_line_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_2.setObjectName("ow_line_2")
        self.horizontalLayout_9.addWidget(self.ow_line_2)
        self.ow_openButton_2 = QtWidgets.QToolButton(optionWindow)
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
        spacerItem10 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.ow_infoButton_4 = QtWidgets.QToolButton(optionWindow)
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
        spacerItem11 = QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ow_checkbox_1 = QtWidgets.QCheckBox(optionWindow)
        self.ow_checkbox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_1.setFont(font)
        self.ow_checkbox_1.setStyleSheet("QCheckBox {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_checkbox_1.setObjectName("ow_checkbox_1")
        self.horizontalLayout_6.addWidget(self.ow_checkbox_1)
        spacerItem12 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.ow_check_button = QtWidgets.QToolButton(optionWindow)
        self.ow_check_button.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_check_button.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ow_check_button.setFont(font)
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
        spacerItem13 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.ow_infoButton_6 = QtWidgets.QToolButton(optionWindow)
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
        self.horizontalLayout_6.addWidget(self.ow_infoButton_6)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 0, 1, 2)
        self.ow_label_5 = QtWidgets.QLabel(optionWindow)
        self.ow_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_5.setFont(font)
        self.ow_label_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_5.setObjectName("ow_label_5")
        self.gridLayout.addWidget(self.ow_label_5, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ow_combobox_3 = QtWidgets.QComboBox(optionWindow)
        self.ow_combobox_3.setMinimumSize(QtCore.QSize(200, 27))
        self.ow_combobox_3.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
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
        spacerItem15 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.ow_infoButton_5 = QtWidgets.QToolButton(optionWindow)
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
        self.horizontalLayout_3.addWidget(self.ow_infoButton_5)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem17, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem18)
        self.ow_ok_button = QtWidgets.QToolButton(optionWindow)
        self.ow_ok_button.setMinimumSize(QtCore.QSize(100, 27))
        self.ow_ok_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ow_ok_button.setFont(font)
        self.ow_ok_button.setStyleSheet("QToolButton {\n"
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
        self.ow_ok_button.setObjectName("ow_ok_button")
        self.horizontalLayout_2.addWidget(self.ow_ok_button)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem19)
        self.ow_cancel_button = QtWidgets.QToolButton(optionWindow)
        self.ow_cancel_button.setMinimumSize(QtCore.QSize(100, 27))
        self.ow_cancel_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ow_cancel_button.setFont(font)
        self.ow_cancel_button.setStyleSheet("QToolButton {\n"
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
        self.ow_cancel_button.setObjectName("ow_cancel_button")
        self.horizontalLayout_2.addWidget(self.ow_cancel_button)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem20)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(optionWindow)
        QtCore.QMetaObject.connectSlotsByName(optionWindow)

    def retranslateUi(self, optionWindow):
        _translate = QtCore.QCoreApplication.translate
        optionWindow.setWindowTitle(_translate("optionWindow", "Options"))
        self.ow_combobox_2.setItemText(0, _translate("optionWindow", "English"))
        self.ow_combobox_2.setItemText(1, _translate("optionWindow", "Français"))
        self.ow_label_3.setText(_translate("optionWindow", "Language:"))
        self.ow_label_1.setText(_translate("optionWindow", "Logging level:"))
        self.ow_label_4.setText(_translate("optionWindow", "Default folder:"))
        self.ow_combobox_1.setItemText(0, _translate("optionWindow", "DEBUG"))
        self.ow_combobox_1.setItemText(1, _translate("optionWindow", "INFO"))
        self.ow_combobox_1.setItemText(2, _translate("optionWindow", "WARNING"))
        self.ow_combobox_1.setItemText(3, _translate("optionWindow", "CRITICAL"))
        self.ow_combobox_1.setItemText(4, _translate("optionWindow", "ERROR"))
        self.ow_label_2.setText(_translate("optionWindow", "Logging file folder:"))
        self.ow_checkbox_1.setText(_translate("optionWindow", "Check OrionFTP updates on GitHub"))
        self.ow_check_button.setText(_translate("optionWindow", "Check now"))
        self.ow_label_5.setText(_translate("optionWindow", "Default profile:"))
        self.ow_combobox_3.setItemText(0, _translate("optionWindow", "No default profile..."))
        self.ow_ok_button.setText(_translate("optionWindow", "Ok"))
        self.ow_cancel_button.setText(_translate("optionWindow", "Cancel"))

