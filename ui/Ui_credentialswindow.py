# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credentialswindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_credentialsWindow(object):
    def setupUi(self, credentialsWindow):
        credentialsWindow.setObjectName("credentialsWindow")
        credentialsWindow.resize(602, 356)
        credentialsWindow.setMinimumSize(QtCore.QSize(0, 0))
        credentialsWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        credentialsWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        credentialsWindow.setWindowIcon(icon)
        credentialsWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout_3 = QtWidgets.QGridLayout(credentialsWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.cw_label_7 = QtWidgets.QLabel(credentialsWindow)
        self.cw_label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_7.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_7.setFont(font)
        self.cw_label_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.cw_label_7.setObjectName("cw_label_7")
        self.gridLayout_2.addWidget(self.cw_label_7, 0, 3, 1, 1)
        self.cw_label_1 = QtWidgets.QLabel(credentialsWindow)
        self.cw_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_1.setFont(font)
        self.cw_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.cw_label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cw_label_1.setObjectName("cw_label_1")
        self.gridLayout_2.addWidget(self.cw_label_1, 0, 1, 1, 1)
        self.cw_label_2 = QtWidgets.QLabel(credentialsWindow)
        self.cw_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_2.setFont(font)
        self.cw_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.cw_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cw_label_2.setObjectName("cw_label_2")
        self.gridLayout_2.addWidget(self.cw_label_2, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 2, 1, 1)
        self.cw_label_3 = QtWidgets.QLabel(credentialsWindow)
        self.cw_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_3.setFont(font)
        self.cw_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.cw_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cw_label_3.setObjectName("cw_label_3")
        self.gridLayout_2.addWidget(self.cw_label_3, 2, 1, 1, 1)
        self.cw_label_8 = QtWidgets.QLabel(credentialsWindow)
        self.cw_label_8.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_8.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_8.setFont(font)
        self.cw_label_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.cw_label_8.setObjectName("cw_label_8")
        self.gridLayout_2.addWidget(self.cw_label_8, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        self.cw_label_9 = QtWidgets.QLabel(credentialsWindow)
        self.cw_label_9.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_9.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_9.setFont(font)
        self.cw_label_9.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.cw_label_9.setObjectName("cw_label_9")
        self.gridLayout_2.addWidget(self.cw_label_9, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem5, 1, 0, 1, 1)
        self.cw_label_4 = QtWidgets.QLabel(credentialsWindow)
        self.cw_label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.cw_label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_4.setFont(font)
        self.cw_label_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.cw_label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cw_label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cw_label_4.setLineWidth(0)
        self.cw_label_4.setMidLineWidth(0)
        self.cw_label_4.setTextFormat(QtCore.Qt.AutoText)
        self.cw_label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.cw_label_4.setWordWrap(True)
        self.cw_label_4.setOpenExternalLinks(True)
        self.cw_label_4.setObjectName("cw_label_4")
        self.gridLayout_3.addWidget(self.cw_label_4, 2, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem6, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.cw_label_5 = QtWidgets.QLabel(credentialsWindow)
        self.cw_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_5.setFont(font)
        self.cw_label_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.cw_label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cw_label_5.setObjectName("cw_label_5")
        self.gridLayout.addWidget(self.cw_label_5, 0, 0, 1, 1)
        self.edit_1 = QtWidgets.QLineEdit(credentialsWindow)
        self.edit_1.setEnabled(True)
        self.edit_1.setMinimumSize(QtCore.QSize(0, 27))
        self.edit_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_1.setFont(font)
        self.edit_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.edit_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200, 200, 200);\n"
"}")
        self.edit_1.setFrame(False)
        self.edit_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.edit_1.setObjectName("edit_1")
        self.gridLayout.addWidget(self.edit_1, 0, 1, 1, 1)
        self.cw_label_6 = QtWidgets.QLabel(credentialsWindow)
        self.cw_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.cw_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_6.setFont(font)
        self.cw_label_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.cw_label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cw_label_6.setObjectName("cw_label_6")
        self.gridLayout.addWidget(self.cw_label_6, 1, 0, 1, 1)
        self.edit_2 = QtWidgets.QLineEdit(credentialsWindow)
        self.edit_2.setEnabled(True)
        self.edit_2.setMinimumSize(QtCore.QSize(0, 27))
        self.edit_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.edit_2.setFont(font)
        self.edit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.edit_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200, 200, 200);\n"
"}")
        self.edit_2.setFrame(False)
        self.edit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.edit_2.setObjectName("edit_2")
        self.gridLayout.addWidget(self.edit_2, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.cw_submit_button = QtWidgets.QToolButton(credentialsWindow)
        self.cw_submit_button.setEnabled(False)
        self.cw_submit_button.setMinimumSize(QtCore.QSize(90, 27))
        self.cw_submit_button.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cw_submit_button.setFont(font)
        self.cw_submit_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
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
        self.cw_submit_button.setObjectName("cw_submit_button")
        self.horizontalLayout_2.addWidget(self.cw_submit_button)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.cw_cancel_button = QtWidgets.QToolButton(credentialsWindow)
        self.cw_cancel_button.setMinimumSize(QtCore.QSize(90, 27))
        self.cw_cancel_button.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cw_cancel_button.setFont(font)
        self.cw_cancel_button.setStyleSheet("QToolButton {\n"
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
        self.cw_cancel_button.setObjectName("cw_cancel_button")
        self.horizontalLayout_2.addWidget(self.cw_cancel_button)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)

        self.retranslateUi(credentialsWindow)
        QtCore.QMetaObject.connectSlotsByName(credentialsWindow)

    def retranslateUi(self, credentialsWindow):
        _translate = QtCore.QCoreApplication.translate
        credentialsWindow.setWindowTitle(_translate("credentialsWindow", "Information"))
        self.cw_label_7.setText(_translate("credentialsWindow", "TMP"))
        self.cw_label_1.setText(_translate("credentialsWindow", "Host:"))
        self.cw_label_2.setText(_translate("credentialsWindow", "Username:"))
        self.cw_label_3.setText(_translate("credentialsWindow", "Password:"))
        self.cw_label_8.setText(_translate("credentialsWindow", "TMP"))
        self.cw_label_9.setText(_translate("credentialsWindow", "TMP"))
        self.cw_label_4.setText(_translate("credentialsWindow", "<html><head/><body><p>There is no username and/or password stored with this profile. Please enter a username and/or a password for this server.</p></body></html>"))
        self.cw_label_5.setText(_translate("credentialsWindow", "Username:"))
        self.cw_label_6.setText(_translate("credentialsWindow", "Password:"))
        self.cw_submit_button.setText(_translate("credentialsWindow", "Submit"))
        self.cw_cancel_button.setText(_translate("credentialsWindow", "Cancel"))

