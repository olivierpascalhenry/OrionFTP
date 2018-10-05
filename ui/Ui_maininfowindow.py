# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maininfowindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainInfoWindow(object):
    def setupUi(self, mainInfoWindow):
        mainInfoWindow.setObjectName("mainInfoWindow")
        mainInfoWindow.resize(991, 789)
        mainInfoWindow.setMinimumSize(QtCore.QSize(0, 0))
        mainInfoWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        mainInfoWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainInfoWindow.setWindowIcon(icon)
        mainInfoWindow.setStyleSheet("QWidget {\n"
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
        self.gridLayout_5 = QtWidgets.QGridLayout(mainInfoWindow)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.aiw_label_1 = QtWidgets.QLabel(mainInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_1.sizePolicy().hasHeightForWidth())
        self.aiw_label_1.setSizePolicy(sizePolicy)
        self.aiw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_1.setFont(font)
        self.aiw_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_1.setLineWidth(0)
        self.aiw_label_1.setMidLineWidth(0)
        self.aiw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.aiw_label_1.setWordWrap(True)
        self.aiw_label_1.setObjectName("aiw_label_1")
        self.gridLayout_5.addWidget(self.aiw_label_1, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.aiw_label_23 = QtWidgets.QLabel(mainInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_23.sizePolicy().hasHeightForWidth())
        self.aiw_label_23.setSizePolicy(sizePolicy)
        self.aiw_label_23.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_23.setFont(font)
        self.aiw_label_23.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"   background-color: rgb(250,250,250);\n"
"    padding: 10px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}")
        self.aiw_label_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_23.setLineWidth(0)
        self.aiw_label_23.setMidLineWidth(0)
        self.aiw_label_23.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.aiw_label_23.setWordWrap(True)
        self.aiw_label_23.setObjectName("aiw_label_23")
        self.horizontalLayout_6.addWidget(self.aiw_label_23)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.frame = QtWidgets.QFrame(mainInfoWindow)
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(250,250,250);\n"
"    border-top-left-radius: 0px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.aiw_label_10 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_10.sizePolicy().hasHeightForWidth())
        self.aiw_label_10.setSizePolicy(sizePolicy)
        self.aiw_label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_10.setFont(font)
        self.aiw_label_10.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_10.setLineWidth(0)
        self.aiw_label_10.setMidLineWidth(0)
        self.aiw_label_10.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_10.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_10.setWordWrap(True)
        self.aiw_label_10.setObjectName("aiw_label_10")
        self.gridLayout.addWidget(self.aiw_label_10, 3, 1, 1, 1)
        self.aiw_label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_3.sizePolicy().hasHeightForWidth())
        self.aiw_label_3.setSizePolicy(sizePolicy)
        self.aiw_label_3.setMinimumSize(QtCore.QSize(120, 27))
        self.aiw_label_3.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_3.setFont(font)
        self.aiw_label_3.setStyleSheet("QLabel {\n"
"    padding: 4px;\n"
"    color: rgb(45,45,45);\n"
"    background-color: rgb(200,200,200);\n"
"    border-radius: 0px;\n"
"}")
        self.aiw_label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_3.setLineWidth(0)
        self.aiw_label_3.setMidLineWidth(0)
        self.aiw_label_3.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_3.setWordWrap(True)
        self.aiw_label_3.setObjectName("aiw_label_3")
        self.gridLayout.addWidget(self.aiw_label_3, 1, 0, 1, 1)
        self.aiw_label_8 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_8.sizePolicy().hasHeightForWidth())
        self.aiw_label_8.setSizePolicy(sizePolicy)
        self.aiw_label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_8.setFont(font)
        self.aiw_label_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_8.setLineWidth(0)
        self.aiw_label_8.setMidLineWidth(0)
        self.aiw_label_8.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_8.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_8.setWordWrap(True)
        self.aiw_label_8.setObjectName("aiw_label_8")
        self.gridLayout.addWidget(self.aiw_label_8, 1, 1, 1, 1)
        self.aiw_label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_4.sizePolicy().hasHeightForWidth())
        self.aiw_label_4.setSizePolicy(sizePolicy)
        self.aiw_label_4.setMinimumSize(QtCore.QSize(120, 27))
        self.aiw_label_4.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_4.setFont(font)
        self.aiw_label_4.setStyleSheet("QLabel {\n"
"    padding: 4px;\n"
"    color: rgb(45,45,45);\n"
"    background-color: rgb(200,200,200);\n"
"    border-radius: 0px;\n"
"}")
        self.aiw_label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_4.setLineWidth(0)
        self.aiw_label_4.setMidLineWidth(0)
        self.aiw_label_4.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_4.setWordWrap(True)
        self.aiw_label_4.setObjectName("aiw_label_4")
        self.gridLayout.addWidget(self.aiw_label_4, 2, 0, 1, 1)
        self.aiw_label_9 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_9.sizePolicy().hasHeightForWidth())
        self.aiw_label_9.setSizePolicy(sizePolicy)
        self.aiw_label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_9.setFont(font)
        self.aiw_label_9.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_9.setLineWidth(0)
        self.aiw_label_9.setMidLineWidth(0)
        self.aiw_label_9.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_9.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_9.setWordWrap(True)
        self.aiw_label_9.setObjectName("aiw_label_9")
        self.gridLayout.addWidget(self.aiw_label_9, 2, 1, 1, 1)
        self.aiw_label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_5.sizePolicy().hasHeightForWidth())
        self.aiw_label_5.setSizePolicy(sizePolicy)
        self.aiw_label_5.setMinimumSize(QtCore.QSize(120, 27))
        self.aiw_label_5.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_5.setFont(font)
        self.aiw_label_5.setStyleSheet("QLabel {\n"
"    padding: 4px;\n"
"    color: rgb(45,45,45);\n"
"    background-color: rgb(200,200,200);\n"
"    border-radius: 0px;\n"
"}")
        self.aiw_label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_5.setLineWidth(0)
        self.aiw_label_5.setMidLineWidth(0)
        self.aiw_label_5.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_5.setWordWrap(True)
        self.aiw_label_5.setObjectName("aiw_label_5")
        self.gridLayout.addWidget(self.aiw_label_5, 3, 0, 1, 1)
        self.aiw_label_12 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_12.sizePolicy().hasHeightForWidth())
        self.aiw_label_12.setSizePolicy(sizePolicy)
        self.aiw_label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_12.setFont(font)
        self.aiw_label_12.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_12.setLineWidth(0)
        self.aiw_label_12.setMidLineWidth(0)
        self.aiw_label_12.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_12.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_12.setWordWrap(True)
        self.aiw_label_12.setObjectName("aiw_label_12")
        self.gridLayout.addWidget(self.aiw_label_12, 5, 1, 1, 1)
        self.aiw_connect_button = QtWidgets.QToolButton(self.frame)
        self.aiw_connect_button.setEnabled(False)
        self.aiw_connect_button.setMinimumSize(QtCore.QSize(100, 27))
        self.aiw_connect_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_connect_button.setFont(font)
        self.aiw_connect_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_connect_button.setObjectName("aiw_connect_button")
        self.gridLayout.addWidget(self.aiw_connect_button, 5, 0, 1, 1)
        self.aiw_label_13 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_13.sizePolicy().hasHeightForWidth())
        self.aiw_label_13.setSizePolicy(sizePolicy)
        self.aiw_label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_13.setFont(font)
        self.aiw_label_13.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_13.setLineWidth(0)
        self.aiw_label_13.setMidLineWidth(0)
        self.aiw_label_13.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_13.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_13.setWordWrap(True)
        self.aiw_label_13.setObjectName("aiw_label_13")
        self.gridLayout.addWidget(self.aiw_label_13, 6, 1, 1, 1)
        self.aiw_label_11 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_11.sizePolicy().hasHeightForWidth())
        self.aiw_label_11.setSizePolicy(sizePolicy)
        self.aiw_label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_11.setFont(font)
        self.aiw_label_11.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_11.setLineWidth(0)
        self.aiw_label_11.setMidLineWidth(0)
        self.aiw_label_11.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_11.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_11.setWordWrap(True)
        self.aiw_label_11.setObjectName("aiw_label_11")
        self.gridLayout.addWidget(self.aiw_label_11, 4, 1, 1, 1)
        self.aiw_download_button = QtWidgets.QToolButton(self.frame)
        self.aiw_download_button.setEnabled(False)
        self.aiw_download_button.setMinimumSize(QtCore.QSize(110, 27))
        self.aiw_download_button.setMaximumSize(QtCore.QSize(110, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_download_button.setFont(font)
        self.aiw_download_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_download_button.setObjectName("aiw_download_button")
        self.gridLayout.addWidget(self.aiw_download_button, 6, 0, 1, 1)
        self.aiw_label_6 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_6.sizePolicy().hasHeightForWidth())
        self.aiw_label_6.setSizePolicy(sizePolicy)
        self.aiw_label_6.setMinimumSize(QtCore.QSize(120, 27))
        self.aiw_label_6.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_6.setFont(font)
        self.aiw_label_6.setStyleSheet("QLabel {\n"
"    padding: 4px;\n"
"    color: rgb(45,45,45);\n"
"    background-color: rgb(200,200,200);\n"
"    border-radius: 0px;\n"
"}")
        self.aiw_label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_6.setLineWidth(0)
        self.aiw_label_6.setMidLineWidth(0)
        self.aiw_label_6.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_6.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_6.setWordWrap(True)
        self.aiw_label_6.setObjectName("aiw_label_6")
        self.gridLayout.addWidget(self.aiw_label_6, 4, 0, 1, 1)
        self.aiw_label_2 = QtWidgets.QLabel(self.frame)
        self.aiw_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.aiw_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        self.aiw_label_2.setFont(font)
        self.aiw_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.aiw_label_2.setObjectName("aiw_label_2")
        self.gridLayout.addWidget(self.aiw_label_2, 0, 0, 1, 1)
        self.aiw_label_7 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_7.sizePolicy().hasHeightForWidth())
        self.aiw_label_7.setSizePolicy(sizePolicy)
        self.aiw_label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_7.setFont(font)
        self.aiw_label_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_7.setLineWidth(0)
        self.aiw_label_7.setMidLineWidth(0)
        self.aiw_label_7.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_7.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_7.setWordWrap(True)
        self.aiw_label_7.setObjectName("aiw_label_7")
        self.gridLayout.addWidget(self.aiw_label_7, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem2, 3, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.aiw_label_14 = QtWidgets.QLabel(mainInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_14.sizePolicy().hasHeightForWidth())
        self.aiw_label_14.setSizePolicy(sizePolicy)
        self.aiw_label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_14.setFont(font)
        self.aiw_label_14.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"   background-color: rgb(250,250,250);\n"
"    padding: 10px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}")
        self.aiw_label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_14.setLineWidth(0)
        self.aiw_label_14.setMidLineWidth(0)
        self.aiw_label_14.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.aiw_label_14.setWordWrap(True)
        self.aiw_label_14.setObjectName("aiw_label_14")
        self.horizontalLayout_7.addWidget(self.aiw_label_14)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.frame_2 = QtWidgets.QFrame(mainInfoWindow)
        self.frame_2.setStyleSheet("QFrame {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(250,250,250);\n"
"    border-top-left-radius: 0px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.aiw_label_18 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_18.sizePolicy().hasHeightForWidth())
        self.aiw_label_18.setSizePolicy(sizePolicy)
        self.aiw_label_18.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_18.setFont(font)
        self.aiw_label_18.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_18.setLineWidth(0)
        self.aiw_label_18.setMidLineWidth(0)
        self.aiw_label_18.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_18.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_18.setWordWrap(True)
        self.aiw_label_18.setObjectName("aiw_label_18")
        self.gridLayout_3.addWidget(self.aiw_label_18, 3, 1, 1, 1)
        self.aiw_label_21 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_21.sizePolicy().hasHeightForWidth())
        self.aiw_label_21.setSizePolicy(sizePolicy)
        self.aiw_label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_21.setFont(font)
        self.aiw_label_21.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_21.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_21.setLineWidth(0)
        self.aiw_label_21.setMidLineWidth(0)
        self.aiw_label_21.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_21.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_21.setWordWrap(True)
        self.aiw_label_21.setObjectName("aiw_label_21")
        self.gridLayout_3.addWidget(self.aiw_label_21, 6, 1, 1, 1)
        self.aiw_label_15 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_15.sizePolicy().hasHeightForWidth())
        self.aiw_label_15.setSizePolicy(sizePolicy)
        self.aiw_label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_15.setFont(font)
        self.aiw_label_15.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_15.setLineWidth(0)
        self.aiw_label_15.setMidLineWidth(0)
        self.aiw_label_15.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_15.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_15.setWordWrap(True)
        self.aiw_label_15.setObjectName("aiw_label_15")
        self.gridLayout_3.addWidget(self.aiw_label_15, 0, 1, 1, 1)
        self.aiw_label_16 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_16.sizePolicy().hasHeightForWidth())
        self.aiw_label_16.setSizePolicy(sizePolicy)
        self.aiw_label_16.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_16.setFont(font)
        self.aiw_label_16.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_16.setLineWidth(0)
        self.aiw_label_16.setMidLineWidth(0)
        self.aiw_label_16.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_16.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_16.setWordWrap(True)
        self.aiw_label_16.setObjectName("aiw_label_16")
        self.gridLayout_3.addWidget(self.aiw_label_16, 1, 1, 1, 1)
        self.aiw_label_17 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_17.sizePolicy().hasHeightForWidth())
        self.aiw_label_17.setSizePolicy(sizePolicy)
        self.aiw_label_17.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_17.setFont(font)
        self.aiw_label_17.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_17.setLineWidth(0)
        self.aiw_label_17.setMidLineWidth(0)
        self.aiw_label_17.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_17.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_17.setWordWrap(True)
        self.aiw_label_17.setObjectName("aiw_label_17")
        self.gridLayout_3.addWidget(self.aiw_label_17, 2, 1, 1, 1)
        self.aiw_label_20 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_20.sizePolicy().hasHeightForWidth())
        self.aiw_label_20.setSizePolicy(sizePolicy)
        self.aiw_label_20.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_20.setFont(font)
        self.aiw_label_20.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_20.setLineWidth(0)
        self.aiw_label_20.setMidLineWidth(0)
        self.aiw_label_20.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_20.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_20.setWordWrap(True)
        self.aiw_label_20.setObjectName("aiw_label_20")
        self.gridLayout_3.addWidget(self.aiw_label_20, 5, 1, 1, 1)
        self.aiw_label_19 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_19.sizePolicy().hasHeightForWidth())
        self.aiw_label_19.setSizePolicy(sizePolicy)
        self.aiw_label_19.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_19.setFont(font)
        self.aiw_label_19.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_19.setLineWidth(0)
        self.aiw_label_19.setMidLineWidth(0)
        self.aiw_label_19.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_19.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_19.setWordWrap(True)
        self.aiw_label_19.setObjectName("aiw_label_19")
        self.gridLayout_3.addWidget(self.aiw_label_19, 4, 1, 1, 1)
        self.aiw_label_22 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_label_22.sizePolicy().hasHeightForWidth())
        self.aiw_label_22.setSizePolicy(sizePolicy)
        self.aiw_label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.aiw_label_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_label_22.setFont(font)
        self.aiw_label_22.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_label_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_label_22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_label_22.setLineWidth(0)
        self.aiw_label_22.setMidLineWidth(0)
        self.aiw_label_22.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_label_22.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_label_22.setWordWrap(True)
        self.aiw_label_22.setObjectName("aiw_label_22")
        self.gridLayout_3.addWidget(self.aiw_label_22, 7, 1, 1, 1)
        self.aiw_icon_5 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_icon_5.sizePolicy().hasHeightForWidth())
        self.aiw_icon_5.setSizePolicy(sizePolicy)
        self.aiw_icon_5.setMinimumSize(QtCore.QSize(27, 27))
        self.aiw_icon_5.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_icon_5.setFont(font)
        self.aiw_icon_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_icon_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_icon_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_icon_5.setLineWidth(0)
        self.aiw_icon_5.setMidLineWidth(0)
        self.aiw_icon_5.setText("")
        self.aiw_icon_5.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_icon_5.setPixmap(QtGui.QPixmap("icons/reload_icon.svg"))
        self.aiw_icon_5.setScaledContents(True)
        self.aiw_icon_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_icon_5.setWordWrap(True)
        self.aiw_icon_5.setObjectName("aiw_icon_5")
        self.gridLayout_3.addWidget(self.aiw_icon_5, 4, 0, 1, 1)
        self.aiw_icon_1 = QtWidgets.QLabel(self.frame_2)
        self.aiw_icon_1.setMinimumSize(QtCore.QSize(27, 27))
        self.aiw_icon_1.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        self.aiw_icon_1.setFont(font)
        self.aiw_icon_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_icon_1.setText("")
        self.aiw_icon_1.setPixmap(QtGui.QPixmap("icons/exit_icon.svg"))
        self.aiw_icon_1.setScaledContents(True)
        self.aiw_icon_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.aiw_icon_1.setObjectName("aiw_icon_1")
        self.gridLayout_3.addWidget(self.aiw_icon_1, 0, 0, 1, 1)
        self.aiw_icon_3 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_icon_3.sizePolicy().hasHeightForWidth())
        self.aiw_icon_3.setSizePolicy(sizePolicy)
        self.aiw_icon_3.setMinimumSize(QtCore.QSize(27, 27))
        self.aiw_icon_3.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_icon_3.setFont(font)
        self.aiw_icon_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_icon_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_icon_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_icon_3.setLineWidth(0)
        self.aiw_icon_3.setMidLineWidth(0)
        self.aiw_icon_3.setText("")
        self.aiw_icon_3.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_icon_3.setPixmap(QtGui.QPixmap("icons/off_icon.svg"))
        self.aiw_icon_3.setScaledContents(True)
        self.aiw_icon_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_icon_3.setWordWrap(True)
        self.aiw_icon_3.setObjectName("aiw_icon_3")
        self.gridLayout_3.addWidget(self.aiw_icon_3, 2, 0, 1, 1)
        self.aiw_icon_2 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_icon_2.sizePolicy().hasHeightForWidth())
        self.aiw_icon_2.setSizePolicy(sizePolicy)
        self.aiw_icon_2.setMinimumSize(QtCore.QSize(27, 27))
        self.aiw_icon_2.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_icon_2.setFont(font)
        self.aiw_icon_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_icon_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_icon_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_icon_2.setLineWidth(0)
        self.aiw_icon_2.setMidLineWidth(0)
        self.aiw_icon_2.setText("")
        self.aiw_icon_2.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_icon_2.setPixmap(QtGui.QPixmap("icons/manager_icon.svg"))
        self.aiw_icon_2.setScaledContents(True)
        self.aiw_icon_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_icon_2.setWordWrap(True)
        self.aiw_icon_2.setObjectName("aiw_icon_2")
        self.gridLayout_3.addWidget(self.aiw_icon_2, 1, 0, 1, 1)
        self.aiw_icon_4 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_icon_4.sizePolicy().hasHeightForWidth())
        self.aiw_icon_4.setSizePolicy(sizePolicy)
        self.aiw_icon_4.setMinimumSize(QtCore.QSize(27, 27))
        self.aiw_icon_4.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_icon_4.setFont(font)
        self.aiw_icon_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_icon_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_icon_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_icon_4.setLineWidth(0)
        self.aiw_icon_4.setMidLineWidth(0)
        self.aiw_icon_4.setText("")
        self.aiw_icon_4.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_icon_4.setPixmap(QtGui.QPixmap("icons/origin_icon.svg"))
        self.aiw_icon_4.setScaledContents(True)
        self.aiw_icon_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_icon_4.setWordWrap(True)
        self.aiw_icon_4.setObjectName("aiw_icon_4")
        self.gridLayout_3.addWidget(self.aiw_icon_4, 3, 0, 1, 1)
        self.aiw_icon_6 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_icon_6.sizePolicy().hasHeightForWidth())
        self.aiw_icon_6.setSizePolicy(sizePolicy)
        self.aiw_icon_6.setMinimumSize(QtCore.QSize(27, 27))
        self.aiw_icon_6.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_icon_6.setFont(font)
        self.aiw_icon_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_icon_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_icon_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_icon_6.setLineWidth(0)
        self.aiw_icon_6.setMidLineWidth(0)
        self.aiw_icon_6.setText("")
        self.aiw_icon_6.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_icon_6.setPixmap(QtGui.QPixmap("icons/option_icon.svg"))
        self.aiw_icon_6.setScaledContents(True)
        self.aiw_icon_6.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_icon_6.setWordWrap(True)
        self.aiw_icon_6.setObjectName("aiw_icon_6")
        self.gridLayout_3.addWidget(self.aiw_icon_6, 5, 0, 1, 1)
        self.aiw_icon_8 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_icon_8.sizePolicy().hasHeightForWidth())
        self.aiw_icon_8.setSizePolicy(sizePolicy)
        self.aiw_icon_8.setMinimumSize(QtCore.QSize(27, 27))
        self.aiw_icon_8.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_icon_8.setFont(font)
        self.aiw_icon_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_icon_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_icon_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_icon_8.setLineWidth(0)
        self.aiw_icon_8.setMidLineWidth(0)
        self.aiw_icon_8.setText("")
        self.aiw_icon_8.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_icon_8.setPixmap(QtGui.QPixmap("icons/orionftp_update_on.svg"))
        self.aiw_icon_8.setScaledContents(True)
        self.aiw_icon_8.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_icon_8.setWordWrap(True)
        self.aiw_icon_8.setObjectName("aiw_icon_8")
        self.gridLayout_3.addWidget(self.aiw_icon_8, 7, 0, 1, 1)
        self.aiw_icon_7 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aiw_icon_7.sizePolicy().hasHeightForWidth())
        self.aiw_icon_7.setSizePolicy(sizePolicy)
        self.aiw_icon_7.setMinimumSize(QtCore.QSize(27, 27))
        self.aiw_icon_7.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_icon_7.setFont(font)
        self.aiw_icon_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.aiw_icon_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aiw_icon_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aiw_icon_7.setLineWidth(0)
        self.aiw_icon_7.setMidLineWidth(0)
        self.aiw_icon_7.setText("")
        self.aiw_icon_7.setTextFormat(QtCore.Qt.AutoText)
        self.aiw_icon_7.setPixmap(QtGui.QPixmap("icons/about_popup_icon.svg"))
        self.aiw_icon_7.setScaledContents(True)
        self.aiw_icon_7.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.aiw_icon_7.setWordWrap(True)
        self.aiw_icon_7.setObjectName("aiw_icon_7")
        self.gridLayout_3.addWidget(self.aiw_icon_7, 6, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 4, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.aiw_ok_button = QtWidgets.QToolButton(mainInfoWindow)
        self.aiw_ok_button.setMinimumSize(QtCore.QSize(100, 27))
        self.aiw_ok_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aiw_ok_button.setFont(font)
        self.aiw_ok_button.setStyleSheet("QToolButton {\n"
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
        self.aiw_ok_button.setObjectName("aiw_ok_button")
        self.horizontalLayout_2.addWidget(self.aiw_ok_button)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 6, 0, 1, 3)

        self.retranslateUi(mainInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(mainInfoWindow)

    def retranslateUi(self, mainInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        mainInfoWindow.setWindowTitle(_translate("mainInfoWindow", "Information"))
        self.aiw_label_1.setText(_translate("mainInfoWindow", "<html><head/><body><p>The main window of OrionFTP. From here, the user interacts with its own computer and the (S)FTP server.</p></body></html>"))
        self.aiw_label_23.setText(_translate("mainInfoWindow", "Functions:"))
        self.aiw_label_10.setText(_translate("mainInfoWindow", "This section displays information about the connection to the selected (S)FTP server."))
        self.aiw_label_3.setText(_translate("mainInfoWindow", "Local"))
        self.aiw_label_8.setText(_translate("mainInfoWindow", "The local section, displaying path and folders/files on the local computer."))
        self.aiw_label_4.setText(_translate("mainInfoWindow", "Remote"))
        self.aiw_label_9.setText(_translate("mainInfoWindow", "The remote section, displaying path and folders/files on the remote (S)FTP server."))
        self.aiw_label_5.setText(_translate("mainInfoWindow", "FTP Connection"))
        self.aiw_label_12.setText(_translate("mainInfoWindow", "Click on this button, when an FTP profile is selected, to start the connexion to the (S)FTP server."))
        self.aiw_connect_button.setText(_translate("mainInfoWindow", "Connect"))
        self.aiw_label_13.setText(_translate("mainInfoWindow", "First select one or more files and/or one or more folders, then click on Download to start downloading."))
        self.aiw_label_11.setText(_translate("mainInfoWindow", "When a file/folder is downloaded, it will displayed here with the downloading progress."))
        self.aiw_download_button.setText(_translate("mainInfoWindow", "Download"))
        self.aiw_label_6.setText(_translate("mainInfoWindow", "Transfers"))
        self.aiw_label_2.setText(_translate("mainInfoWindow", "FTP profile:"))
        self.aiw_label_7.setText(_translate("mainInfoWindow", "This ComboBox lists all available FTP profiles. If a profile is set by default in the Option window, it will selected by default here."))
        self.aiw_label_14.setText(_translate("mainInfoWindow", "Icons:"))
        self.aiw_label_18.setText(_translate("mainInfoWindow", "When OrionFTP is connected to a (S)FTP server, click on this icon to go back to the default remote path."))
        self.aiw_label_21.setText(_translate("mainInfoWindow", "Here you will find information about OrionFTP."))
        self.aiw_label_15.setText(_translate("mainInfoWindow", "Click on this icon to exit OrionFTP."))
        self.aiw_label_16.setText(_translate("mainInfoWindow", "The OrionFTP FTP manager is accessible by clicking on this icon."))
        self.aiw_label_17.setText(_translate("mainInfoWindow", "When OrionFTP is connected to a (S)FTP server, click on this icon to close the connection."))
        self.aiw_label_20.setText(_translate("mainInfoWindow", "Options are accessible by clicking on this icon."))
        self.aiw_label_19.setText(_translate("mainInfoWindow", "When OrionFTP is connected to a (S)FTP server, click on this icon to refresh the remote folder displayed in the remote section."))
        self.aiw_label_22.setText(_translate("mainInfoWindow", "When a red ! is visible, an update is available for OrionFTP. In that case, click on this icon to start the update procedure."))
        self.aiw_ok_button.setText(_translate("mainInfoWindow", "Ok"))

