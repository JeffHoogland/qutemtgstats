import os
import csv
import sys

from PySide.QtGui import *
from PySide.QtCore import *

from ui_OpponentList import Ui_OpponentList

if sys.version_info >= (3,0):
    from builtins import str as text
else:
    def text( data ):
        return unicode( data )

class OpponentListWindow(QDialog, Ui_OpponentList):
    def __init__(self, parent):
        super(OpponentListWindow, self).__init__(parent)
        self.rent = parent
        self.setupUi(self)
        self.assignWidgets()
        self.csvList = []

    def updateGUI( self ):
        self.opponentTree.setSortingEnabled(False)
        self.opponentTree.clear()
        del self.csvList[:]
        self.csvList.append(["Opponent", "Wins", "Losses", "Draws", "Total"])
        for opponent in self.rent.opponentData:
            opponentItem =  TreeWidgetItem(self.opponentTree)
            opponentItem.setText(0, opponent)
            opponentItem.setText(1, text(self.rent.opponentData[opponent]["Win"]))
            opponentItem.setText(2, text(self.rent.opponentData[opponent]["Loss"]))
            opponentItem.setText(3, text(self.rent.opponentData[opponent]["Draw"]))
            opponentItem.setText(4, text(self.rent.opponentData[opponent]["Win"]+self.rent.opponentData[opponent]["Loss"]+self.rent.opponentData[opponent]["Draw"]))
            
            self.opponentTree.addTopLevelItem(opponentItem)
            self.csvList.append([opponent, self.rent.opponentData[opponent]["Win"], self.rent.opponentData[opponent]["Loss"],
                                self.rent.opponentData[opponent]["Draw"], self.rent.opponentData[opponent]["Win"]+self.rent.opponentData[opponent]["Loss"]+self.rent.opponentData[opponent]["Draw"]])
        
        self.opponentTree.setSortingEnabled(True)
        self.opponentTree.resizeColumnToContents(0)

    def cancelPressed( self ):
        self.hide()

    def exportStatsPressed( self ):
        filename = QFileDialog.getSaveFileName(self, 'Selection a location to save your data to:', os.getenv('HOME'), 'CSV Files (*.csv)') #returns (fileName, selectedFilter) 
        if filename[0]:
            with open(filename[0], "wb") as f:
                writer = csv.writer(f)
                writer.writerows(self.csvList)

            self.rent.messageBox( "Data exported successfully." )

    def assignWidgets( self ):
        self.adjustFiltersButton.clicked.connect(lambda: self.rent.filtersWindow.show())
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
