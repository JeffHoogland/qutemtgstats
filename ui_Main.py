# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created: Thu Nov  6 20:19:48 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 630)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 630))
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
        self.phraseButton = QtGui.QPushButton(self.dataTab)
        self.phraseButton.setObjectName("phraseButton")
        self.verticalLayout.addWidget(self.phraseButton)
        self.tabWidget.addTab(self.dataTab, "")
        self.filtersTab = QtGui.QWidget()
        self.filtersTab.setObjectName("filtersTab")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.filtersTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtGui.QFrame(self.filtersTab)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formatFrame = QtGui.QFrame(self.frame)
        self.formatFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.formatFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.formatFrame.setObjectName("formatFrame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.formatFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formatLabel = QtGui.QLabel(self.formatFrame)
        self.formatLabel.setObjectName("formatLabel")
        self.verticalLayout_2.addWidget(self.formatLabel)
        self.standardFilter = QtGui.QCheckBox(self.formatFrame)
        self.standardFilter.setChecked(True)
        self.standardFilter.setObjectName("standardFilter")
        self.verticalLayout_2.addWidget(self.standardFilter)
        self.modernFilter = QtGui.QCheckBox(self.formatFrame)
        self.modernFilter.setChecked(True)
        self.modernFilter.setObjectName("modernFilter")
        self.verticalLayout_2.addWidget(self.modernFilter)
        self.legacyFilter = QtGui.QCheckBox(self.formatFrame)
        self.legacyFilter.setChecked(True)
        self.legacyFilter.setObjectName("legacyFilter")
        self.verticalLayout_2.addWidget(self.legacyFilter)
        self.vintageFilter = QtGui.QCheckBox(self.formatFrame)
        self.vintageFilter.setChecked(True)
        self.vintageFilter.setObjectName("vintageFilter")
        self.verticalLayout_2.addWidget(self.vintageFilter)
        self.boosterDraftFilter = QtGui.QCheckBox(self.formatFrame)
        self.boosterDraftFilter.setChecked(True)
        self.boosterDraftFilter.setObjectName("boosterDraftFilter")
        self.verticalLayout_2.addWidget(self.boosterDraftFilter)
        self.sealedFilter = QtGui.QCheckBox(self.formatFrame)
        self.sealedFilter.setChecked(True)
        self.sealedFilter.setObjectName("sealedFilter")
        self.verticalLayout_2.addWidget(self.sealedFilter)
        self.twoHGSealedFilter = QtGui.QCheckBox(self.formatFrame)
        self.twoHGSealedFilter.setChecked(True)
        self.twoHGSealedFilter.setObjectName("twoHGSealedFilter")
        self.verticalLayout_2.addWidget(self.twoHGSealedFilter)
        self.casualFilter = QtGui.QCheckBox(self.formatFrame)
        self.casualFilter.setChecked(True)
        self.casualFilter.setObjectName("casualFilter")
        self.verticalLayout_2.addWidget(self.casualFilter)
        self.otherFormatFilter = QtGui.QCheckBox(self.formatFrame)
        self.otherFormatFilter.setChecked(True)
        self.otherFormatFilter.setObjectName("otherFormatFilter")
        self.verticalLayout_2.addWidget(self.otherFormatFilter)
        self.horizontalLayout_4.addWidget(self.formatFrame)
        self.eventFrame = QtGui.QFrame(self.frame)
        self.eventFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.eventFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.eventFrame.setObjectName("eventFrame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.eventFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.eventLabel = QtGui.QLabel(self.eventFrame)
        self.eventLabel.setObjectName("eventLabel")
        self.verticalLayout_3.addWidget(self.eventLabel)
        self.premiumTournamentFilter = QtGui.QCheckBox(self.eventFrame)
        self.premiumTournamentFilter.setChecked(True)
        self.premiumTournamentFilter.setObjectName("premiumTournamentFilter")
        self.verticalLayout_3.addWidget(self.premiumTournamentFilter)
        self.grandPrixFilter = QtGui.QCheckBox(self.eventFrame)
        self.grandPrixFilter.setChecked(True)
        self.grandPrixFilter.setObjectName("grandPrixFilter")
        self.verticalLayout_3.addWidget(self.grandPrixFilter)
        self.proTourFilter = QtGui.QCheckBox(self.eventFrame)
        self.proTourFilter.setChecked(True)
        self.proTourFilter.setObjectName("proTourFilter")
        self.verticalLayout_3.addWidget(self.proTourFilter)
        self.PTQFilter = QtGui.QCheckBox(self.eventFrame)
        self.PTQFilter.setChecked(True)
        self.PTQFilter.setObjectName("PTQFilter")
        self.verticalLayout_3.addWidget(self.PTQFilter)
        self.gameDayFilter = QtGui.QCheckBox(self.eventFrame)
        self.gameDayFilter.setChecked(True)
        self.gameDayFilter.setObjectName("gameDayFilter")
        self.verticalLayout_3.addWidget(self.gameDayFilter)
        self.prereleaseFilter = QtGui.QCheckBox(self.eventFrame)
        self.prereleaseFilter.setChecked(True)
        self.prereleaseFilter.setObjectName("prereleaseFilter")
        self.verticalLayout_3.addWidget(self.prereleaseFilter)
        self.tournamentFilter = QtGui.QCheckBox(self.eventFrame)
        self.tournamentFilter.setChecked(True)
        self.tournamentFilter.setObjectName("tournamentFilter")
        self.verticalLayout_3.addWidget(self.tournamentFilter)
        self.GPTFilter = QtGui.QCheckBox(self.eventFrame)
        self.GPTFilter.setChecked(True)
        self.GPTFilter.setObjectName("GPTFilter")
        self.verticalLayout_3.addWidget(self.GPTFilter)
        self.FNMFilter = QtGui.QCheckBox(self.eventFrame)
        self.FNMFilter.setChecked(True)
        self.FNMFilter.setObjectName("FNMFilter")
        self.verticalLayout_3.addWidget(self.FNMFilter)
        self.WMCQFilter = QtGui.QCheckBox(self.eventFrame)
        self.WMCQFilter.setChecked(True)
        self.WMCQFilter.setObjectName("WMCQFilter")
        self.verticalLayout_3.addWidget(self.WMCQFilter)
        self.EightManFilter = QtGui.QCheckBox(self.eventFrame)
        self.EightManFilter.setChecked(True)
        self.EightManFilter.setObjectName("EightManFilter")
        self.verticalLayout_3.addWidget(self.EightManFilter)
        self.CelebrationFilter = QtGui.QCheckBox(self.eventFrame)
        self.CelebrationFilter.setChecked(True)
        self.CelebrationFilter.setObjectName("CelebrationFilter")
        self.verticalLayout_3.addWidget(self.CelebrationFilter)
        self.gpSideEventFilter = QtGui.QCheckBox(self.eventFrame)
        self.gpSideEventFilter.setChecked(True)
        self.gpSideEventFilter.setObjectName("gpSideEventFilter")
        self.verticalLayout_3.addWidget(self.gpSideEventFilter)
        self.otherEventFilter = QtGui.QCheckBox(self.eventFrame)
        self.otherEventFilter.setChecked(True)
        self.otherEventFilter.setObjectName("otherEventFilter")
        self.verticalLayout_3.addWidget(self.otherEventFilter)
        self.horizontalLayout_4.addWidget(self.eventFrame)
        self.datesFrame = QtGui.QFrame(self.frame)
        self.datesFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.datesFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.datesFrame.setObjectName("datesFrame")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.datesFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.datesLabel = QtGui.QLabel(self.datesFrame)
        self.datesLabel.setObjectName("datesLabel")
        self.verticalLayout_4.addWidget(self.datesLabel)
        self.startingDate = QtGui.QCalendarWidget(self.datesFrame)
        self.startingDate.setSelectedDate(QtCore.QDate(1991, 1, 1))
        self.startingDate.setMinimumDate(QtCore.QDate(1991, 1, 1))
        self.startingDate.setObjectName("startingDate")
        self.verticalLayout_4.addWidget(self.startingDate)
        self.label_2 = QtGui.QLabel(self.datesFrame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.endingDate = QtGui.QCalendarWidget(self.datesFrame)
        self.endingDate.setSelectedDate(QtCore.QDate(2015, 12, 31))
        self.endingDate.setMinimumDate(QtCore.QDate(1991, 1, 1))
        self.endingDate.setObjectName("endingDate")
        self.verticalLayout_4.addWidget(self.endingDate)
        self.horizontalLayout_4.addWidget(self.datesFrame)
        self.verticalLayout_5.addWidget(self.frame)
        self.updateFilters = QtGui.QPushButton(self.filtersTab)
        self.updateFilters.setObjectName("updateFilters")
        self.verticalLayout_5.addWidget(self.updateFilters)
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
        self.formatLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Formats:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.standardFilter.setText(QtGui.QApplication.translate("MainWindow", "Standard", None, QtGui.QApplication.UnicodeUTF8))
        self.modernFilter.setText(QtGui.QApplication.translate("MainWindow", "Modern", None, QtGui.QApplication.UnicodeUTF8))
        self.legacyFilter.setText(QtGui.QApplication.translate("MainWindow", "Legacy", None, QtGui.QApplication.UnicodeUTF8))
        self.vintageFilter.setText(QtGui.QApplication.translate("MainWindow", "Vintage", None, QtGui.QApplication.UnicodeUTF8))
        self.boosterDraftFilter.setText(QtGui.QApplication.translate("MainWindow", "Booster Draft", None, QtGui.QApplication.UnicodeUTF8))
        self.sealedFilter.setText(QtGui.QApplication.translate("MainWindow", "Sealed", None, QtGui.QApplication.UnicodeUTF8))
        self.twoHGSealedFilter.setText(QtGui.QApplication.translate("MainWindow", "2 HG Sealed", None, QtGui.QApplication.UnicodeUTF8))
        self.casualFilter.setText(QtGui.QApplication.translate("MainWindow", "Casual", None, QtGui.QApplication.UnicodeUTF8))
        self.otherFormatFilter.setText(QtGui.QApplication.translate("MainWindow", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.eventLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Event Types:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.premiumTournamentFilter.setText(QtGui.QApplication.translate("MainWindow", "Premium Tournament", None, QtGui.QApplication.UnicodeUTF8))
        self.grandPrixFilter.setText(QtGui.QApplication.translate("MainWindow", "Grand Prix", None, QtGui.QApplication.UnicodeUTF8))
        self.proTourFilter.setText(QtGui.QApplication.translate("MainWindow", "Pro Tour", None, QtGui.QApplication.UnicodeUTF8))
        self.PTQFilter.setText(QtGui.QApplication.translate("MainWindow", "Pro Tour Qualifier", None, QtGui.QApplication.UnicodeUTF8))
        self.gameDayFilter.setText(QtGui.QApplication.translate("MainWindow", "Game Day", None, QtGui.QApplication.UnicodeUTF8))
        self.prereleaseFilter.setText(QtGui.QApplication.translate("MainWindow", "Prerelease", None, QtGui.QApplication.UnicodeUTF8))
        self.tournamentFilter.setText(QtGui.QApplication.translate("MainWindow", "Tournament", None, QtGui.QApplication.UnicodeUTF8))
        self.GPTFilter.setText(QtGui.QApplication.translate("MainWindow", "Grand Prix Trial", None, QtGui.QApplication.UnicodeUTF8))
        self.FNMFilter.setText(QtGui.QApplication.translate("MainWindow", "Friday Night Magic", None, QtGui.QApplication.UnicodeUTF8))
        self.WMCQFilter.setText(QtGui.QApplication.translate("MainWindow", "WMCQ", None, QtGui.QApplication.UnicodeUTF8))
        self.EightManFilter.setText(QtGui.QApplication.translate("MainWindow", "8 players Side Events", None, QtGui.QApplication.UnicodeUTF8))
        self.CelebrationFilter.setText(QtGui.QApplication.translate("MainWindow", "Magic Celebration", None, QtGui.QApplication.UnicodeUTF8))
        self.gpSideEventFilter.setText(QtGui.QApplication.translate("MainWindow", "GP Side Event", None, QtGui.QApplication.UnicodeUTF8))
        self.otherEventFilter.setText(QtGui.QApplication.translate("MainWindow", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.datesLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Starting Date:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Ending Date:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.updateFilters.setText(QtGui.QApplication.translate("MainWindow", "Apply Filters", None, QtGui.QApplication.UnicodeUTF8))
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

