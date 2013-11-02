# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/untitled.ui'
#
# Created: Sat Nov  2 09:08:59 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(300, 180)
        Dialog.setMinimumSize(QtCore.QSize(300, 180))
        Dialog.setMaximumSize(QtCore.QSize(300, 180))
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.usrEntry = QtGui.QLineEdit(Dialog)
        self.usrEntry.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.usrEntry.setObjectName("usrEntry")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.usrEntry)
        self.pwdEntry = QtGui.QLineEdit(Dialog)
        self.pwdEntry.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pwdEntry.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdEntry.setObjectName("pwdEntry")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.pwdEntry)
        self.srvEntry = QtGui.QLineEdit(Dialog)
        self.srvEntry.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.srvEntry.setObjectName("srvEntry")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.srvEntry)
        self.buttonLogin = QtGui.QPushButton(Dialog)
        self.buttonLogin.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.buttonLogin.setObjectName("buttonLogin")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.buttonLogin)
        self.checkRemember = QtGui.QCheckBox(Dialog)
        self.checkRemember.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.checkRemember.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkRemember.setTristate(False)
        self.checkRemember.setObjectName("checkRemember")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkRemember)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.usrEntry, self.pwdEntry)
        Dialog.setTabOrder(self.pwdEntry, self.srvEntry)
        Dialog.setTabOrder(self.srvEntry, self.checkRemember)
        Dialog.setTabOrder(self.checkRemember, self.buttonLogin)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Travian Raider 2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.usrEntry.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.pwdEntry.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.srvEntry.setText(QtGui.QApplication.translate("Dialog", "http://ts7.travian.com/", None, QtGui.QApplication.UnicodeUTF8))
        self.srvEntry.setPlaceholderText(QtGui.QApplication.translate("Dialog", "http://server.travian.domain/", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLogin.setText(QtGui.QApplication.translate("Dialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.checkRemember.setText(QtGui.QApplication.translate("Dialog", "Remember credentials", None, QtGui.QApplication.UnicodeUTF8))

