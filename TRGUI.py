#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TRGUI.py

__author__ = "Adrian Torres"
__date__ = "2013-11-02"
__version__ = "1.0"


import sys
import TRCore
import parsing
from tr2gui import Ui_Dialog
from PySide.QtCore import *
from PySide.QtGui import *


class MainDialog(QDialog, Ui_Dialog):
    
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonLogin.clicked.connect(self.login)
    
    def login(self):
        usr = self.usrEntry.text()
        pwd = self.pwdEntry.text()
        srv = self.srvEntry.text()
        if TRCore.login(srv, usr, pwd):
            QMessageBox.information(self, "Login", "Login Successful!")
            self.close()
        else:
            QMessageBox.warning(self, "Login", "Invalid credentials")

app = QApplication(sys.argv)
mainDialog = MainDialog()
mainDialog.show()
app.exec_()
