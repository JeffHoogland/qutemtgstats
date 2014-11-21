# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/Calendar.ui'
#
# Created: Fri Nov 21 09:38:52 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.resize(547, 338)
        self.verticalLayout = QtGui.QVBoxLayout(Calendar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtGui.QCalendarWidget(Calendar)
        self.calendarWidget.setMinimumDate(QtCore.QDate(1991, 1, 1))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.buttonFrame = QtGui.QFrame(Calendar)
        self.buttonFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.buttonFrame.setObjectName("buttonFrame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.buttonFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectButton = QtGui.QPushButton(self.buttonFrame)
        self.selectButton.setObjectName("selectButton")
        self.horizontalLayout.addWidget(self.selectButton)
        self.closeButton = QtGui.QPushButton(self.buttonFrame)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addWidget(self.buttonFrame)

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        Calendar.setWindowTitle(QtGui.QApplication.translate("Calendar", "Qute Date Selector", None, QtGui.QApplication.UnicodeUTF8))
        self.selectButton.setText(QtGui.QApplication.translate("Calendar", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Calendar", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

