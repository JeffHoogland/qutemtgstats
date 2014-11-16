import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_FormatStats import Ui_FormatStats

class FormatStatsWindow(QDialog, Ui_FormatStats):
    def __init__(self, parent):
        super(FormatStatsWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.rent = parent

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
