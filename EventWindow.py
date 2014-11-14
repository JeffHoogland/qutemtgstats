import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Event import Ui_Event

class EventWindow(QDialog, Ui_Event):
    def __init__(self, parent, eventId):
        super(ExportStatsWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        
        self.rent = parent

	def assignWidgets( self ):
		pass
