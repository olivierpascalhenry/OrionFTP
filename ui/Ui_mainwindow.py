# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 775)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/orionftp_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.main_profile_lb = QtWidgets.QLabel(self.centralwidget)
        self.main_profile_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.main_profile_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.main_profile_lb.setFont(font)
        self.main_profile_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.main_profile_lb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_profile_lb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_profile_lb.setObjectName("main_profile_lb")
        self.horizontalLayout.addWidget(self.main_profile_lb)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.main_profile_cb = QtWidgets.QComboBox(self.centralwidget)
        self.main_profile_cb.setMinimumSize(QtCore.QSize(300, 27))
        self.main_profile_cb.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_profile_cb.setFont(font)
        self.main_profile_cb.setStyleSheet("QComboBox {\n"
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
        self.main_profile_cb.setObjectName("main_profile_cb")
        self.main_profile_cb.addItem("")
        self.horizontalLayout.addWidget(self.main_profile_cb)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.main_connect_bt = QtWidgets.QToolButton(self.centralwidget)
        self.main_connect_bt.setEnabled(False)
        self.main_connect_bt.setMinimumSize(QtCore.QSize(100, 27))
        self.main_connect_bt.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_connect_bt.setFont(font)
        self.main_connect_bt.setStyleSheet("QToolButton {\n"
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
        self.main_connect_bt.setObjectName("main_connect_bt")
        self.horizontalLayout.addWidget(self.main_connect_bt)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.info_button_1 = QtWidgets.QToolButton(self.centralwidget)
        self.info_button_1.setMinimumSize(QtCore.QSize(27, 27))
        self.info_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_1.setStyleSheet("QToolButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_button_1.setIcon(icon1)
        self.info_button_1.setIconSize(QtCore.QSize(23, 23))
        self.info_button_1.setObjectName("info_button_1")
        self.horizontalLayout.addWidget(self.info_button_1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.main_splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.main_splitter_3.setStyleSheet("QSplitter::handle {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"    background: transparent;\n"
"}")
        self.main_splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter_3.setObjectName("main_splitter_3")
        self.layoutWidget = QtWidgets.QWidget(self.main_splitter_3)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.action_quit_bt = QtWidgets.QToolButton(self.layoutWidget)
        self.action_quit_bt.setMinimumSize(QtCore.QSize(37, 37))
        self.action_quit_bt.setMaximumSize(QtCore.QSize(37, 37))
        self.action_quit_bt.setStyleSheet("QToolButton {\n"
"   background-color: transparent;\n"
"   border: 0px solid black;\n"
"}")
        self.action_quit_bt.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_quit_bt.setIcon(icon2)
        self.action_quit_bt.setIconSize(QtCore.QSize(35, 35))
        self.action_quit_bt.setObjectName("action_quit_bt")
        self.horizontalLayout_7.addWidget(self.action_quit_bt)
        self.action_option_bt = QtWidgets.QToolButton(self.layoutWidget)
        self.action_option_bt.setMinimumSize(QtCore.QSize(37, 37))
        self.action_option_bt.setMaximumSize(QtCore.QSize(37, 37))
        self.action_option_bt.setStyleSheet("QToolButton {\n"
"   background-color: transparent;\n"
"   border: 0px solid black;\n"
"}")
        self.action_option_bt.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_option_bt.setIcon(icon3)
        self.action_option_bt.setIconSize(QtCore.QSize(35, 35))
        self.action_option_bt.setObjectName("action_option_bt")
        self.horizontalLayout_7.addWidget(self.action_option_bt)
        self.action_about_bt = QtWidgets.QToolButton(self.layoutWidget)
        self.action_about_bt.setMinimumSize(QtCore.QSize(37, 37))
        self.action_about_bt.setMaximumSize(QtCore.QSize(37, 37))
        self.action_about_bt.setStyleSheet("QToolButton {\n"
"   background-color: transparent;\n"
"   border: 0px solid black;\n"
"}")
        self.action_about_bt.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/about_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about_bt.setIcon(icon4)
        self.action_about_bt.setIconSize(QtCore.QSize(35, 35))
        self.action_about_bt.setObjectName("action_about_bt")
        self.horizontalLayout_7.addWidget(self.action_about_bt)
        self.action_update_bt = QtWidgets.QToolButton(self.layoutWidget)
        self.action_update_bt.setEnabled(False)
        self.action_update_bt.setMinimumSize(QtCore.QSize(37, 37))
        self.action_update_bt.setMaximumSize(QtCore.QSize(37, 37))
        self.action_update_bt.setStyleSheet("QToolButton {\n"
"   background-color: transparent;\n"
"   border: 0px solid black;\n"
"}")
        self.action_update_bt.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/orionftp_update_off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_update_bt.setIcon(icon5)
        self.action_update_bt.setIconSize(QtCore.QSize(35, 35))
        self.action_update_bt.setObjectName("action_update_bt")
        self.horizontalLayout_7.addWidget(self.action_update_bt)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.main_upload_bt = QtWidgets.QToolButton(self.layoutWidget)
        self.main_upload_bt.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(112)
        sizePolicy.setVerticalStretch(27)
        sizePolicy.setHeightForWidth(self.main_upload_bt.sizePolicy().hasHeightForWidth())
        self.main_upload_bt.setSizePolicy(sizePolicy)
        self.main_upload_bt.setMinimumSize(QtCore.QSize(110, 27))
        self.main_upload_bt.setMaximumSize(QtCore.QSize(110, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_upload_bt.setFont(font)
        self.main_upload_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-right-top-radius: 1px;\n"
"    border-right-bottom-radius: 1px;\n"
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
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #daecfc, stop: 1 #c4e0fc);\n"
"}")
        self.main_upload_bt.setObjectName("main_upload_bt")
        self.horizontalLayout_6.addWidget(self.main_upload_bt)
        self.main_upload_bt_2 = QtWidgets.QToolButton(self.layoutWidget)
        self.main_upload_bt_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(112)
        sizePolicy.setVerticalStretch(27)
        sizePolicy.setHeightForWidth(self.main_upload_bt_2.sizePolicy().hasHeightForWidth())
        self.main_upload_bt_2.setSizePolicy(sizePolicy)
        self.main_upload_bt_2.setMinimumSize(QtCore.QSize(27, 27))
        self.main_upload_bt_2.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_upload_bt_2.setFont(font)
        self.main_upload_bt_2.setStyleSheet("QToolButton {\n"
"    border-top: 0px solid #acacac;\n"
"    border-bottom: 0px solid #acacac;\n"
"    border-right: 0px solid #acacac;\n"
"    border-right-top-radius: 1px;\n"
"    border-right-bottom-radius: 1px;\n"
"    background-color: transparent;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"\n"
"}")
        self.main_upload_bt_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/send_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_upload_bt_2.setIcon(icon6)
        self.main_upload_bt_2.setObjectName("main_upload_bt_2")
        self.horizontalLayout_6.addWidget(self.main_upload_bt_2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.layoutWidget1 = QtWidgets.QWidget(self.main_splitter_3)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.main_download_bt_2 = QtWidgets.QToolButton(self.layoutWidget1)
        self.main_download_bt_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(112)
        sizePolicy.setVerticalStretch(27)
        sizePolicy.setHeightForWidth(self.main_download_bt_2.sizePolicy().hasHeightForWidth())
        self.main_download_bt_2.setSizePolicy(sizePolicy)
        self.main_download_bt_2.setMinimumSize(QtCore.QSize(27, 27))
        self.main_download_bt_2.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_download_bt_2.setFont(font)
        self.main_download_bt_2.setStyleSheet("QToolButton {\n"
"    border-top: 0px solid #acacac;\n"
"    border-bottom: 0px solid #acacac;\n"
"    border-left: 0px solid #acacac;\n"
"    border-left-top-radius: 1px;\n"
"    border-left-bottom-radius: 1px;\n"
"    background-color: transparent;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed {\n"
"}")
        self.main_download_bt_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/receive_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_download_bt_2.setIcon(icon7)
        self.main_download_bt_2.setObjectName("main_download_bt_2")
        self.horizontalLayout_4.addWidget(self.main_download_bt_2)
        self.main_download_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.main_download_bt.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(112)
        sizePolicy.setVerticalStretch(27)
        sizePolicy.setHeightForWidth(self.main_download_bt.sizePolicy().hasHeightForWidth())
        self.main_download_bt.setSizePolicy(sizePolicy)
        self.main_download_bt.setMinimumSize(QtCore.QSize(110, 27))
        self.main_download_bt.setMaximumSize(QtCore.QSize(110, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_download_bt.setFont(font)
        self.main_download_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-right-top-radius: 1px;\n"
"    border-right-bottom-radius: 1px;\n"
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
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #daecfc, stop: 1 #c4e0fc);\n"
"}")
        self.main_download_bt.setObjectName("main_download_bt")
        self.horizontalLayout_4.addWidget(self.main_download_bt)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.action_refresh_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.action_refresh_bt.setEnabled(False)
        self.action_refresh_bt.setMinimumSize(QtCore.QSize(37, 37))
        self.action_refresh_bt.setMaximumSize(QtCore.QSize(37, 37))
        self.action_refresh_bt.setStyleSheet("QToolButton {\n"
"   background-color: transparent;\n"
"   border: 0px solid black;\n"
"}")
        self.action_refresh_bt.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/reload_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_refresh_bt.setIcon(icon8)
        self.action_refresh_bt.setIconSize(QtCore.QSize(35, 35))
        self.action_refresh_bt.setObjectName("action_refresh_bt")
        self.horizontalLayout_5.addWidget(self.action_refresh_bt)
        self.action_close_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.action_close_bt.setEnabled(False)
        self.action_close_bt.setMinimumSize(QtCore.QSize(37, 37))
        self.action_close_bt.setMaximumSize(QtCore.QSize(37, 37))
        self.action_close_bt.setStyleSheet("QToolButton {\n"
"   background-color: transparent;\n"
"   border: 0px solid black;\n"
"}")
        self.action_close_bt.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/off_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_close_bt.setIcon(icon9)
        self.action_close_bt.setIconSize(QtCore.QSize(35, 35))
        self.action_close_bt.setObjectName("action_close_bt")
        self.horizontalLayout_5.addWidget(self.action_close_bt)
        self.action_manager_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.action_manager_bt.setEnabled(True)
        self.action_manager_bt.setMinimumSize(QtCore.QSize(37, 37))
        self.action_manager_bt.setMaximumSize(QtCore.QSize(37, 37))
        self.action_manager_bt.setStyleSheet("QToolButton {\n"
"   background-color: transparent;\n"
"   border: 0px solid black;\n"
"}")
        self.action_manager_bt.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/manager_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_manager_bt.setIcon(icon10)
        self.action_manager_bt.setIconSize(QtCore.QSize(35, 35))
        self.action_manager_bt.setObjectName("action_manager_bt")
        self.horizontalLayout_5.addWidget(self.action_manager_bt)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.gridLayout.addWidget(self.main_splitter_3, 1, 0, 1, 1)
        self.main_splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.main_splitter_2.setStyleSheet("QSplitter::handle {\n"
"    background: rgb(220,220,220);\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"    background: rgb(190,190,190);\n"
"}\n"
"")
        self.main_splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.main_splitter_2.setObjectName("main_splitter_2")
        self.main_frame = QtWidgets.QFrame(self.main_splitter_2)
        self.main_frame.setStyleSheet("QFrame {\n"
"    background: rgb(220,220,220);\n"
"    margin-bottom: 5px;\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.main_frame)
        self.gridLayout_3.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.main_splitter_1 = QtWidgets.QSplitter(self.main_frame)
        self.main_splitter_1.setStyleSheet("QSplitter::handle {\n"
"    background: rgb(220,220,220);\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"    background: rgb(190,190,190);\n"
"}\n"
"")
        self.main_splitter_1.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter_1.setObjectName("main_splitter_1")
        self.layoutWidget2 = QtWidgets.QWidget(self.main_splitter_1)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_local_lb = QtWidgets.QLabel(self.layoutWidget2)
        self.main_local_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.main_local_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.main_local_lb.setFont(font)
        self.main_local_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    padding-bottom: -2px;\n"
"}")
        self.main_local_lb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_local_lb.setObjectName("main_local_lb")
        self.horizontalLayout_2.addWidget(self.main_local_lb)
        self.main_local_ln = QtWidgets.QLineEdit(self.layoutWidget2)
        self.main_local_ln.setEnabled(True)
        self.main_local_ln.setMinimumSize(QtCore.QSize(0, 27))
        self.main_local_ln.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.main_local_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_local_ln.setFont(font)
        self.main_local_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: rgb(200,200,200);\n"
"}")
        self.main_local_ln.setText("")
        self.main_local_ln.setFrame(False)
        self.main_local_ln.setReadOnly(True)
        self.main_local_ln.setObjectName("main_local_ln")
        self.horizontalLayout_2.addWidget(self.main_local_ln)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem14)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.main_local_sp = QtWidgets.QSplitter(self.layoutWidget2)
        self.main_local_sp.setStyleSheet("QSplitter::handle {\n"
"    background: rgb(220,220,220);\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"    background: rgb(190,190,190);\n"
"}")
        self.main_local_sp.setOrientation(QtCore.Qt.Vertical)
        self.main_local_sp.setObjectName("main_local_sp")
        self.main_local_tr_1 = QtWidgets.QTreeView(self.main_local_sp)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_local_tr_1.setFont(font)
        self.main_local_tr_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_local_tr_1.setStyleSheet("QTreeView {\n"
"    background: rgb(240,240,240);\n"
"    color: rgb(45,45,45);\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTreeView:disabled {\n"
"    color: rgb(90,90,90);\n"
"    selection-color: rgb(90,90,90);\n"
"    selection-background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #eaeaea, stop:1 #dcdcdc);\n"
"}\n"
"\n"
"QTreeView::item: {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    padding-right: 1px;\n"
"    margin-right: 2px;\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    padding-left: 1px;\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(253,253,253);\n"
"    color: rgb(45,45,45);\n"
"    border-top: 1px solid lightgray;\n"
"    border-bottom: 1px solid lightgray;\n"
"    border-right: 1px solid lightgray;\n"
"    padding-left: 10px;\n"
"    padding-bottom: 3px;\n"
"    height: 30px;\n"
"    font-family: \"fonts/SourceSansPro-Regular.ttf\";\n"
"    font-size: 20px;\n"
"}")
        self.main_local_tr_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_local_tr_1.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.main_local_tr_1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.main_local_tr_1.setIndentation(20)
        self.main_local_tr_1.setSortingEnabled(True)
        self.main_local_tr_1.setWordWrap(True)
        self.main_local_tr_1.setObjectName("main_local_tr_1")
        self.main_local_tr_1.header().setCascadingSectionResizes(True)
        self.main_local_tr_1.header().setSortIndicatorShown(False)
        self.main_local_tr_1.header().setStretchLastSection(False)
        self.main_local_tr_2 = QtWidgets.QTreeWidget(self.main_local_sp)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_local_tr_2.setFont(font)
        self.main_local_tr_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_local_tr_2.setStyleSheet("QTreeWidget {\n"
"    background: rgb(240,240,240);\n"
"    color: rgb(45,45,45);\n"
"    margin-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"QTreeWidget:disabled {\n"
"    color: rgb(90,90,90);\n"
"    selection-color: rgb(90,90,90);\n"
"    selection-background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #eaeaea, stop:1 #dcdcdc);\n"
"}\n"
"\n"
"QTreeWidget::item:first {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    padding-left: 1px;\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTreeWidget::item:last {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    padding-right: 1px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(253,253,253);\n"
"    color: rgb(45,45,45);\n"
"    border-top: 1px solid lightgray;\n"
"    border-bottom: 1px solid lightgray;\n"
"    border-right: 1px solid lightgray;\n"
"    padding-left: 10px;\n"
"    padding-bottom: 3px;\n"
"    height: 30px;\n"
"    font-family: \"fonts/SourceSansPro-Regular.ttf\";\n"
"    font-size: 15px;\n"
"}")
        self.main_local_tr_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_local_tr_2.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.main_local_tr_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.main_local_tr_2.setIndentation(0)
        self.main_local_tr_2.setWordWrap(True)
        self.main_local_tr_2.setObjectName("main_local_tr_2")
        self.main_local_tr_2.header().setVisible(True)
        self.main_local_tr_2.header().setSortIndicatorShown(False)
        self.verticalLayout_2.addWidget(self.main_local_sp)
        self.layoutWidget_2 = QtWidgets.QWidget(self.main_splitter_1)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.main_remote_lb = QtWidgets.QLabel(self.layoutWidget_2)
        self.main_remote_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.main_remote_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        self.main_remote_lb.setFont(font)
        self.main_remote_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    padding-bottom: -2px;\n"
"}")
        self.main_remote_lb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_remote_lb.setObjectName("main_remote_lb")
        self.horizontalLayout_3.addWidget(self.main_remote_lb)
        self.main_remote_ln = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.main_remote_ln.setEnabled(True)
        self.main_remote_ln.setMinimumSize(QtCore.QSize(0, 27))
        self.main_remote_ln.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.main_remote_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_remote_ln.setFont(font)
        self.main_remote_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: rgb(200,200,200);\n"
"}")
        self.main_remote_ln.setText("")
        self.main_remote_ln.setFrame(False)
        self.main_remote_ln.setReadOnly(True)
        self.main_remote_ln.setObjectName("main_remote_ln")
        self.horizontalLayout_3.addWidget(self.main_remote_ln)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem15)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.main_remote_sp = QtWidgets.QSplitter(self.layoutWidget_2)
        self.main_remote_sp.setStyleSheet("QSplitter::handle {\n"
"    background: rgb(220,220,220);\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"    background: rgb(190,190,190);\n"
"}")
        self.main_remote_sp.setOrientation(QtCore.Qt.Vertical)
        self.main_remote_sp.setObjectName("main_remote_sp")
        self.main_remote_tr_1 = QtWidgets.QTreeView(self.main_remote_sp)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_remote_tr_1.setFont(font)
        self.main_remote_tr_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_remote_tr_1.setStyleSheet("QTreeView {\n"
"    background: rgb(240,240,240);\n"
"    color: rgb(45,45,45);\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTreeView:disabled {\n"
"    color: rgb(90,90,90);\n"
"    selection-color: rgb(90,90,90);\n"
"    selection-background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #eaeaea, stop:1 #dcdcdc);\n"
"}\n"
"\n"
"QTreeView::item: {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    padding-right: 1px;\n"
"    margin-right: 2px;\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    padding-left: 1px;\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(253,253,253);\n"
"    color: rgb(45,45,45);\n"
"    border-top: 1px solid lightgray;\n"
"    border-bottom: 1px solid lightgray;\n"
"    border-right: 1px solid lightgray;\n"
"    padding-left: 10px;\n"
"    padding-bottom: 3px;\n"
"    height: 30px;\n"
"    font-family: \"fonts/SourceSansPro-Regular.ttf\";\n"
"    font-size: 15px;\n"
"}")
        self.main_remote_tr_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_remote_tr_1.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.main_remote_tr_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.main_remote_tr_1.setIndentation(20)
        self.main_remote_tr_1.setSortingEnabled(True)
        self.main_remote_tr_1.setWordWrap(True)
        self.main_remote_tr_1.setObjectName("main_remote_tr_1")
        self.main_remote_tr_1.header().setCascadingSectionResizes(True)
        self.main_remote_tr_1.header().setSortIndicatorShown(False)
        self.main_remote_tr_1.header().setStretchLastSection(False)
        self.main_remote_tr_2 = QtWidgets.QTreeWidget(self.main_remote_sp)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_remote_tr_2.setFont(font)
        self.main_remote_tr_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_remote_tr_2.setStyleSheet("QTreeWidget {\n"
"    background: rgb(240,240,240);\n"
"    color: rgb(45,45,45);\n"
"    margin-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"QTreeWidget:disabled {\n"
"    color: rgb(90,90,90);\n"
"    selection-color: rgb(90,90,90);\n"
"    selection-background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #eaeaea, stop:1 #dcdcdc);\n"
"}\n"
"\n"
"QTreeWidget::item:first {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    padding-left: 1px;\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTreeWidget::item:last {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    padding-right: 1px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(253,253,253);\n"
"    color: rgb(45,45,45);\n"
"    border-top: 1px solid lightgray;\n"
"    border-bottom: 1px solid lightgray;\n"
"    border-right: 1px solid lightgray;\n"
"    padding-left: 10px;\n"
"    padding-bottom: 3px;\n"
"    height: 30px;\n"
"    font-family: \"fonts/SourceSansPro-Regular.ttf\";\n"
"    font-size: 15px;\n"
"}")
        self.main_remote_tr_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_remote_tr_2.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.main_remote_tr_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.main_remote_tr_2.setIndentation(0)
        self.main_remote_tr_2.setWordWrap(True)
        self.main_remote_tr_2.setObjectName("main_remote_tr_2")
        self.main_remote_tr_2.header().setVisible(True)
        self.main_remote_tr_2.header().setSortIndicatorShown(False)
        self.verticalLayout_3.addWidget(self.main_remote_sp)
        self.gridLayout_3.addWidget(self.main_splitter_1, 0, 0, 1, 1)
        self.main_tabwidget = QtWidgets.QTabWidget(self.main_splitter_2)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_tabwidget.setFont(font)
        self.main_tabwidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 0px solid rgb(180,180,180);\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    top: -1px;\n"
"    background-color: rgb(220,220,220);\n"
"    color: rgb(45,45,45);\n"
"    padding: 7px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    margin-top: 5px;\n"
"    background: transparent;\n"
"    border-top: 0px solid rgb(180,180,180);\n"
"    border-left: 0px solid rgb(180,180,180);\n"
"    border-right: 0px solid rgb(180,180,180);\n"
"    border-top-right-radius: 0px;\n"
"    border-top-left-radius: 0px;\n"
"    padding: 2px 10px 2px 10px;\n"
"    margin-right: 2px;\n"
"    color: rgb(45,45,45);\n"
"    \n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(210,210,210);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(220,220,220);\n"
"    color: rgb(45,45,45);\n"
"    border-bottom: 5px solid rgb(220,220,220);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 6px; \n"
"}\n"
"\n"
"QTabBar::scroller {\n"
"}\n"
"\n"
"QTabBar QToolButton {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    background-color: rgb(240,240,240);\n"
"}\n"
"\n"
"QTabBar QToolButton:hover {\n"
"    background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow {\n"
"    image: url(icons/right_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(icons/left_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}")
        self.main_tabwidget.setObjectName("main_tabwidget")
        self.connection_tab = QtWidgets.QWidget()
        self.connection_tab.setObjectName("connection_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.connection_tab)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.connexion_browser = QtWidgets.QTableWidget(self.connection_tab)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.connexion_browser.setFont(font)
        self.connexion_browser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.connexion_browser.setStyleSheet("QTableWidget {\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
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
"  border-bottom-right-radius: 3px;\n"
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
"  border-top-right-radius: 3px;\n"
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
"  border-bottom-right-radius: 3px;\n"
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
"border-bottom-left-radius: 3px;\n"
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
        self.connexion_browser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.connexion_browser.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.connexion_browser.setShowGrid(False)
        self.connexion_browser.setRowCount(0)
        self.connexion_browser.setColumnCount(2)
        self.connexion_browser.setObjectName("connexion_browser")
        self.connexion_browser.horizontalHeader().setVisible(False)
        self.connexion_browser.verticalHeader().setVisible(False)
        self.connexion_browser.verticalHeader().setDefaultSectionSize(20)
        self.gridLayout_5.addWidget(self.connexion_browser, 0, 0, 1, 1)
        self.main_tabwidget.addTab(self.connection_tab, "")
        self.transfers_tab = QtWidgets.QWidget()
        self.transfers_tab.setObjectName("transfers_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.transfers_tab)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.transfert_tree = QtWidgets.QTreeWidget(self.transfers_tab)
        self.transfert_tree.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.transfert_tree.setFont(font)
        self.transfert_tree.setFocusPolicy(QtCore.Qt.NoFocus)
        self.transfert_tree.setStyleSheet("QTreeWidget {\n"
"    background: rgb(240,240,240);\n"
"    color: rgb(45,45,45);\n"
"    margin-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"QTreeWidget:disabled {\n"
"    color: rgb(90,90,90);\n"
"    selection-color: rgb(90,90,90);\n"
"    selection-background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #eaeaea, stop:1 #dcdcdc);\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    margin-top: 0px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"\n"
"QTreeWidget::item:first {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    padding-left: 1px;\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTreeWidget::item:last {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    padding-right: 1px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(253,253,253);\n"
"    color: rgb(45,45,45);\n"
"    border-top: 1px solid lightgray;\n"
"    border-bottom: 1px solid lightgray;\n"
"    border-right: 1px solid lightgray;\n"
"    padding-left: 10px;\n"
"    padding-bottom: 3px;\n"
"    height: 25px;\n"
"    font-family: \"fonts/SourceSansPro-Regular.ttf\";\n"
"    font-size: 15px;\n"
"    margin-bottom: 3px;\n"
"}")
        self.transfert_tree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.transfert_tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.transfert_tree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.transfert_tree.setIndentation(0)
        self.transfert_tree.setWordWrap(True)
        self.transfert_tree.setHeaderHidden(True)
        self.transfert_tree.setObjectName("transfert_tree")
        self.transfert_tree.header().setVisible(False)
        self.gridLayout_6.addWidget(self.transfert_tree, 0, 0, 1, 1)
        self.main_tabwidget.addTab(self.transfers_tab, "")
        self.gridLayout.addWidget(self.main_splitter_2, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_tabwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OrionFTP"))
        self.main_profile_lb.setText(_translate("MainWindow", "FTP profile:"))
        self.main_profile_cb.setItemText(0, _translate("MainWindow", "No stored profile..."))
        self.main_connect_bt.setText(_translate("MainWindow", "Connect"))
        self.main_upload_bt.setText(_translate("MainWindow", "Send"))
        self.main_download_bt.setText(_translate("MainWindow", "Receive"))
        self.main_local_lb.setText(_translate("MainWindow", "Local:"))
        self.main_local_tr_2.setSortingEnabled(True)
        self.main_local_tr_2.headerItem().setText(0, _translate("MainWindow", "File"))
        self.main_local_tr_2.headerItem().setText(1, _translate("MainWindow", "Size"))
        self.main_local_tr_2.headerItem().setText(2, _translate("MainWindow", "Type"))
        self.main_remote_lb.setText(_translate("MainWindow", "Remote:"))
        self.main_remote_tr_2.setSortingEnabled(True)
        self.main_remote_tr_2.headerItem().setText(0, _translate("MainWindow", "File"))
        self.main_remote_tr_2.headerItem().setText(1, _translate("MainWindow", "Size"))
        self.main_remote_tr_2.headerItem().setText(2, _translate("MainWindow", "Type"))
        self.main_tabwidget.setTabText(self.main_tabwidget.indexOf(self.connection_tab), _translate("MainWindow", "FTP Connection"))
        self.transfert_tree.headerItem().setText(0, _translate("MainWindow", "Status"))
        self.transfert_tree.headerItem().setText(1, _translate("MainWindow", "File"))
        self.transfert_tree.headerItem().setText(2, _translate("MainWindow", "Size"))
        self.transfert_tree.headerItem().setText(3, _translate("MainWindow", "Speed"))
        self.transfert_tree.headerItem().setText(4, _translate("MainWindow", "Progress"))
        self.main_tabwidget.setTabText(self.main_tabwidget.indexOf(self.transfers_tab), _translate("MainWindow", "Transfers"))

