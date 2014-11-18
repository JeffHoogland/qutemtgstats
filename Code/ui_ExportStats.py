# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/ExportStats.ui'
#
# Created: Tue Nov 18 14:23:46 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ExportStats(object):
    def setupUi(self, ExportStats):
        ExportStats.setObjectName("ExportStats")
        ExportStats.resize(569, 365)
        self.verticalLayout = QtGui.QVBoxLayout(ExportStats)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statsText = QtGui.QPlainTextEdit(ExportStats)
        self.statsText.setPlainText("")
        self.statsText.setObjectName("statsText")
        self.verticalLayout.addWidget(self.statsText)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveStatsButton = QtGui.QPushButton(ExportStats)
        self.saveStatsButton.setObjectName("saveStatsButton")
        self.horizontalLayout.addWidget(self.saveStatsButton)
        self.copyStatsButton = QtGui.QPushButton(ExportStats)
        self.copyStatsButton.setObjectName("copyStatsButton")
        self.horizontalLayout.addWidget(self.copyStatsButton)
        self.closeStatsButton = QtGui.QPushButton(ExportStats)
        self.closeStatsButton.setObjectName("closeStatsButton")
        self.horizontalLayout.addWidget(self.closeStatsButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ExportStats)
        QtCore.QMetaObject.connectSlotsByName(ExportStats)

    def retranslateUi(self, ExportStats):
        ExportStats.setWindowTitle(QtGui.QApplication.translate("ExportStats", "Qute Stats Export", None, QtGui.QApplication.UnicodeUTF8))
        self.saveStatsButton.setText(QtGui.QApplication.translate("ExportStats", "Save to File", None, QtGui.QApplication.UnicodeUTF8))
        self.copyStatsButton.setText(QtGui.QApplication.translate("ExportStats", "Copy to Clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.closeStatsButton.setText(QtGui.QApplication.translate("ExportStats", "Close", None, QtGui.QApplication.UnicodeUTF8))

