# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/mainScreen.ui'
#
# Created: Tue Nov  5 23:28:23 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainScreen(object):
    def setupUi(self, mainScreen):
        mainScreen.setObjectName("mainScreen")
        mainScreen.setWindowModality(QtCore.Qt.NonModal)
        mainScreen.setEnabled(True)
        mainScreen.resize(410, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainScreen.sizePolicy().hasHeightForWidth())
        mainScreen.setSizePolicy(sizePolicy)
        mainScreen.setMinimumSize(QtCore.QSize(410, 300))
        mainScreen.setMaximumSize(QtCore.QSize(410, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/swords.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainScreen.setWindowIcon(icon)
        mainScreen.setTabPosition(QtGui.QTabWidget.North)
        mainScreen.setTabShape(QtGui.QTabWidget.Rounded)
        mainScreen.setIconSize(QtCore.QSize(48, 48))
        mainScreen.setElideMode(QtCore.Qt.ElideNone)
        self.raidTab = QtGui.QWidget()
        self.raidTab.setObjectName("raidTab")
        self.raidTable = QtGui.QTableWidget(self.raidTab)
        self.raidTable.setGeometry(QtCore.QRect(1, 0, 404, 230))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raidTable.sizePolicy().hasHeightForWidth())
        self.raidTable.setSizePolicy(sizePolicy)
        self.raidTable.setMinimumSize(QtCore.QSize(404, 230))
        self.raidTable.setMaximumSize(QtCore.QSize(404, 267))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.raidTable.setFont(font)
        self.raidTable.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.raidTable.setFrameShadow(QtGui.QFrame.Sunken)
        self.raidTable.setLineWidth(0)
        self.raidTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.raidTable.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
        self.raidTable.setDragDropOverwriteMode(False)
        self.raidTable.setAlternatingRowColors(True)
        self.raidTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.raidTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.raidTable.setTextElideMode(QtCore.Qt.ElideLeft)
        self.raidTable.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.raidTable.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.raidTable.setShowGrid(True)
        self.raidTable.setGridStyle(QtCore.Qt.DotLine)
        self.raidTable.setWordWrap(False)
        self.raidTable.setCornerButtonEnabled(False)
        self.raidTable.setColumnCount(13)
        self.raidTable.setObjectName("raidTable")
        self.raidTable.setColumnCount(13)
        self.raidTable.setRowCount(0)
        self.raidTable.horizontalHeader().setCascadingSectionResizes(False)
        self.raidTable.horizontalHeader().setDefaultSectionSize(30)
        self.raidTable.horizontalHeader().setHighlightSections(False)
        self.raidTable.horizontalHeader().setMinimumSectionSize(30)
        self.raidTable.horizontalHeader().setStretchLastSection(True)
        self.raidTable.verticalHeader().setVisible(False)
        self.raidTable.verticalHeader().setDefaultSectionSize(25)
        self.raidTable.verticalHeader().setMinimumSectionSize(25)
        self.buttonRaid = QtGui.QPushButton(self.raidTab)
        self.buttonRaid.setGeometry(QtCore.QRect(0, 230, 50, 38))
        self.buttonRaid.setIconSize(QtCore.QSize(32, 32))
        self.buttonRaid.setObjectName("buttonRaid")
        self.buttonAdd = QtGui.QPushButton(self.raidTab)
        self.buttonAdd.setGeometry(QtCore.QRect(210, 230, 50, 38))
        self.buttonAdd.setObjectName("buttonAdd")
        self.buttonDelete = QtGui.QPushButton(self.raidTab)
        self.buttonDelete.setGeometry(QtCore.QRect(260, 230, 60, 38))
        self.buttonDelete.setObjectName("buttonDelete")
        self.raidProgress = QtGui.QProgressBar(self.raidTab)
        self.raidProgress.setGeometry(QtCore.QRect(50, 231, 159, 36))
        self.raidProgress.setProperty("value", 24)
        self.raidProgress.setObjectName("raidProgress")
        self.buttonDeleteAll = QtGui.QPushButton(self.raidTab)
        self.buttonDeleteAll.setGeometry(QtCore.QRect(320, 230, 86, 38))
        self.buttonDeleteAll.setObjectName("buttonDeleteAll")
        mainScreen.addTab(self.raidTab, "")
        self.troopTab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.troopTab.sizePolicy().hasHeightForWidth())
        self.troopTab.setSizePolicy(sizePolicy)
        self.troopTab.setObjectName("troopTab")
        mainScreen.addTab(self.troopTab, "")

        self.retranslateUi(mainScreen)
        mainScreen.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainScreen)

    def retranslateUi(self, mainScreen):
        mainScreen.setWindowTitle(QtGui.QApplication.translate("mainScreen", "Travian Raider 2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonRaid.setText(QtGui.QApplication.translate("mainScreen", "Raid", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdd.setText(QtGui.QApplication.translate("mainScreen", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDelete.setText(QtGui.QApplication.translate("mainScreen", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDeleteAll.setText(QtGui.QApplication.translate("mainScreen", "Delete All", None, QtGui.QApplication.UnicodeUTF8))
        mainScreen.setTabText(mainScreen.indexOf(self.raidTab), QtGui.QApplication.translate("mainScreen", "Raids", None, QtGui.QApplication.UnicodeUTF8))
        mainScreen.setTabToolTip(mainScreen.indexOf(self.raidTab), QtGui.QApplication.translate("mainScreen", "Manage Raids", None, QtGui.QApplication.UnicodeUTF8))
        mainScreen.setTabText(mainScreen.indexOf(self.troopTab), QtGui.QApplication.translate("mainScreen", "Troops", None, QtGui.QApplication.UnicodeUTF8))
        mainScreen.setTabToolTip(mainScreen.indexOf(self.troopTab), QtGui.QApplication.translate("mainScreen", "Manage Troops", None, QtGui.QApplication.UnicodeUTF8))

import imgs_rc
