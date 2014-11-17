# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/Help.ui'
#
# Created: Mon Nov 17 14:40:31 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(704, 283)
        self.verticalLayout = QtGui.QVBoxLayout(Help)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Help)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.closeButton = QtGui.QPushButton(Help)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        Help.setWindowTitle(QtGui.QApplication.translate("Help", "Qute Help", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Segoe UI,Arial,freesans,sans-serif\'; font-size:16pt; font-weight:600; color:#333333;\">Getting  Started:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Helvetica Neue,Helvetica,Segoe UI,Arial,freesans,sans-serif\'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Make sure you are logged into your Wizard\'s account <a href=\"http://www.wizards.com/magic/planeswalkerpoints\"><span style=\" text-decoration: underline; color:#0057ae;\">here</span></a> in <a href=\"http://www.google.com/chrome/\"><span style=\" text-decoration: underline; color:#0057ae;\">Google Chrome</span></a>.</li>\n"
"<li style=\" font-family:\'Helvetica Neue,Helvetica,Segoe UI,Arial,freesans,sans-serif\'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open <a href=\"https://www.wizards.com/Magic/PlaneswalkerPoints/History#type=EventsOnly\"><span style=\" text-decoration: underline; color:#0057ae;\">this link</span></a>.</li>\n"
"<li style=\" font-family:\'Helvetica Neue,Helvetica,Segoe UI,Arial,freesans,sans-serif\'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press <span style=\" font-style:italic;\">ctrl+shift+j</span></li>\n"
"<li style=\" font-family:\'Helvetica Neue,Helvetica,Segoe UI,Arial,freesans,sans-serif\'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In the console that opens run the command: <span style=\" font-weight:600;\">$(&quot;a.Expand&quot;).click()</span></li>\n"
"<li style=\" font-family:\'Helvetica Neue,Helvetica,Segoe UI,Arial,freesans,sans-serif\'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Make sure you gave the previous command enough time to run! It takes a minute.</li>\n"
"<li style=\" font-family:\'Helvetica Neue,Helvetica,Segoe UI,Arial,freesans,sans-serif\'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press <span style=\" font-style:italic;\">ctrl+a</span> to select the data followed by <span style=\" font-style:italic;\">ctrl+c</span> to copy the data</li>\n"
"<li style=\" font-family:\'Helvetica Neue,Helvetica,Segoe UI,Arial,freesans,sans-serif\'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the <span style=\" font-weight:600;\">Paste Data</span> button on the main window</li>\n"
"<li style=\" font-family:\'Helvetica Neue,Helvetica,Segoe UI,Arial,freesans,sans-serif\'; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Paste the data into the window that opens</li>\n"
"<li style=\" font-family:\'Helvetica Neue,Helvetica,Segoe UI,Arial,freesans,sans-serif\'; color:#333333;\" style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press Prase Data and Enjoy!</li></ul></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Help", "Done", None, QtGui.QApplication.UnicodeUTF8))

