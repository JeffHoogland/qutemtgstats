# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/FormatStats.ui'
#
# Created: Sun Nov 16 22:11:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FormatStats(object):
    def setupUi(self, FormatStats):
        FormatStats.setObjectName("FormatStats")
        FormatStats.resize(398, 302)
        self.verticalLayout = QtGui.QVBoxLayout(FormatStats)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(FormatStats)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1249, 208))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.standardFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.standardFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.standardFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.standardFrame.setObjectName("standardFrame")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.standardFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtGui.QLabel(self.standardFrame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.standardRecord = QtGui.QLabel(self.standardFrame)
        self.standardRecord.setObjectName("standardRecord")
        self.verticalLayout_7.addWidget(self.standardRecord)
        self.standardMatches = QtGui.QLabel(self.standardFrame)
        self.standardMatches.setObjectName("standardMatches")
        self.verticalLayout_7.addWidget(self.standardMatches)
        self.standardWinPercent = QtGui.QLabel(self.standardFrame)
        self.standardWinPercent.setObjectName("standardWinPercent")
        self.verticalLayout_7.addWidget(self.standardWinPercent)
        self.horizontalLayout_5.addWidget(self.standardFrame)
        self.modernFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.modernFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.modernFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.modernFrame.setObjectName("modernFrame")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.modernFrame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtGui.QLabel(self.modernFrame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.modernRecord = QtGui.QLabel(self.modernFrame)
        self.modernRecord.setObjectName("modernRecord")
        self.verticalLayout_8.addWidget(self.modernRecord)
        self.modernMatches = QtGui.QLabel(self.modernFrame)
        self.modernMatches.setObjectName("modernMatches")
        self.verticalLayout_8.addWidget(self.modernMatches)
        self.modernWinPercent = QtGui.QLabel(self.modernFrame)
        self.modernWinPercent.setObjectName("modernWinPercent")
        self.verticalLayout_8.addWidget(self.modernWinPercent)
        self.horizontalLayout_5.addWidget(self.modernFrame)
        self.legacyFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.legacyFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.legacyFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.legacyFrame.setObjectName("legacyFrame")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.legacyFrame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtGui.QLabel(self.legacyFrame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.legacyRecord = QtGui.QLabel(self.legacyFrame)
        self.legacyRecord.setObjectName("legacyRecord")
        self.verticalLayout_9.addWidget(self.legacyRecord)
        self.legacyMatches = QtGui.QLabel(self.legacyFrame)
        self.legacyMatches.setObjectName("legacyMatches")
        self.verticalLayout_9.addWidget(self.legacyMatches)
        self.legacyWinPercent = QtGui.QLabel(self.legacyFrame)
        self.legacyWinPercent.setObjectName("legacyWinPercent")
        self.verticalLayout_9.addWidget(self.legacyWinPercent)
        self.horizontalLayout_5.addWidget(self.legacyFrame)
        self.vintageFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.vintageFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vintageFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.vintageFrame.setObjectName("vintageFrame")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.vintageFrame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_23 = QtGui.QLabel(self.vintageFrame)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_12.addWidget(self.label_23)
        self.vintageRecord = QtGui.QLabel(self.vintageFrame)
        self.vintageRecord.setObjectName("vintageRecord")
        self.verticalLayout_12.addWidget(self.vintageRecord)
        self.vintageMatches = QtGui.QLabel(self.vintageFrame)
        self.vintageMatches.setObjectName("vintageMatches")
        self.verticalLayout_12.addWidget(self.vintageMatches)
        self.vintageWinPercent = QtGui.QLabel(self.vintageFrame)
        self.vintageWinPercent.setObjectName("vintageWinPercent")
        self.verticalLayout_12.addWidget(self.vintageWinPercent)
        self.horizontalLayout_5.addWidget(self.vintageFrame)
        self.draftFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.draftFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.draftFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.draftFrame.setObjectName("draftFrame")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.draftFrame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtGui.QLabel(self.draftFrame)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.draftRecord = QtGui.QLabel(self.draftFrame)
        self.draftRecord.setObjectName("draftRecord")
        self.verticalLayout_11.addWidget(self.draftRecord)
        self.draftMatches = QtGui.QLabel(self.draftFrame)
        self.draftMatches.setObjectName("draftMatches")
        self.verticalLayout_11.addWidget(self.draftMatches)
        self.draftWinPercent = QtGui.QLabel(self.draftFrame)
        self.draftWinPercent.setObjectName("draftWinPercent")
        self.verticalLayout_11.addWidget(self.draftWinPercent)
        self.horizontalLayout_5.addWidget(self.draftFrame)
        self.sealedFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.sealedFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sealedFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.sealedFrame.setObjectName("sealedFrame")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.sealedFrame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QtGui.QLabel(self.sealedFrame)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.sealedRecord = QtGui.QLabel(self.sealedFrame)
        self.sealedRecord.setObjectName("sealedRecord")
        self.verticalLayout_10.addWidget(self.sealedRecord)
        self.sealedMatches = QtGui.QLabel(self.sealedFrame)
        self.sealedMatches.setObjectName("sealedMatches")
        self.verticalLayout_10.addWidget(self.sealedMatches)
        self.sealedWinPercent = QtGui.QLabel(self.sealedFrame)
        self.sealedWinPercent.setObjectName("sealedWinPercent")
        self.verticalLayout_10.addWidget(self.sealedWinPercent)
        self.horizontalLayout_5.addWidget(self.sealedFrame)
        self.twoHGFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.twoHGFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.twoHGFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.twoHGFrame.setObjectName("twoHGFrame")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.twoHGFrame)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_27 = QtGui.QLabel(self.twoHGFrame)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_13.addWidget(self.label_27)
        self.twoHGRecord = QtGui.QLabel(self.twoHGFrame)
        self.twoHGRecord.setObjectName("twoHGRecord")
        self.verticalLayout_13.addWidget(self.twoHGRecord)
        self.twoHGMatches = QtGui.QLabel(self.twoHGFrame)
        self.twoHGMatches.setObjectName("twoHGMatches")
        self.verticalLayout_13.addWidget(self.twoHGMatches)
        self.twoHGWinPercent = QtGui.QLabel(self.twoHGFrame)
        self.twoHGWinPercent.setObjectName("twoHGWinPercent")
        self.verticalLayout_13.addWidget(self.twoHGWinPercent)
        self.horizontalLayout_5.addWidget(self.twoHGFrame)
        self.casualConFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.casualConFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.casualConFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.casualConFrame.setObjectName("casualConFrame")
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.casualConFrame)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_31 = QtGui.QLabel(self.casualConFrame)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_14.addWidget(self.label_31)
        self.casualConRecord = QtGui.QLabel(self.casualConFrame)
        self.casualConRecord.setObjectName("casualConRecord")
        self.verticalLayout_14.addWidget(self.casualConRecord)
        self.casualConMatches = QtGui.QLabel(self.casualConFrame)
        self.casualConMatches.setObjectName("casualConMatches")
        self.verticalLayout_14.addWidget(self.casualConMatches)
        self.casualConWinPercent = QtGui.QLabel(self.casualConFrame)
        self.casualConWinPercent.setObjectName("casualConWinPercent")
        self.verticalLayout_14.addWidget(self.casualConWinPercent)
        self.horizontalLayout_5.addWidget(self.casualConFrame)
        self.casualLimFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.casualLimFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.casualLimFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.casualLimFrame.setObjectName("casualLimFrame")
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.casualLimFrame)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_39 = QtGui.QLabel(self.casualLimFrame)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_16.addWidget(self.label_39)
        self.casualLimRecord = QtGui.QLabel(self.casualLimFrame)
        self.casualLimRecord.setObjectName("casualLimRecord")
        self.verticalLayout_16.addWidget(self.casualLimRecord)
        self.casualLimMatches = QtGui.QLabel(self.casualLimFrame)
        self.casualLimMatches.setObjectName("casualLimMatches")
        self.verticalLayout_16.addWidget(self.casualLimMatches)
        self.casualLimWinPercent = QtGui.QLabel(self.casualLimFrame)
        self.casualLimWinPercent.setObjectName("casualLimWinPercent")
        self.verticalLayout_16.addWidget(self.casualLimWinPercent)
        self.horizontalLayout_5.addWidget(self.casualLimFrame)
        self.otherFrame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.otherFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.otherFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.otherFrame.setObjectName("otherFrame")
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.otherFrame)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_35 = QtGui.QLabel(self.otherFrame)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_15.addWidget(self.label_35)
        self.otherRecord = QtGui.QLabel(self.otherFrame)
        self.otherRecord.setObjectName("otherRecord")
        self.verticalLayout_15.addWidget(self.otherRecord)
        self.otherMatches = QtGui.QLabel(self.otherFrame)
        self.otherMatches.setObjectName("otherMatches")
        self.verticalLayout_15.addWidget(self.otherMatches)
        self.otherWinPercent = QtGui.QLabel(self.otherFrame)
        self.otherWinPercent.setObjectName("otherWinPercent")
        self.verticalLayout_15.addWidget(self.otherWinPercent)
        self.horizontalLayout_5.addWidget(self.otherFrame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonFrame = QtGui.QFrame(FormatStats)
        self.buttonFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.buttonFrame.setObjectName("buttonFrame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.buttonFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exportStatsButton = QtGui.QPushButton(self.buttonFrame)
        self.exportStatsButton.setObjectName("exportStatsButton")
        self.horizontalLayout.addWidget(self.exportStatsButton)
        self.cancelButton = QtGui.QPushButton(self.buttonFrame)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addWidget(self.buttonFrame)

        self.retranslateUi(FormatStats)
        QtCore.QMetaObject.connectSlotsByName(FormatStats)

    def retranslateUi(self, FormatStats):
        FormatStats.setWindowTitle(QtGui.QApplication.translate("FormatStats", "Qute Format Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Standard:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.standardRecord.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p>Total Record</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.standardMatches.setText(QtGui.QApplication.translate("FormatStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.standardWinPercent.setText(QtGui.QApplication.translate("FormatStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Modern:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.modernRecord.setText(QtGui.QApplication.translate("FormatStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.modernMatches.setText(QtGui.QApplication.translate("FormatStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.modernWinPercent.setText(QtGui.QApplication.translate("FormatStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Legacy:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.legacyRecord.setText(QtGui.QApplication.translate("FormatStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.legacyMatches.setText(QtGui.QApplication.translate("FormatStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.legacyWinPercent.setText(QtGui.QApplication.translate("FormatStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Vintage:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.vintageRecord.setText(QtGui.QApplication.translate("FormatStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.vintageMatches.setText(QtGui.QApplication.translate("FormatStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.vintageWinPercent.setText(QtGui.QApplication.translate("FormatStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Draft:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.draftRecord.setText(QtGui.QApplication.translate("FormatStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.draftMatches.setText(QtGui.QApplication.translate("FormatStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.draftWinPercent.setText(QtGui.QApplication.translate("FormatStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Sealed:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sealedRecord.setText(QtGui.QApplication.translate("FormatStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.sealedMatches.setText(QtGui.QApplication.translate("FormatStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.sealedWinPercent.setText(QtGui.QApplication.translate("FormatStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">2 HG Sealed:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.twoHGRecord.setText(QtGui.QApplication.translate("FormatStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.twoHGMatches.setText(QtGui.QApplication.translate("FormatStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.twoHGWinPercent.setText(QtGui.QApplication.translate("FormatStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Casual - Con:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.casualConRecord.setText(QtGui.QApplication.translate("FormatStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.casualConMatches.setText(QtGui.QApplication.translate("FormatStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.casualConWinPercent.setText(QtGui.QApplication.translate("FormatStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Casual - Lim:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.casualLimRecord.setText(QtGui.QApplication.translate("FormatStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.casualLimMatches.setText(QtGui.QApplication.translate("FormatStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.casualLimWinPercent.setText(QtGui.QApplication.translate("FormatStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("FormatStats", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Other:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.otherRecord.setText(QtGui.QApplication.translate("FormatStats", "Total Record", None, QtGui.QApplication.UnicodeUTF8))
        self.otherMatches.setText(QtGui.QApplication.translate("FormatStats", "Total Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.otherWinPercent.setText(QtGui.QApplication.translate("FormatStats", "Win %", None, QtGui.QApplication.UnicodeUTF8))
        self.exportStatsButton.setText(QtGui.QApplication.translate("FormatStats", "Export Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("FormatStats", "Done", None, QtGui.QApplication.UnicodeUTF8))

