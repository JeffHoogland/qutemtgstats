# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/EventStats.ui'
#
# Created: Wed May  6 12:22:53 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EventStats(object):
    def setupUi(self, EventStats):
        EventStats.setObjectName("EventStats")
        EventStats.resize(400, 350)
        self.verticalLayout = QtGui.QVBoxLayout(EventStats)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(EventStats)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 273))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.frame = QtGui.QFrame(EventStats)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exportStatsButton = QtGui.QPushButton(self.frame)
        self.exportStatsButton.setObjectName("exportStatsButton")
        self.horizontalLayout.addWidget(self.exportStatsButton)
        self.adjustFiltersButton = QtGui.QPushButton(self.frame)
        self.adjustFiltersButton.setEnabled(True)
        self.adjustFiltersButton.setObjectName("adjustFiltersButton")
        self.horizontalLayout.addWidget(self.adjustFiltersButton)
        self.cancelButton = QtGui.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(EventStats)
        QtCore.QMetaObject.connectSlotsByName(EventStats)

    def retranslateUi(self, EventStats):
        EventStats.setWindowTitle(QtGui.QApplication.translate("EventStats", "Qute Event Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.exportStatsButton.setText(QtGui.QApplication.translate("EventStats", "Export Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.adjustFiltersButton.setText(QtGui.QApplication.translate("EventStats", "Adjust Filters", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("EventStats", "Done", None, QtGui.QApplication.UnicodeUTF8))

