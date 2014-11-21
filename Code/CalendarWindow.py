import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Calendar import Ui_Calendar

class CalendarWindow(QDialog, Ui_Calendar):
    def __init__(self, parent, btn, typ ):
        super(CalendarWindow, self).__init__(parent)
        self.rent = parent
        self.button = btn
        self.typ = typ.lower()
        
        self.setupUi(self)
        self.assignWidgets()
        
        self.setWindowTitle(unicode("%s Date Select"%typ))
        
    def selectPressed( self ):
        ourDate = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.button.setText(ourDate)
        self.hide()
        
    def closePressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.selectButton.clicked.connect(self.selectPressed)
        self.closeButton.clicked.connect(self.closePressed)
        
        splitDate = self.button.text().split("-")
        
        self.calendarWidget.setSelectedDate(QDate(int(splitDate[0]), int(splitDate[1]), int(splitDate[2])))
