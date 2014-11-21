import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Calendar import Ui_Calendar

class CalendarWindow(QDialog, Ui_Calendar):
    def __init__(self, parent, btn, typ):
        super(EventWindow, self).__init__(parent)
        self.rent = parent
        self.button = btn
        self.typ = typ.lower()
        
        self.setupUi(self)
        self.assignWidgets()
        
        self.setWindowTitle(unicode("%s Date Select"%typ))
        
    def closePressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.saveChangesButton.clicked.connect(self.savePressed)
        self.closeButton.clicked.connect(self.closePressed)
