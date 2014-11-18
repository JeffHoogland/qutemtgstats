# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/Paste.ui'
#
# Created: Tue Nov 18 14:23:47 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Paste(object):
    def setupUi(self, Paste):
        Paste.setObjectName("Paste")
        Paste.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Paste)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pasteLabel = QtGui.QLabel(Paste)
        self.pasteLabel.setObjectName("pasteLabel")
        self.verticalLayout.addWidget(self.pasteLabel)
        self.statsPaste = QtGui.QTextEdit(Paste)
        self.statsPaste.setAcceptRichText(False)
        self.statsPaste.setObjectName("statsPaste")
        self.verticalLayout.addWidget(self.statsPaste)
        self.frame = QtGui.QFrame(Paste)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.praseButton = QtGui.QPushButton(self.frame)
        self.praseButton.setObjectName("praseButton")
        self.horizontalLayout.addWidget(self.praseButton)
        self.cancelButton = QtGui.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Paste)
        QtCore.QMetaObject.connectSlotsByName(Paste)

    def retranslateUi(self, Paste):
        Paste.setWindowTitle(QtGui.QApplication.translate("Paste", "Qute Data Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.pasteLabel.setText(QtGui.QApplication.translate("Paste", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Paste Data Below:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.praseButton.setText(QtGui.QApplication.translate("Paste", "Parse Data and Generate Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Paste", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

