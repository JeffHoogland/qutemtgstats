# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/OpponentList.ui'
#
# Created: Sun Nov 16 22:11:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_OpponentList(object):
    def setupUi(self, OpponentList):
        OpponentList.setObjectName("OpponentList")
        OpponentList.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(OpponentList)
        self.verticalLayout.setObjectName("verticalLayout")
        self.opponentListLabel = QtGui.QLabel(OpponentList)
        self.opponentListLabel.setObjectName("opponentListLabel")
        self.verticalLayout.addWidget(self.opponentListLabel)
        self.opponentTree = QtGui.QTreeWidget(OpponentList)
        self.opponentTree.setAutoFillBackground(False)
        self.opponentTree.setObjectName("opponentTree")
        self.verticalLayout.addWidget(self.opponentTree)
        self.buttonFrame = QtGui.QFrame(OpponentList)
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

        self.retranslateUi(OpponentList)
        QtCore.QMetaObject.connectSlotsByName(OpponentList)

    def retranslateUi(self, OpponentList):
        OpponentList.setWindowTitle(QtGui.QApplication.translate("OpponentList", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentListLabel.setText(QtGui.QApplication.translate("OpponentList", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Opponents</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentTree.setSortingEnabled(True)
        self.opponentTree.headerItem().setText(0, QtGui.QApplication.translate("OpponentList", "Opponent", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentTree.headerItem().setText(1, QtGui.QApplication.translate("OpponentList", "Wins", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentTree.headerItem().setText(2, QtGui.QApplication.translate("OpponentList", "Losses", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentTree.headerItem().setText(3, QtGui.QApplication.translate("OpponentList", "Draws", None, QtGui.QApplication.UnicodeUTF8))
        self.opponentTree.headerItem().setText(4, QtGui.QApplication.translate("OpponentList", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.exportStatsButton.setText(QtGui.QApplication.translate("OpponentList", "Save to CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("OpponentList", "Done", None, QtGui.QApplication.UnicodeUTF8))

