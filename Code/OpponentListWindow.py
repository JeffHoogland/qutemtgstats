import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_OpponentList import Ui_OpponentList

class OpponentListWindow(QDialog, Ui_OpponentList):
    def __init__(self, parent):
        super(OpponentListWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.rent = parent

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
