import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_EventList import Ui_EventList

class EventListWindow(QDialog, Ui_EventList):
    def __init__(self, parent):
        super(EventListWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.rent = parent

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
