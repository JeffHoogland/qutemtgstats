# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created: Thu Nov  6 12:56:59 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 535)
        MainWindow.setMinimumSize(QtCore.QSize(800, 535))
        MainWindow.setMaximumSize(QtCore.QSize(800, 535))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 535))
        self.tabWidget.setObjectName("tabWidget")
        self.dataTab = QtGui.QWidget()
        self.dataTab.setObjectName("dataTab")
        self.statsPaste = QtGui.QTextEdit(self.dataTab)
        self.statsPaste.setGeometry(QtCore.QRect(0, 40, 795, 401))
        self.statsPaste.setAcceptRichText(False)
        self.statsPaste.setObjectName("statsPaste")
        self.phraseButton = QtGui.QToolButton(self.dataTab)
        self.phraseButton.setGeometry(QtCore.QRect(10, 450, 781, 41))
        self.phraseButton.setObjectName("phraseButton")
        self.label = QtGui.QLabel(self.dataTab)
        self.label.setGeometry(QtCore.QRect(250, 0, 261, 41))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.dataTab, "")
        self.formatTab = QtGui.QWidget()
        self.formatTab.setObjectName("formatTab")
        self.tabWidget.addTab(self.formatTab, "")
        self.eventTab = QtGui.QWidget()
        self.eventTab.setObjectName("eventTab")
        self.tabWidget.addTab(self.eventTab, "")
        self.opponentTab = QtGui.QWidget()
        self.opponentTab.setObjectName("opponentTab")
        self.treeWidget = QtGui.QTreeWidget(self.opponentTab)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 795, 501))
        self.treeWidget.setObjectName("treeWidget")
        self.tabWidget.addTab(self.opponentTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionMenu_Item = QtGui.QAction(MainWindow)
        self.actionMenu_Item.setObjectName("actionMenu_Item")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Qute MTG Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.phraseButton.setText(QtGui.QApplication.translate("MainWindow", "Phrase Data and Generate Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Paste Data Below:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dataTab), QtGui.QApplication.translate("MainWindow", "Raw Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.formatTab), QtGui.QApplication.translate("MainWindow", "Stats by Format", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eventTab), QtGui.QApplication.translate("MainWindow", "Stats by Event Type", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Opponent", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Wins", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Losses", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Draws", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.opponentTab), QtGui.QApplication.translate("MainWindow", "Stats by Opponent", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMenu_Item.setText(QtGui.QApplication.translate("MainWindow", "Menu Item", None, QtGui.QApplication.UnicodeUTF8))

