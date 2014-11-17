# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/EventList.ui'
#
# Created: Mon Nov 17 13:38:21 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EventList(object):
    def setupUi(self, EventList):
        EventList.setObjectName("EventList")
        EventList.resize(401, 301)
        self.verticalLayout = QtGui.QVBoxLayout(EventList)
        self.verticalLayout.setObjectName("verticalLayout")
        self.eventListLabel = QtGui.QLabel(EventList)
        self.eventListLabel.setObjectName("eventListLabel")
        self.verticalLayout.addWidget(self.eventListLabel)
        self.eventTree = QtGui.QTreeWidget(EventList)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventTree.sizePolicy().hasHeightForWidth())
        self.eventTree.setSizePolicy(sizePolicy)
        self.eventTree.setAutoFillBackground(False)
        self.eventTree.setObjectName("eventTree")
        self.verticalLayout.addWidget(self.eventTree)
        self.buttonFrame = QtGui.QFrame(EventList)
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

        self.retranslateUi(EventList)
        QtCore.QMetaObject.connectSlotsByName(EventList)

    def retranslateUi(self, EventList):
        EventList.setWindowTitle(QtGui.QApplication.translate("EventList", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.eventListLabel.setText(QtGui.QApplication.translate("EventList", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Select an Event to Add/Edit Data</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(0, QtGui.QApplication.translate("EventList", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(1, QtGui.QApplication.translate("EventList", "Place", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(2, QtGui.QApplication.translate("EventList", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(3, QtGui.QApplication.translate("EventList", "Players", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(4, QtGui.QApplication.translate("EventList", "Format", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(5, QtGui.QApplication.translate("EventList", "Location", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(6, QtGui.QApplication.translate("EventList", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(7, QtGui.QApplication.translate("EventList", "Deck", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(8, QtGui.QApplication.translate("EventList", "Wins", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(9, QtGui.QApplication.translate("EventList", "Losses", None, QtGui.QApplication.UnicodeUTF8))
        self.eventTree.headerItem().setText(10, QtGui.QApplication.translate("EventList", "Draws", None, QtGui.QApplication.UnicodeUTF8))
        self.exportStatsButton.setText(QtGui.QApplication.translate("EventList", "Save to CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("EventList", "Done", None, QtGui.QApplication.UnicodeUTF8))

