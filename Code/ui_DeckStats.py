# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/DeckStats.ui'
#
# Created: Mon Nov 17 14:50:54 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DeckStats(object):
    def setupUi(self, DeckStats):
        DeckStats.setObjectName("DeckStats")
        DeckStats.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(DeckStats)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtGui.QScrollArea(DeckStats)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 378, 223))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.frame = QtGui.QFrame(DeckStats)
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

        self.retranslateUi(DeckStats)
        QtCore.QMetaObject.connectSlotsByName(DeckStats)

    def retranslateUi(self, DeckStats):
        DeckStats.setWindowTitle(QtGui.QApplication.translate("DeckStats", "Qute Deck Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.exportStatsButton.setText(QtGui.QApplication.translate("DeckStats", "Export Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("DeckStats", "Done", None, QtGui.QApplication.UnicodeUTF8))

