# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/EventStats.ui'
#
# Created: Tue Nov 18 08:27:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EventStats(object):
    def setupUi(self, EventStats):
        EventStats.setObjectName("EventStats")
        EventStats.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(EventStats)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtGui.QScrollArea(EventStats)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1266, 206))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.proTourFrame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.proTourFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.proTourFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.proTourFrame.setObjectName("proTourFrame")
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.proTourFrame)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_24 = QtGui.QLabel(self.proTourFrame)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_20.addWidget(self.label_24)
        self.proTourRecord = QtGui.QLabel(self.proTourFrame)
        self.proTourRecord.setObjectName("proTourRecord")
        self.verticalLayout_20.addWidget(self.proTourRecord)
        self.proTourMatches = QtGui.QLabel(self.proTourFrame)
        self.proTourMatches.setObjectName("proTourMatches")
        self.verticalLayout_20.addWidget(self.proTourMatches)
        self.proTourWinPercent = QtGui.QLabel(self.proTourFrame)
        self.proTourWinPercent.setObjectName("proTourWinPercent")
        self.verticalLayout_20.addWidget(self.proTourWinPercent)
        self.horizontalLayout_6.addWidget(self.proTourFrame)
        self.grandPrixFrame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.grandPrixFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.grandPrixFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.grandPrixFrame.setObjectName("grandPrixFrame")
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.grandPrixFrame)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_8 = QtGui.QLabel(self.grandPrixFrame)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_17.addWidget(self.label_8)
        self.grandPrixRecord = QtGui.QLabel(self.grandPrixFrame)
        self.grandPrixRecord.setObjectName("grandPrixRecord")
        self.verticalLayout_17.addWidget(self.grandPrixRecord)
        self.grandPrixMatches = QtGui.QLabel(self.grandPrixFrame)
        self.grandPrixMatches.setObjectName("grandPrixMatches")
        self.verticalLayout_17.addWidget(self.grandPrixMatches)
        self.grandPrixWinPercent = QtGui.QLabel(self.grandPrixFrame)
        self.grandPrixWinPercent.setObjectName("grandPrixWinPercent")
        self.verticalLayout_17.addWidget(self.grandPrixWinPercent)
        self.horizontalLayout_6.addWidget(self.grandPrixFrame)
        self.premiumFrame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.premiumFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.premiumFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.premiumFrame.setObjectName("premiumFrame")
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.premiumFrame)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_9 = QtGui.QLabel(self.premiumFrame)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_18.addWidget(self.label_9)
        self.premiumRecord = QtGui.QLabel(self.premiumFrame)
        self.premiumRecord.setObjectName("premiumRecord")
        self.verticalLayout_18.addWidget(self.premiumRecord)
        self.premiumMatches = QtGui.QLabel(self.premiumFrame)
        self.premiumMatches.setObjectName("premiumMatches")
        self.verticalLayout_18.addWidget(self.premiumMatches)
        self.premiumWinPercent = QtGui.QLabel(self.premiumFrame)
        self.premiumWinPercent.setObjectName("premiumWinPercent")
        self.verticalLayout_18.addWidget(self.premiumWinPercent)
        self.horizontalLayout_6.addWidget(self.premiumFrame)
        self.ptqFrame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.ptqFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ptqFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.ptqFrame.setObjectName("ptqFrame")
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.ptqFrame)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_10 = QtGui.QLabel(self.ptqFrame)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_19.addWidget(self.label_10)
        self.ptqRecord = QtGui.QLabel(self.ptqFrame)
        self.ptqRecord.setObjectName("ptqRecord")
        self.verticalLayout_19.addWidget(self.ptqRecord)
        self.ptqMatches = QtGui.QLabel(self.ptqFrame)
        self.ptqMatches.setObjectName("ptqMatches")
        self.verticalLayout_19.addWidget(self.ptqMatches)
        self.ptqWinPercent = QtGui.QLabel(self.ptqFrame)
        self.ptqWinPercent.setObjectName("ptqWinPercent")
        self.verticalLayout_19.addWidget(self.ptqWinPercent)
        self.horizontalLayout_6.addWidget(self.ptqFrame)
        self.wmcqFrame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.wmcqFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.wmcqFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.wmcqFrame.setObjectName("wmcqFrame")
        self.verticalLayout_24 = QtGui.QVBoxLayout(self.wmcqFrame)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_32 = QtGui.QLabel(self.wmcqFrame)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_24.addWidget(self.label_32)
        self.wmcqRecord = QtGui.QLabel(self.wmcqFrame)
        self.wmcqRecord.setObjectName("wmcqRecord")
        self.verticalLayout_24.addWidget(self.wmcqRecord)
        self.wmcqMatches = QtGui.QLabel(self.wmcqFrame)
        self.wmcqMatches.setObjectName("wmcqMatches")
        self.verticalLayout_24.addWidget(self.wmcqMatches)
        self.wmcqWinPercent = QtGui.QLabel(self.wmcqFrame)
        self.wmcqWinPercent.setObjectName("wmcqWinPercent")
        self.verticalLayout_24.addWidget(self.wmcqWinPercent)
        self.horizontalLayout_6.addWidget(self.wmcqFrame)
        self.gptFrame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.gptFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.gptFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.gptFrame.setObjectName("gptFrame")
        self.verticalLayout_22 = QtGui.QVBoxLayout(self.gptFrame)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_12 = QtGui.QLabel(self.gptFrame)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_22.addWidget(self.label_12)
        self.gptRecord = QtGui.QLabel(self.gptFrame)
        self.gptRecord.setObjectName("gptRecord")
        self.verticalLayout_22.addWidget(self.gptRecord)
        self.gptMatches = QtGui.QLabel(self.gptFrame)
        self.gptMatches.setObjectName("gptMatches")
        self.verticalLayout_22.addWidget(self.gptMatches)
        self.gptWinPercent = QtGui.QLabel(self.gptFrame)
        self.gptWinPercent.setObjectName("gptWinPercent")
        self.verticalLayout_22.addWidget(self.gptWinPercent)
        self.horizontalLayout_6.addWidget(self.gptFrame)
        self.fnmFrame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.fnmFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fnmFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.fnmFrame.setObjectName("fnmFrame")
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.fnmFrame)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_11 = QtGui.QLabel(self.fnmFrame)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_21.addWidget(self.label_11)
        self.fnmRecord = QtGui.QLabel(self.fnmFrame)
        self.fnmRecord.setObjectName("fnmRecord")
        self.verticalLayout_21.addWidget(self.fnmRecord)
        self.fnmMatches = QtGui.QLabel(self.fnmFrame)
        self.fnmMatches.setObjectName("fnmMatches")
        self.verticalLayout_21.addWidget(self.fnmMatches)
        self.fnmWinPercent = QtGui.QLabel(self.fnmFrame)
        self.fnmWinPercent.setObjectName("fnmWinPercent")
        self.verticalLayout_21.addWidget(self.fnmWinPercent)
        self.horizontalLayout_6.addWidget(self.fnmFrame)
        self.prereleaseFrame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.prereleaseFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prereleaseFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.prereleaseFrame.setObjectName("prereleaseFrame")
        self.verticalLayout_23 = QtGui.QVBoxLayout(self.prereleaseFrame)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_28 = QtGui.QLabel(self.prereleaseFrame)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_23.addWidget(self.label_28)
        self.prereleaseRecord = QtGui.QLabel(self.prereleaseFrame)
        self.prereleaseRecord.setObjectName("prereleaseRecord")
        self.verticalLayout_23.addWidget(self.prereleaseRecord)
        self.prereleaseMatches = QtGui.QLabel(self.prereleaseFrame)
        self.prereleaseMatches.setObjectName("prereleaseMatches")
        self.verticalLayout_23.addWidget(self.prereleaseMatches)
        self.prereleaseWinPercent = QtGui.QLabel(self.prereleaseFrame)
        self.prereleaseWinPercent.setObjectName("prereleaseWinPercent")
        self.verticalLayout_23.addWidget(self.prereleaseWinPercent)
        self.horizontalLayout_6.addWidget(self.prereleaseFrame)
        self.gameDayFrame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.gameDayFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.gameDayFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.gameDayFrame.setObjectName("gameDayFrame")
        self.verticalLayout_25 = QtGui.QVBoxLayout(self.gameDayFrame)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_40 = QtGui.QLabel(self.gameDayFrame)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_25.addWidget(self.label_40)
        self.gameDayRecord = QtGui.QLabel(self.gameDayFrame)
        self.gameDayRecord.setObjectName("gameDayRecord")
        self.verticalLayout_25.addWidget(self.gameDayRecord)
        self.gameDayMatches = QtGui.QLabel(self.gameDayFrame)
        self.gameDayMatches.setObjectName("gameDayMatches")
        self.verticalLayout_25.addWidget(self.gameDayMatches)
        self.gameDayWinPercent = QtGui.QLabel(self.gameDayFrame)
        self.gameDayWinPercent.setObjectName("gameDayWinPercent")
        self.verticalLayout_25.addWidget(self.gameDayWinPercent)
        self.horizontalLayout_6.addWidget(self.gameDayFrame)
        self.otherEventFrame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.otherEventFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.otherEventFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.otherEventFrame.setObjectName("otherEventFrame")
        self.verticalLayout_26 = QtGui.QVBoxLayout(self.otherEventFrame)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_36 = QtGui.QLabel(self.otherEventFrame)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_26.addWidget(self.label_36)
        self.otherEventRecord = QtGui.QLabel(self.otherEventFrame)
        self.otherEventRecord.setObjectName("otherEventRecord")
        self.verticalLayout_26.addWidget(self.otherEventRecord)
        self.otherEventMatches = QtGui.QLabel(self.otherEventFrame)
        self.otherEventMatches.setObjectName("otherEventMatches")
        self.verticalLayout_26.addWidget(self.otherEventMatches)
        self.otherEventWinPercent = QtGui.QLabel(self.otherEventFrame)
        self.otherEventWinPercent.setObjectName("otherEventWinPercent")
        self.verticalLayout_26.addWidget(self.otherEventWinPercent)
        self.horizontalLayout_6.addWidget(self.otherEventFrame)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.frame = QtGui.QFrame(EventStats)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exportStatsButton = QtGui.QPushButton(self.frame)
        self.exportStatsButton.setObjectName("exportStatsButton")
        self.horizontalLayout.addWidget(self.exportStatsButton)
        self.cancelButton = QtGui.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(EventStats)
        QtCore.QMetaObject.connectSlotsByName(EventStats)

    def retranslateUi(self, EventStats):
        EventStats.setWindowTitle(QtGui.QApplication.translate("EventStats", "Qute Event Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Pro Tour:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.proTourRecord.setText(QtGui.QApplication.translate("EventStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.proTourMatches.setText(QtGui.QApplication.translate("EventStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.proTourWinPercent.setText(QtGui.QApplication.translate("EventStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Grand Prix:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.grandPrixRecord.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p>Total Record</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.grandPrixMatches.setText(QtGui.QApplication.translate("EventStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.grandPrixWinPercent.setText(QtGui.QApplication.translate("EventStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Premium Event:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.premiumRecord.setText(QtGui.QApplication.translate("EventStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.premiumMatches.setText(QtGui.QApplication.translate("EventStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.premiumWinPercent.setText(QtGui.QApplication.translate("EventStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">PTQ:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ptqRecord.setText(QtGui.QApplication.translate("EventStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.ptqMatches.setText(QtGui.QApplication.translate("EventStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.ptqWinPercent.setText(QtGui.QApplication.translate("EventStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">WMCQ:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.wmcqRecord.setText(QtGui.QApplication.translate("EventStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.wmcqMatches.setText(QtGui.QApplication.translate("EventStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.wmcqWinPercent.setText(QtGui.QApplication.translate("EventStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">GPT:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.gptRecord.setText(QtGui.QApplication.translate("EventStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.gptMatches.setText(QtGui.QApplication.translate("EventStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.gptWinPercent.setText(QtGui.QApplication.translate("EventStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">FNM:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.fnmRecord.setText(QtGui.QApplication.translate("EventStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.fnmMatches.setText(QtGui.QApplication.translate("EventStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.fnmWinPercent.setText(QtGui.QApplication.translate("EventStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">PreRelease:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.prereleaseRecord.setText(QtGui.QApplication.translate("EventStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.prereleaseMatches.setText(QtGui.QApplication.translate("EventStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.prereleaseWinPercent.setText(QtGui.QApplication.translate("EventStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Game Day:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.gameDayRecord.setText(QtGui.QApplication.translate("EventStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.gameDayMatches.setText(QtGui.QApplication.translate("EventStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.gameDayWinPercent.setText(QtGui.QApplication.translate("EventStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("EventStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Other:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.otherEventRecord.setText(QtGui.QApplication.translate("EventStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.otherEventMatches.setText(QtGui.QApplication.translate("EventStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.otherEventWinPercent.setText(QtGui.QApplication.translate("EventStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.exportStatsButton.setText(QtGui.QApplication.translate("EventStats", "Export Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("EventStats", "Done", None, QtGui.QApplication.UnicodeUTF8))

