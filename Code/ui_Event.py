# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/Event.ui'
#
# Created: Fri Nov 21 09:38:52 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Event(object):
    def setupUi(self, Event):
        Event.setObjectName("Event")
        Event.resize(980, 486)
        self.verticalLayout = QtGui.QVBoxLayout(Event)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_8 = QtGui.QFrame(Event)
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.scrollArea = QtGui.QScrollArea(self.frame_8)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 446, 445))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.eventTypeText = QtGui.QLineEdit(self.frame_2)
        self.eventTypeText.setObjectName("eventTypeText")
        self.horizontalLayout.addWidget(self.eventTypeText)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.locationText = QtGui.QLineEdit(self.frame)
        self.locationText.setObjectName("locationText")
        self.horizontalLayout_2.addWidget(self.locationText)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.playersText = QtGui.QLineEdit(self.frame_3)
        self.playersText.setObjectName("playersText")
        self.horizontalLayout_3.addWidget(self.playersText)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.formatText = QtGui.QLineEdit(self.frame_4)
        self.formatText.setObjectName("formatText")
        self.horizontalLayout_4.addWidget(self.formatText)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtGui.QLabel(self.frame_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.placeText = QtGui.QLineEdit(self.frame_5)
        self.placeText.setObjectName("placeText")
        self.horizontalLayout_5.addWidget(self.placeText)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtGui.QLabel(self.frame_6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.dateText = QtGui.QLineEdit(self.frame_6)
        self.dateText.setObjectName("dateText")
        self.horizontalLayout_6.addWidget(self.dateText)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtGui.QLabel(self.frame_7)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.resultsTree = QtGui.QTreeWidget(self.frame_7)
        self.resultsTree.setObjectName("resultsTree")
        self.horizontalLayout_7.addWidget(self.resultsTree)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_8.addWidget(self.scrollArea)
        self.frame_12 = QtGui.QFrame(self.frame_8)
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_9 = QtGui.QFrame(self.frame_12)
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtGui.QLabel(self.frame_9)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.deckText = QtGui.QLineEdit(self.frame_9)
        self.deckText.setObjectName("deckText")
        self.horizontalLayout_9.addWidget(self.deckText)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_10 = QtGui.QFrame(self.frame_12)
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtGui.QLabel(self.frame_10)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.notesText = QtGui.QPlainTextEdit(self.frame_10)
        self.notesText.setMinimumSize(QtCore.QSize(0, 59))
        self.notesText.setObjectName("notesText")
        self.horizontalLayout_10.addWidget(self.notesText)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.horizontalLayout_8.addWidget(self.frame_12)
        self.verticalLayout.addWidget(self.frame_8)
        self.roundTree = QtGui.QTreeWidget(Event)
        self.roundTree.setObjectName("roundTree")
        self.verticalLayout.addWidget(self.roundTree)
        self.frame_11 = QtGui.QFrame(Event)
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.saveChangesButton = QtGui.QPushButton(self.frame_11)
        self.saveChangesButton.setObjectName("saveChangesButton")
        self.horizontalLayout_11.addWidget(self.saveChangesButton)
        self.closeButton = QtGui.QPushButton(self.frame_11)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_11.addWidget(self.closeButton)
        self.verticalLayout.addWidget(self.frame_11)

        self.retranslateUi(Event)
        QtCore.QMetaObject.connectSlotsByName(Event)

    def retranslateUi(self, Event):
        Event.setWindowTitle(QtGui.QApplication.translate("Event", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Event", "<html><head/><body><p><span style=\" font-size:16pt;\">Event Type:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Event", "<html><head/><body><p><span style=\" font-size:16pt;\">Location:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Event", "<html><head/><body><p><span style=\" font-size:16pt;\">Player Count:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Event", "<html><head/><body><p><span style=\" font-size:16pt;\">Format:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Event", "<html><head/><body><p><span style=\" font-size:16pt;\">Final Place:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Event", "<html><head/><body><p><span style=\" font-size:16pt;\">Date:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Event", "<html><head/><body><p><span style=\" font-size:16pt;\">Match Results:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTree.headerItem().setText(0, QtGui.QApplication.translate("Event", "Wins", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTree.headerItem().setText(1, QtGui.QApplication.translate("Event", "Losses", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTree.headerItem().setText(2, QtGui.QApplication.translate("Event", "Draws", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTree.headerItem().setText(3, QtGui.QApplication.translate("Event", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Event", "<html><head/><body><p><span style=\" font-size:16pt;\">Your Deck:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Event", "<html><head/><body><p><span style=\" font-size:16pt;\">Notes:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.roundTree.headerItem().setText(0, QtGui.QApplication.translate("Event", "Round", None, QtGui.QApplication.UnicodeUTF8))
        self.roundTree.headerItem().setText(1, QtGui.QApplication.translate("Event", "Opponent", None, QtGui.QApplication.UnicodeUTF8))
        self.roundTree.headerItem().setText(2, QtGui.QApplication.translate("Event", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.roundTree.headerItem().setText(3, QtGui.QApplication.translate("Event", "Deck", None, QtGui.QApplication.UnicodeUTF8))
        self.saveChangesButton.setText(QtGui.QApplication.translate("Event", "Save Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Event", "Close", None, QtGui.QApplication.UnicodeUTF8))

