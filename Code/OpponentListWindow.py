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

    def updateGUI( self ):
        self.opponentTree.setSortingEnabled(False)
        self.opponentTree.clear()
        for opponent in self.rent.opponentData:
            opponentItem =  TreeWidgetItem(self.opponentTree)
            opponentItem.setText(0, opponent)
            opponentItem.setText(1, unicode(self.rent.opponentData[opponent]["Win"]))
            opponentItem.setText(2, unicode(self.rent.opponentData[opponent]["Loss"]))
            opponentItem.setText(3, unicode(self.rent.opponentData[opponent]["Draw"]))
            opponentItem.setText(4, unicode(self.rent.opponentData[opponent]["Win"]+self.rent.opponentData[opponent]["Loss"]+self.rent.opponentData[opponent]["Draw"]))
            
            self.opponentTree.addTopLevelItem(opponentItem)
        
        self.opponentTree.setSortingEnabled(True)
        self.opponentTree.resizeColumnToContents(0)

    def cancelPressed( self ):
        self.hide()

    def exportStatsPressed( self ):
        pass

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
        self.exportStatsButton.clicked.connect(self.exportStatsPressed)

#Custom object to allow sorting by number and alpha
class TreeWidgetItem( QTreeWidgetItem ):
    def __init__(self, parent=None):
        QTreeWidgetItem.__init__(self, parent)

    def __lt__(self, otherItem):
        column = self.treeWidget().sortColumn()
        try:
            return float( self.text(column) ) > float( otherItem.text(column) )
        except ValueError:
            return self.text(column) > otherItem.text(column)
