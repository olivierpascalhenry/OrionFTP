# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storewindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_storeWindow(object):
    def setupUi(self, storeWindow):
        storeWindow.setObjectName("storeWindow")
        storeWindow.resize(550, 140)
        storeWindow.setMinimumSize(QtCore.QSize(0, 0))
        storeWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        storeWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/download_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        storeWindow.setWindowIcon(icon)
        storeWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(storeWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.sw_progressbar = QtWidgets.QProgressBar(storeWindow)
        self.sw_progressbar.setMinimumSize(QtCore.QSize(0, 27))
        self.sw_progressbar.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sw_progressbar.setFont(font)
        self.sw_progressbar.setStyleSheet("QProgressBar {\n"
"   border: 0px solid black;\n"
"   border-radius: 3px;\n"
"   background: rgb(220,220,220);\n"
"   color: rgb(45,45,45);\n"
"   text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"   border: 0px solid black;\n"
"   border-radius: 3px;\n"
"   background: rgb(0,200,0);\n"
" }")
        self.sw_progressbar.setProperty("value", 0)
        self.sw_progressbar.setTextVisible(True)
        self.sw_progressbar.setObjectName("sw_progressbar")
        self.gridLayout.addWidget(self.sw_progressbar, 0, 0, 1, 1)
        self.sw_label = QtWidgets.QLabel(storeWindow)
        self.sw_label.setMinimumSize(QtCore.QSize(0, 0))
        self.sw_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setItalic(True)
        self.sw_label.setFont(font)
        self.sw_label.setStyleSheet("QLabel {\n"
"    margin-top: 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.sw_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.sw_label.setWordWrap(True)
        self.sw_label.setObjectName("sw_label")
        self.gridLayout.addWidget(self.sw_label, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.sw_button = QtWidgets.QToolButton(storeWindow)
        self.sw_button.setMinimumSize(QtCore.QSize(100, 27))
        self.sw_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.sw_button.setFont(font)
        self.sw_button.setStyleSheet("QToolButton {\n"
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
        self.sw_button.setObjectName("sw_button")
        self.horizontalLayout.addWidget(self.sw_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(storeWindow)
        QtCore.QMetaObject.connectSlotsByName(storeWindow)

    def retranslateUi(self, storeWindow):
        _translate = QtCore.QCoreApplication.translate
        storeWindow.setWindowTitle(_translate("storeWindow", "Download"))
        self.sw_progressbar.setFormat(_translate("storeWindow", "%p %"))
        self.sw_label.setText(_translate("storeWindow", "Downloading..."))
        self.sw_button.setText(_translate("storeWindow", "Cancel"))

