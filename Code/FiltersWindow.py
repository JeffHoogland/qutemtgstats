import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Filters import Ui_Filters

class FiltersWindow(QDialog, Ui_Filters):
    def __init__(self, parent):
        super(FiltersWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.rent = parent

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
