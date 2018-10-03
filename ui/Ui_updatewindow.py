# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updatewindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_updateWindow(object):
    def setupUi(self, updateWindow):
        updateWindow.setObjectName("updateWindow")
        updateWindow.resize(600, 210)
        updateWindow.setMinimumSize(QtCore.QSize(0, 0))
        updateWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        updateWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/orionftp_update_on.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        updateWindow.setWindowIcon(icon)
        updateWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(updateWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.uw_label_1 = QtWidgets.QLabel(updateWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uw_label_1.sizePolicy().hasHeightForWidth())
        self.uw_label_1.setSizePolicy(sizePolicy)
        self.uw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.uw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.uw_label_1.setFont(font)
        self.uw_label_1.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.uw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.uw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.uw_label_1.setLineWidth(0)
        self.uw_label_1.setMidLineWidth(0)
        self.uw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.uw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.uw_label_1.setWordWrap(True)
        self.uw_label_1.setObjectName("uw_label_1")
        self.gridLayout.addWidget(self.uw_label_1, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.uw_update_button = QtWidgets.QToolButton(updateWindow)
        self.uw_update_button.setMinimumSize(QtCore.QSize(100, 27))
        self.uw_update_button.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.uw_update_button.setFont(font)
        self.uw_update_button.setStyleSheet("QToolButton {\n"
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
        self.uw_update_button.setIconSize(QtCore.QSize(25, 25))
        self.uw_update_button.setObjectName("uw_update_button")
        self.horizontalLayout_2.addWidget(self.uw_update_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.uw_cancel_button = QtWidgets.QToolButton(updateWindow)
        self.uw_cancel_button.setMinimumSize(QtCore.QSize(100, 27))
        self.uw_cancel_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.uw_cancel_button.setFont(font)
        self.uw_cancel_button.setStyleSheet("QToolButton {\n"
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
        self.uw_cancel_button.setIconSize(QtCore.QSize(25, 25))
        self.uw_cancel_button.setObjectName("uw_cancel_button")
        self.horizontalLayout_2.addWidget(self.uw_cancel_button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(updateWindow)
        QtCore.QMetaObject.connectSlotsByName(updateWindow)

    def retranslateUi(self, updateWindow):
        _translate = QtCore.QCoreApplication.translate
        updateWindow.setWindowTitle(_translate("updateWindow", "Ready to update"))
        self.uw_label_1.setText(_translate("updateWindow", "<html><head/><body><p align=\"justify\">Click on <span style=\" font-weight:600;\">Update</span> to download and install automatically the last update from <span style=\" font-weight:600;\">GitHub</span> repository.</p><p align=\"justify\">On <span style=\" font-weight:600;\">Windows</span>, the installation of the update requires actions from the user and can be canceled. On <span style=\" font-weight:600;\">Linux</span>, the process is fully automatic and can\'t be interrupted until it is over.</p></body></html>"))
        self.uw_update_button.setText(_translate("updateWindow", "Update"))
        self.uw_cancel_button.setText(_translate("updateWindow", "Cancel"))

