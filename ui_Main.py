# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created: Thu Nov  6 19:13:28 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 535)
        MainWindow.setMinimumSize(QtCore.QSize(800, 535))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.dataTab = QtGui.QWidget()
        self.dataTab.setObjectName("dataTab")
        self.verticalLayout = QtGui.QVBoxLayout(self.dataTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.dataTab)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.statsPaste = QtGui.QTextEdit(self.dataTab)
        self.statsPaste.setAcceptRichText(False)
        self.statsPaste.setObjectName("statsPaste")
        self.verticalLayout.addWidget(self.statsPaste)
        self.phraseButton = QtGui.QToolButton(self.dataTab)
        self.phraseButton.setObjectName("phraseButton")
        self.verticalLayout.addWidget(self.phraseButton)
        self.tabWidget.addTab(self.dataTab, "")
        self.filtersTab = QtGui.QWidget()
        self.filtersTab.setObjectName("filtersTab")
        self.tabWidget.addTab(self.filtersTab, "")
        self.eventListTab = QtGui.QWidget()
        self.eventListTab.setObjectName("eventListTab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.eventListTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.eventTree = QtGui.QTreeWidget(self.eventListTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventTree.sizePolicy().hasHeightForWidth())
        self.eventTree.setSizePolicy(sizePolicy)
        self.eventTree.setAutoFillBackground(False)
        self.eventTree.setObjectName("eventTree")
        self.horizontalLayout_2.addWidget(self.eventTree)
        self.tabWidget.addTab(self.eventListTab, "")
        self.formatTab = QtGui.QWidget()
        self.formatTab.setObjectName("formatTab")
        self.tabWidget.addTab(self.formatTab, "")
        self.eventTab = QtGui.QWidget()
        self.eventTab.setObjectName("eventTab")
        self.tabWidget.addTab(self.eventTab, "")
        self.opponentTab = QtGui.QWidget()
        self.opponentTab.setObjectName("opponentTab")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.opponentTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.opponentTree = QtGui.QTreeWidget(self.opponentTab)
        self.opponentTree.setAutoFillBackground(False)
        self.opponentTree.setObjectName("opponentTree")
        self.horizontalLayout_3.addWidget(self.opponentTree)
        self.tabWidget.addTab(self.opponentTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionMenu_Item = QtGui.QAction(MainWindow)
        self.actionMenu_Item.setObjectName("actionMenu_Item")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Qute MTG Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Paste Data Below:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.phraseButton.setText(QtGui.QApplication.translate("MainWindow", "Phrase Data and Generate Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dataTab), QtGui.QApplication.translate("MainWindow", "Raw Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filtersTab), QtGui.QApplication.translate("MainWindow", "Filters", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Place", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Players", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Format", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(5, QtGui.QApplication.translate("MainWindow", "Location", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(6, QtGui.QApplication.translate("MainWindow", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(7, QtGui.QApplication.translate("MainWindow", "Wins", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(8, QtGui.QApplication.translate("MainWindow", "Losses", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(9, QtGui.QApplication.translate("MainWindow", "Draws", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eventListTab), QtGui.QApplication.translate("MainWindow", "Event List", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.formatTab), QtGui.QApplication.translate("MainWindow", "Stats by Format", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eventTab), QtGui.QApplication.translate("MainWindow", "Stats by Event Type", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentTree.setSortingEnabled(True)
        self.opponentTree.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Opponent", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentTree.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Wins", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentTree.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Losses", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentTree.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Draws", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentTree.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.opponentTab), QtGui.QApplication.translate("MainWindow", "Stats by Opponent", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMenu_Item.setText(QtGui.QApplication.translate("MainWindow", "Menu Item", None, QtGui.QApplication.UnicodeUTF8))

