import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_EventStats import Ui_EventStats

class EventStatsWindow(QDialog, Ui_EventStats):
    def __init__(self, parent):
        super(EventStatsWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.rent = parent

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
