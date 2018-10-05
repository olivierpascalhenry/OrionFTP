# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerinfowindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_managerInfoWindow(object):
    def setupUi(self, managerInfoWindow):
        managerInfoWindow.setObjectName("managerInfoWindow")
        managerInfoWindow.resize(918, 633)
        managerInfoWindow.setMinimumSize(QtCore.QSize(0, 0))
        managerInfoWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        managerInfoWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        managerInfoWindow.setWindowIcon(icon)
        managerInfoWindow.setStyleSheet("QWidget {\n"
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
        self.gridLayout_3 = QtWidgets.QGridLayout(managerInfoWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.miw_label_1 = QtWidgets.QLabel(managerInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_1.sizePolicy().hasHeightForWidth())
        self.miw_label_1.setSizePolicy(sizePolicy)
        self.miw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_1.setFont(font)
        self.miw_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.miw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_1.setLineWidth(0)
        self.miw_label_1.setMidLineWidth(0)
        self.miw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.miw_label_1.setWordWrap(True)
        self.miw_label_1.setObjectName("miw_label_1")
        self.gridLayout_3.addWidget(self.miw_label_1, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.miw_label_11 = QtWidgets.QLabel(managerInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_11.sizePolicy().hasHeightForWidth())
        self.miw_label_11.setSizePolicy(sizePolicy)
        self.miw_label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_11.setFont(font)
        self.miw_label_11.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"   background-color: rgb(250,250,250);\n"
"    padding: 10px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}")
        self.miw_label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_11.setLineWidth(0)
        self.miw_label_11.setMidLineWidth(0)
        self.miw_label_11.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.miw_label_11.setWordWrap(True)
        self.miw_label_11.setObjectName("miw_label_11")
        self.horizontalLayout_6.addWidget(self.miw_label_11)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.frame = QtWidgets.QFrame(managerInfoWindow)
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(250,250,250);\n"
"    border-top-left-radius: 0px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.miw_icon_1 = QtWidgets.QLabel(self.frame)
        self.miw_icon_1.setMinimumSize(QtCore.QSize(23, 23))
        self.miw_icon_1.setMaximumSize(QtCore.QSize(23, 23))
        self.miw_icon_1.setText("")
        self.miw_icon_1.setPixmap(QtGui.QPixmap("icons/plus_icon.svg"))
        self.miw_icon_1.setScaledContents(True)
        self.miw_icon_1.setObjectName("miw_icon_1")
        self.horizontalLayout.addWidget(self.miw_icon_1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.miw_label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_2.sizePolicy().hasHeightForWidth())
        self.miw_label_2.setSizePolicy(sizePolicy)
        self.miw_label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_2.setFont(font)
        self.miw_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.miw_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_2.setLineWidth(0)
        self.miw_label_2.setMidLineWidth(0)
        self.miw_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.miw_label_2.setWordWrap(True)
        self.miw_label_2.setObjectName("miw_label_2")
        self.gridLayout_2.addWidget(self.miw_label_2, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.miw_icon_2 = QtWidgets.QLabel(self.frame)
        self.miw_icon_2.setMinimumSize(QtCore.QSize(23, 23))
        self.miw_icon_2.setMaximumSize(QtCore.QSize(23, 23))
        self.miw_icon_2.setText("")
        self.miw_icon_2.setPixmap(QtGui.QPixmap("icons/del_tick_icon.svg"))
        self.miw_icon_2.setScaledContents(True)
        self.miw_icon_2.setObjectName("miw_icon_2")
        self.horizontalLayout_3.addWidget(self.miw_icon_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.miw_label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_3.sizePolicy().hasHeightForWidth())
        self.miw_label_3.setSizePolicy(sizePolicy)
        self.miw_label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_3.setFont(font)
        self.miw_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.miw_label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_3.setLineWidth(0)
        self.miw_label_3.setMidLineWidth(0)
        self.miw_label_3.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.miw_label_3.setWordWrap(True)
        self.miw_label_3.setObjectName("miw_label_3")
        self.gridLayout_2.addWidget(self.miw_label_3, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.miw_icon_3 = QtWidgets.QLabel(self.frame)
        self.miw_icon_3.setMinimumSize(QtCore.QSize(23, 23))
        self.miw_icon_3.setMaximumSize(QtCore.QSize(23, 23))
        self.miw_icon_3.setText("")
        self.miw_icon_3.setPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"))
        self.miw_icon_3.setScaledContents(True)
        self.miw_icon_3.setObjectName("miw_icon_3")
        self.horizontalLayout_4.addWidget(self.miw_icon_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.miw_label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_4.sizePolicy().hasHeightForWidth())
        self.miw_label_4.setSizePolicy(sizePolicy)
        self.miw_label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_4.setFont(font)
        self.miw_label_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.miw_label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_4.setLineWidth(0)
        self.miw_label_4.setMidLineWidth(0)
        self.miw_label_4.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.miw_label_4.setWordWrap(True)
        self.miw_label_4.setObjectName("miw_label_4")
        self.gridLayout_2.addWidget(self.miw_label_4, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.miw_icon_4 = QtWidgets.QLabel(self.frame)
        self.miw_icon_4.setMinimumSize(QtCore.QSize(23, 23))
        self.miw_icon_4.setMaximumSize(QtCore.QSize(23, 23))
        self.miw_icon_4.setText("")
        self.miw_icon_4.setPixmap(QtGui.QPixmap("icons/save_icon.svg"))
        self.miw_icon_4.setScaledContents(True)
        self.miw_icon_4.setObjectName("miw_icon_4")
        self.horizontalLayout_5.addWidget(self.miw_icon_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.miw_label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_5.sizePolicy().hasHeightForWidth())
        self.miw_label_5.setSizePolicy(sizePolicy)
        self.miw_label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_5.setFont(font)
        self.miw_label_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.miw_label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_5.setLineWidth(0)
        self.miw_label_5.setMidLineWidth(0)
        self.miw_label_5.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.miw_label_5.setWordWrap(True)
        self.miw_label_5.setObjectName("miw_label_5")
        self.gridLayout_2.addWidget(self.miw_label_5, 3, 1, 1, 1)
        self.miw_ok_button = QtWidgets.QToolButton(self.frame)
        self.miw_ok_button.setEnabled(False)
        self.miw_ok_button.setMinimumSize(QtCore.QSize(100, 27))
        self.miw_ok_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_ok_button.setFont(font)
        self.miw_ok_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.miw_ok_button.setObjectName("miw_ok_button")
        self.gridLayout_2.addWidget(self.miw_ok_button, 4, 0, 1, 1)
        self.miw_label_6 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_6.sizePolicy().hasHeightForWidth())
        self.miw_label_6.setSizePolicy(sizePolicy)
        self.miw_label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_6.setFont(font)
        self.miw_label_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.miw_label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_6.setLineWidth(0)
        self.miw_label_6.setMidLineWidth(0)
        self.miw_label_6.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_6.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.miw_label_6.setWordWrap(True)
        self.miw_label_6.setObjectName("miw_label_6")
        self.gridLayout_2.addWidget(self.miw_label_6, 4, 1, 1, 1)
        self.miw_cancel_button = QtWidgets.QToolButton(self.frame)
        self.miw_cancel_button.setEnabled(False)
        self.miw_cancel_button.setMinimumSize(QtCore.QSize(100, 27))
        self.miw_cancel_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_cancel_button.setFont(font)
        self.miw_cancel_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.miw_cancel_button.setObjectName("miw_cancel_button")
        self.gridLayout_2.addWidget(self.miw_cancel_button, 5, 0, 1, 1)
        self.miw_label_7 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_7.sizePolicy().hasHeightForWidth())
        self.miw_label_7.setSizePolicy(sizePolicy)
        self.miw_label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_7.setFont(font)
        self.miw_label_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.miw_label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_7.setLineWidth(0)
        self.miw_label_7.setMidLineWidth(0)
        self.miw_label_7.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_7.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.miw_label_7.setWordWrap(True)
        self.miw_label_7.setObjectName("miw_label_7")
        self.gridLayout_2.addWidget(self.miw_label_7, 5, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem6, 3, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.miw_label_9 = QtWidgets.QLabel(managerInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_9.sizePolicy().hasHeightForWidth())
        self.miw_label_9.setSizePolicy(sizePolicy)
        self.miw_label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_9.setFont(font)
        self.miw_label_9.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(240,240,255);\n"
"    padding: 10px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}")
        self.miw_label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_9.setLineWidth(0)
        self.miw_label_9.setMidLineWidth(0)
        self.miw_label_9.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.miw_label_9.setWordWrap(True)
        self.miw_label_9.setObjectName("miw_label_9")
        self.horizontalLayout_7.addWidget(self.miw_label_9)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.miw_previous_button = QtWidgets.QToolButton(managerInfoWindow)
        self.miw_previous_button.setMinimumSize(QtCore.QSize(27, 27))
        self.miw_previous_button.setMaximumSize(QtCore.QSize(24, 24))
        self.miw_previous_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/left_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.miw_previous_button.setIcon(icon1)
        self.miw_previous_button.setIconSize(QtCore.QSize(20, 20))
        self.miw_previous_button.setObjectName("miw_previous_button")
        self.horizontalLayout_7.addWidget(self.miw_previous_button)
        self.miw_label_10 = QtWidgets.QLabel(managerInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_10.sizePolicy().hasHeightForWidth())
        self.miw_label_10.setSizePolicy(sizePolicy)
        self.miw_label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_10.setFont(font)
        self.miw_label_10.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.miw_label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_10.setLineWidth(0)
        self.miw_label_10.setMidLineWidth(0)
        self.miw_label_10.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.miw_label_10.setWordWrap(True)
        self.miw_label_10.setObjectName("miw_label_10")
        self.horizontalLayout_7.addWidget(self.miw_label_10)
        self.miw_next_button = QtWidgets.QToolButton(managerInfoWindow)
        self.miw_next_button.setMinimumSize(QtCore.QSize(24, 24))
        self.miw_next_button.setMaximumSize(QtCore.QSize(24, 24))
        self.miw_next_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/right_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.miw_next_button.setIcon(icon2)
        self.miw_next_button.setIconSize(QtCore.QSize(20, 20))
        self.miw_next_button.setObjectName("miw_next_button")
        self.horizontalLayout_7.addWidget(self.miw_next_button)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.miw_label_8 = QtWidgets.QLabel(managerInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miw_label_8.sizePolicy().hasHeightForWidth())
        self.miw_label_8.setSizePolicy(sizePolicy)
        self.miw_label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.miw_label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_label_8.setFont(font)
        self.miw_label_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(240,240,255);\n"
"    padding: 10px;\n"
"    border-top-left-radius: 0px;\n"
"}")
        self.miw_label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.miw_label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.miw_label_8.setLineWidth(0)
        self.miw_label_8.setMidLineWidth(0)
        self.miw_label_8.setTextFormat(QtCore.Qt.AutoText)
        self.miw_label_8.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.miw_label_8.setWordWrap(True)
        self.miw_label_8.setObjectName("miw_label_8")
        self.verticalLayout.addWidget(self.miw_label_8)
        self.gridLayout_3.addLayout(self.verticalLayout, 4, 0, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.miw_ok_button_2 = QtWidgets.QToolButton(managerInfoWindow)
        self.miw_ok_button_2.setMinimumSize(QtCore.QSize(100, 27))
        self.miw_ok_button_2.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.miw_ok_button_2.setFont(font)
        self.miw_ok_button_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45)\n"
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
        self.miw_ok_button_2.setObjectName("miw_ok_button_2")
        self.horizontalLayout_2.addWidget(self.miw_ok_button_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)

        self.retranslateUi(managerInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(managerInfoWindow)

    def retranslateUi(self, managerInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        managerInfoWindow.setWindowTitle(_translate("managerInfoWindow", "Information"))
        self.miw_label_1.setText(_translate("managerInfoWindow", "<html><head/><body><p>The FTP profile manager allows the user to create, edit and delete FTP profiles, and to save and load an FTP profile list. Here is a brief description of all available functions.</p></body></html>"))
        self.miw_label_11.setText(_translate("managerInfoWindow", "Functions:"))
        self.miw_label_2.setText(_translate("managerInfoWindow", "<html><head/><body><p>Click on this button to create a new FTP profile.</p></body></html>"))
        self.miw_label_3.setText(_translate("managerInfoWindow", "<html><head/><body><p>Click on this button to delete an existing FTP profile. The button is enabled when at least one profile exists in the profile list and when a profile has been selected.</p></body></html>"))
        self.miw_label_4.setText(_translate("managerInfoWindow", "<html><head/><body><p>Click on this button to load an xml file containing a list of FTP profiles created in the OrionFTP FTP manager.</p></body></html>"))
        self.miw_label_5.setText(_translate("managerInfoWindow", "<html><head/><body><p>Click on this button to save the list of FTP profiles in an xml file.</p></body></html>"))
        self.miw_ok_button.setText(_translate("managerInfoWindow", "Ok"))
        self.miw_label_6.setText(_translate("managerInfoWindow", "<html><head/><body><p>The Ok button is here to confirm modifications brought to the FTP profile list by the user, it will then create an xml file containing all FTP profiles, replacing the old one.</p></body></html>"))
        self.miw_cancel_button.setText(_translate("managerInfoWindow", "Cancel"))
        self.miw_label_7.setText(_translate("managerInfoWindow", "<html><head/><body><p>The Cancel button is here to cancel modifications brought to the FTP profile list.</p></body></html>"))
        self.miw_label_9.setText(_translate("managerInfoWindow", "Important:"))
        self.miw_label_10.setText(_translate("managerInfoWindow", "1/3"))
        self.miw_label_8.setText(_translate("managerInfoWindow", "<html><head/><body><p>When creating a new FTP profile, all fields must be filled to allow a proper operation of the FTP library. An empty field, or a wrong host/port/username/password can lead to a failure during the connection.</p><p>It is possible to modify an FTP profile when OrionFTP is connected to the related host. In that case, modifications will be taken into account at the next connection.</p></body></html>"))
        self.miw_ok_button_2.setText(_translate("managerInfoWindow", "Ok"))

