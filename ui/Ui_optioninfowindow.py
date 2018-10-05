# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optioninfowindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_optionInfoWindow(object):
    def setupUi(self, optionInfoWindow):
        optionInfoWindow.setObjectName("optionInfoWindow")
        optionInfoWindow.resize(1082, 626)
        optionInfoWindow.setMinimumSize(QtCore.QSize(0, 0))
        optionInfoWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        optionInfoWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        optionInfoWindow.setWindowIcon(icon)
        optionInfoWindow.setStyleSheet("QWidget {\n"
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
        self.gridLayout_3 = QtWidgets.QGridLayout(optionInfoWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.oiw_label_1 = QtWidgets.QLabel(optionInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_1.sizePolicy().hasHeightForWidth())
        self.oiw_label_1.setSizePolicy(sizePolicy)
        self.oiw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_1.setFont(font)
        self.oiw_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.oiw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_1.setLineWidth(0)
        self.oiw_label_1.setMidLineWidth(0)
        self.oiw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.oiw_label_1.setWordWrap(True)
        self.oiw_label_1.setObjectName("oiw_label_1")
        self.gridLayout_3.addWidget(self.oiw_label_1, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.oiw_label_8 = QtWidgets.QLabel(optionInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_8.sizePolicy().hasHeightForWidth())
        self.oiw_label_8.setSizePolicy(sizePolicy)
        self.oiw_label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_8.setFont(font)
        self.oiw_label_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"   background-color: rgb(250,250,250);\n"
"    padding: 10px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}")
        self.oiw_label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_8.setLineWidth(0)
        self.oiw_label_8.setMidLineWidth(0)
        self.oiw_label_8.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.oiw_label_8.setWordWrap(True)
        self.oiw_label_8.setObjectName("oiw_label_8")
        self.horizontalLayout_6.addWidget(self.oiw_label_8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.frame = QtWidgets.QFrame(optionInfoWindow)
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
        self.oiw_label_9 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_9.sizePolicy().hasHeightForWidth())
        self.oiw_label_9.setSizePolicy(sizePolicy)
        self.oiw_label_9.setMinimumSize(QtCore.QSize(100, 27))
        self.oiw_label_9.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_9.setFont(font)
        self.oiw_label_9.setStyleSheet("QLabel {\n"
"    padding: 4px;\n"
"    color: rgb(45,45,45);\n"
"    background-color: rgb(200,200,200);\n"
"    border-radius: 5px;\n"
"}")
        self.oiw_label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_9.setLineWidth(0)
        self.oiw_label_9.setMidLineWidth(0)
        self.oiw_label_9.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_9.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.oiw_label_9.setWordWrap(True)
        self.oiw_label_9.setObjectName("oiw_label_9")
        self.gridLayout.addWidget(self.oiw_label_9, 0, 0, 1, 1)
        self.oiw_label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_2.sizePolicy().hasHeightForWidth())
        self.oiw_label_2.setSizePolicy(sizePolicy)
        self.oiw_label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_2.setFont(font)
        self.oiw_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.oiw_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_2.setLineWidth(0)
        self.oiw_label_2.setMidLineWidth(0)
        self.oiw_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.oiw_label_2.setWordWrap(True)
        self.oiw_label_2.setObjectName("oiw_label_2")
        self.gridLayout.addWidget(self.oiw_label_2, 0, 1, 1, 1)
        self.oiw_label_10 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_10.sizePolicy().hasHeightForWidth())
        self.oiw_label_10.setSizePolicy(sizePolicy)
        self.oiw_label_10.setMinimumSize(QtCore.QSize(100, 27))
        self.oiw_label_10.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_10.setFont(font)
        self.oiw_label_10.setStyleSheet("QLabel {\n"
"    padding: 4px;\n"
"    color: rgb(45,45,45);\n"
"    background-color: rgb(200,200,200);\n"
"    border-radius: 5px;\n"
"}")
        self.oiw_label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_10.setLineWidth(0)
        self.oiw_label_10.setMidLineWidth(0)
        self.oiw_label_10.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_10.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.oiw_label_10.setWordWrap(True)
        self.oiw_label_10.setObjectName("oiw_label_10")
        self.gridLayout.addWidget(self.oiw_label_10, 1, 0, 1, 1)
        self.oiw_label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_3.sizePolicy().hasHeightForWidth())
        self.oiw_label_3.setSizePolicy(sizePolicy)
        self.oiw_label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_3.setFont(font)
        self.oiw_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.oiw_label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_3.setLineWidth(0)
        self.oiw_label_3.setMidLineWidth(0)
        self.oiw_label_3.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.oiw_label_3.setWordWrap(True)
        self.oiw_label_3.setObjectName("oiw_label_3")
        self.gridLayout.addWidget(self.oiw_label_3, 1, 1, 1, 1)
        self.oiw_label_11 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_11.sizePolicy().hasHeightForWidth())
        self.oiw_label_11.setSizePolicy(sizePolicy)
        self.oiw_label_11.setMinimumSize(QtCore.QSize(100, 27))
        self.oiw_label_11.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_11.setFont(font)
        self.oiw_label_11.setStyleSheet("QLabel {\n"
"    padding: 4px;\n"
"    color: rgb(45,45,45);\n"
"    background-color: rgb(200,200,200);\n"
"    border-radius: 5px;\n"
"}")
        self.oiw_label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_11.setLineWidth(0)
        self.oiw_label_11.setMidLineWidth(0)
        self.oiw_label_11.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_11.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.oiw_label_11.setWordWrap(True)
        self.oiw_label_11.setObjectName("oiw_label_11")
        self.gridLayout.addWidget(self.oiw_label_11, 2, 0, 1, 1)
        self.oiw_label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_4.sizePolicy().hasHeightForWidth())
        self.oiw_label_4.setSizePolicy(sizePolicy)
        self.oiw_label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_4.setFont(font)
        self.oiw_label_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.oiw_label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_4.setLineWidth(0)
        self.oiw_label_4.setMidLineWidth(0)
        self.oiw_label_4.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.oiw_label_4.setWordWrap(True)
        self.oiw_label_4.setObjectName("oiw_label_4")
        self.gridLayout.addWidget(self.oiw_label_4, 2, 1, 1, 1)
        self.oiw_label_12 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_12.sizePolicy().hasHeightForWidth())
        self.oiw_label_12.setSizePolicy(sizePolicy)
        self.oiw_label_12.setMinimumSize(QtCore.QSize(100, 27))
        self.oiw_label_12.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_12.setFont(font)
        self.oiw_label_12.setStyleSheet("QLabel {\n"
"    padding: 4px;\n"
"    color: rgb(45,45,45);\n"
"    background-color: rgb(200,200,200);\n"
"    border-radius: 5px;\n"
"}")
        self.oiw_label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_12.setLineWidth(0)
        self.oiw_label_12.setMidLineWidth(0)
        self.oiw_label_12.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_12.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.oiw_label_12.setWordWrap(True)
        self.oiw_label_12.setObjectName("oiw_label_12")
        self.gridLayout.addWidget(self.oiw_label_12, 3, 0, 1, 1)
        self.oiw_label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_5.sizePolicy().hasHeightForWidth())
        self.oiw_label_5.setSizePolicy(sizePolicy)
        self.oiw_label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_5.setFont(font)
        self.oiw_label_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.oiw_label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_5.setLineWidth(0)
        self.oiw_label_5.setMidLineWidth(0)
        self.oiw_label_5.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.oiw_label_5.setWordWrap(True)
        self.oiw_label_5.setObjectName("oiw_label_5")
        self.gridLayout.addWidget(self.oiw_label_5, 3, 1, 1, 1)
        self.oiw_ok_button = QtWidgets.QToolButton(self.frame)
        self.oiw_ok_button.setEnabled(False)
        self.oiw_ok_button.setMinimumSize(QtCore.QSize(100, 27))
        self.oiw_ok_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_ok_button.setFont(font)
        self.oiw_ok_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.oiw_ok_button.setObjectName("oiw_ok_button")
        self.gridLayout.addWidget(self.oiw_ok_button, 4, 0, 1, 1)
        self.oiw_label_6 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_6.sizePolicy().hasHeightForWidth())
        self.oiw_label_6.setSizePolicy(sizePolicy)
        self.oiw_label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_6.setFont(font)
        self.oiw_label_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.oiw_label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_6.setLineWidth(0)
        self.oiw_label_6.setMidLineWidth(0)
        self.oiw_label_6.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_6.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.oiw_label_6.setWordWrap(True)
        self.oiw_label_6.setObjectName("oiw_label_6")
        self.gridLayout.addWidget(self.oiw_label_6, 4, 1, 1, 1)
        self.oiw_cancel_button = QtWidgets.QToolButton(self.frame)
        self.oiw_cancel_button.setEnabled(False)
        self.oiw_cancel_button.setMinimumSize(QtCore.QSize(100, 27))
        self.oiw_cancel_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_cancel_button.setFont(font)
        self.oiw_cancel_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.oiw_cancel_button.setObjectName("oiw_cancel_button")
        self.gridLayout.addWidget(self.oiw_cancel_button, 5, 0, 1, 1)
        self.oiw_label_7 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_7.sizePolicy().hasHeightForWidth())
        self.oiw_label_7.setSizePolicy(sizePolicy)
        self.oiw_label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_7.setFont(font)
        self.oiw_label_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.oiw_label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_7.setLineWidth(0)
        self.oiw_label_7.setMidLineWidth(0)
        self.oiw_label_7.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_7.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.oiw_label_7.setWordWrap(True)
        self.oiw_label_7.setObjectName("oiw_label_7")
        self.gridLayout.addWidget(self.oiw_label_7, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.oiw_label_13 = QtWidgets.QLabel(optionInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_13.sizePolicy().hasHeightForWidth())
        self.oiw_label_13.setSizePolicy(sizePolicy)
        self.oiw_label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_13.setFont(font)
        self.oiw_label_13.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(240,240,255);\n"
"    padding: 10px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}")
        self.oiw_label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_13.setLineWidth(0)
        self.oiw_label_13.setMidLineWidth(0)
        self.oiw_label_13.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.oiw_label_13.setWordWrap(True)
        self.oiw_label_13.setObjectName("oiw_label_13")
        self.horizontalLayout_7.addWidget(self.oiw_label_13)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.miw_previous_button = QtWidgets.QToolButton(optionInfoWindow)
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
        self.oiw_label_14 = QtWidgets.QLabel(optionInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_14.sizePolicy().hasHeightForWidth())
        self.oiw_label_14.setSizePolicy(sizePolicy)
        self.oiw_label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_14.setFont(font)
        self.oiw_label_14.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.oiw_label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_14.setLineWidth(0)
        self.oiw_label_14.setMidLineWidth(0)
        self.oiw_label_14.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.oiw_label_14.setWordWrap(True)
        self.oiw_label_14.setObjectName("oiw_label_14")
        self.horizontalLayout_7.addWidget(self.oiw_label_14)
        self.miw_next_button = QtWidgets.QToolButton(optionInfoWindow)
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
        self.oiw_label_15 = QtWidgets.QLabel(optionInfoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiw_label_15.sizePolicy().hasHeightForWidth())
        self.oiw_label_15.setSizePolicy(sizePolicy)
        self.oiw_label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.oiw_label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_label_15.setFont(font)
        self.oiw_label_15.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(240,240,255);\n"
