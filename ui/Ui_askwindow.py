# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'askwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_askWindow(object):
    def setupUi(self, askWindow):
        askWindow.setObjectName("askWindow")
        askWindow.resize(673, 306)
        askWindow.setMinimumSize(QtCore.QSize(0, 0))
        askWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        askWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/download_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        askWindow.setWindowIcon(icon)
        askWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(askWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.aw_label_1 = QtWidgets.QLabel(askWindow)
        self.aw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.aw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_1.setFont(font)
        self.aw_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aw_label_1.setLineWidth(0)
        self.aw_label_1.setMidLineWidth(0)
        self.aw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.aw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.aw_label_1.setWordWrap(True)
        self.aw_label_1.setObjectName("aw_label_1")
        self.gridLayout.addWidget(self.aw_label_1, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aw_label_2 = QtWidgets.QLabel(askWindow)
        self.aw_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_2.setFont(font)
        self.aw_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aw_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aw_label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aw_label_2.setLineWidth(0)
        self.aw_label_2.setMidLineWidth(0)
        self.aw_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.aw_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.aw_label_2.setWordWrap(True)
        self.aw_label_2.setObjectName("aw_label_2")
        self.horizontalLayout.addWidget(self.aw_label_2)
        self.aw_label_3 = QtWidgets.QLabel(askWindow)
        self.aw_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_3.setFont(font)
        self.aw_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aw_label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aw_label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aw_label_3.setLineWidth(0)
        self.aw_label_3.setMidLineWidth(0)
        self.aw_label_3.setTextFormat(QtCore.Qt.AutoText)
        self.aw_label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.aw_label_3.setWordWrap(True)
        self.aw_label_3.setObjectName("aw_label_3")
        self.horizontalLayout.addWidget(self.aw_label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.aw_radio_1 = QtWidgets.QRadioButton(askWindow)
        self.aw_radio_1.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_radio_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_radio_1.setFont(font)
        self.aw_radio_1.setStyleSheet("QRadioButton {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aw_radio_1.setObjectName("aw_radio_1")
        self.aw_group_1 = QtWidgets.QButtonGroup(askWindow)
        self.aw_group_1.setObjectName("aw_group_1")
        self.aw_group_1.addButton(self.aw_radio_1)
        self.verticalLayout.addWidget(self.aw_radio_1)
        self.aw_radio_2 = QtWidgets.QRadioButton(askWindow)
        self.aw_radio_2.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_radio_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_radio_2.setFont(font)
        self.aw_radio_2.setStyleSheet("QRadioButton {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aw_radio_2.setObjectName("aw_radio_2")
        self.aw_group_1.addButton(self.aw_radio_2)
        self.verticalLayout.addWidget(self.aw_radio_2)
        self.aw_radio_3 = QtWidgets.QRadioButton(askWindow)
        self.aw_radio_3.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_radio_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_radio_3.setFont(font)
        self.aw_radio_3.setStyleSheet("QRadioButton {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aw_radio_3.setObjectName("aw_radio_3")
        self.aw_group_1.addButton(self.aw_radio_3)
        self.verticalLayout.addWidget(self.aw_radio_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.aw_checkbox_1 = QtWidgets.QCheckBox(askWindow)
        self.aw_checkbox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.aw_checkbox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_checkbox_1.setFont(font)
        self.aw_checkbox_1.setStyleSheet("QCheckBox {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aw_checkbox_1.setObjectName("aw_checkbox_1")
        self.horizontalLayout_4.addWidget(self.aw_checkbox_1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.aw_button_1 = QtWidgets.QToolButton(askWindow)
        self.aw_button_1.setEnabled(False)
        self.aw_button_1.setMinimumSize(QtCore.QSize(100, 27))
        self.aw_button_1.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_button_1.setFont(font)
        self.aw_button_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #daecfc, stop: 1 #c4e0fc);\n"
"}")
        self.aw_button_1.setObjectName("aw_button_1")
        self.horizontalLayout_2.addWidget(self.aw_button_1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.retranslateUi(askWindow)
        QtCore.QMetaObject.connectSlotsByName(askWindow)

    def retranslateUi(self, askWindow):
        _translate = QtCore.QCoreApplication.translate
        askWindow.setWindowTitle(_translate("askWindow", "Download"))
        self.aw_label_1.setText(_translate("askWindow", "A file with the same name already exists in the local folder. What do you want to do with the remote file ?"))
        self.aw_label_2.setText(_translate("askWindow", "File:"))
        self.aw_label_3.setText(_translate("askWindow", "TMP"))
        self.aw_radio_1.setText(_translate("askWindow", "Download and overwrite the local file"))
        self.aw_radio_2.setText(_translate("askWindow", "Download and rename the downloaded file"))
        self.aw_radio_3.setText(_translate("askWindow", "Ignore and skip the download"))
        self.aw_checkbox_1.setText(_translate("askWindow", "Apply to all conficts ?"))
        self.aw_button_1.setText(_translate("askWindow", "Ok"))

