import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Help import Ui_Help



class HelpWindow(QDialog, Ui_Help):
    def __init__(self, parent):
        super(HelpWindow, self).__init__(parent)
        self.rent = parent
        self.setupUi(self)
        self.assignWidgets()
        
    def closePressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.closeButton.clicked.connect(self.closePressed)