"    padding: 10px;\n"
"    border-top-left-radius: 0px;\n"
"}")
        self.oiw_label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oiw_label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oiw_label_15.setLineWidth(0)
        self.oiw_label_15.setMidLineWidth(0)
        self.oiw_label_15.setTextFormat(QtCore.Qt.AutoText)
        self.oiw_label_15.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.oiw_label_15.setWordWrap(True)
        self.oiw_label_15.setObjectName("oiw_label_15")
        self.verticalLayout.addWidget(self.oiw_label_15)
        self.gridLayout_3.addLayout(self.verticalLayout, 4, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.oiw_ok_button_2 = QtWidgets.QToolButton(optionInfoWindow)
        self.oiw_ok_button_2.setMinimumSize(QtCore.QSize(100, 27))
        self.oiw_ok_button_2.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.oiw_ok_button_2.setFont(font)
        self.oiw_ok_button_2.setStyleSheet("QToolButton {\n"
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
        self.oiw_ok_button_2.setObjectName("oiw_ok_button_2")
        self.horizontalLayout_2.addWidget(self.oiw_ok_button_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)

        self.retranslateUi(optionInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(optionInfoWindow)

    def retranslateUi(self, optionInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        optionInfoWindow.setWindowTitle(_translate("optionInfoWindow", "Information"))
        self.oiw_label_1.setText(_translate("optionInfoWindow", "<html><head/><body><p>In the Option window, the user will find options to control different aspects of OrionFTP. Options are divided in four sections: General, Interface, Connection and Transfer. For almost all options, it is not necessary to restart OrionFTP.</p></body></html>"))
        self.oiw_label_8.setText(_translate("optionInfoWindow", "Functions:"))
        self.oiw_label_9.setText(_translate("optionInfoWindow", "General"))
        self.oiw_label_2.setText(_translate("optionInfoWindow", "<html><head/><body><p>In this section, general options can be found to control the logging function (OrionFTP needs to be restarted if a different option is selected), the language, the update checking.</p></body></html>"))
        self.oiw_label_10.setText(_translate("optionInfoWindow", "Interface"))
        self.oiw_label_3.setText(_translate("optionInfoWindow", "<html><head/><body><p>All options controling the Graphical User Interface can be found here.</p></body></html>"))
        self.oiw_label_11.setText(_translate("optionInfoWindow", "Connection"))
        self.oiw_label_4.setText(_translate("optionInfoWindow", "<html><head/><body><p>It is possible, in the Connection section, to modify options controling the FTP/SFTP protocols.</p></body></html>"))
        self.oiw_label_12.setText(_translate("optionInfoWindow", "Transfer"))
        self.oiw_label_5.setText(_translate("optionInfoWindow", "<html><head/><body><p>In the Transfer section, options are available to control transfer operations.</p></body></html>"))
        self.oiw_ok_button.setText(_translate("optionInfoWindow", "Ok"))
        self.oiw_label_6.setText(_translate("optionInfoWindow", "<html><head/><body><p>The Ok button is here to confirm modifications brought to OrionFTP by the user, those options are then saved into the <span style=\" font-style:italic;\">orion_ftp.ini</span> file.</p></body></html>"))
        self.oiw_cancel_button.setText(_translate("optionInfoWindow", "Cancel"))
        self.oiw_label_7.setText(_translate("optionInfoWindow", "<html><head/><body><p>The Cancel button is here to cancel all selected options. No option is applied to OrionFTP in that case.</p></body></html>"))
        self.oiw_label_13.setText(_translate("optionInfoWindow", "General:"))
        self.oiw_label_14.setText(_translate("optionInfoWindow", "1/3"))
        self.oiw_label_15.setText(_translate("optionInfoWindow", "<html><head/><body><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ut elit sit amet risus facilisis mattis sit amet quis mi. Suspendisse et feugiat turpis. Nam faucibus, mi eget gravida euismod, mauris lorem pretium nunc, non aliquam ipsum erat sit amet orci. Fusce et vulputate purus. Etiam gravida nunc ut purus volutpat aliquet. Integer posuere porta justo gravida rhoncus. Mauris placerat sed neque at fringilla. Sed interdum posuere orci, pharetra hendrerit mi commodo in. Sed a auctor tellus, ut rhoncus ligula. Mauris eleifend scelerisque velit, quis vestibulum urna eleifend eget. Aliquam erat volutpat. Vivamus lacinia nunc in est interdum, nec varius arcu porttitor. Fusce ut suscipit lectus, at laoreet nibh. Duis turpis metus, sollicitudin sed lacus non, venenatis gravida massa.</p></body></html>"))
        self.oiw_ok_button_2.setText(_translate("optionInfoWindow", "Ok"))

