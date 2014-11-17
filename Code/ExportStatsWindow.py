import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_ExportStats import Ui_ExportStats

class ExportStatsWindow(QDialog, Ui_ExportStats):
    def __init__(self, parent):
        super(ExportStatsWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.rent = parent
        
    def updateText( self ):
        ourText = ""
        
        for ourFormat in self.rent.selectedFormats:
            ourKey = self.rent.statsFormats[ourFormat]
            ourText = "%s%s -"%(ourText, ourFormat)
            ourText = "%s \n \nTotal Record: %s-%s-%s"%(ourText, ourKey['Wins'], ourKey['Losses'], ourKey['Draws'])
            ourText = "%s\nTotal Matches: %s"%(ourText, ourKey['Matches'])
            ourText = "%s\nWin Percent: %.2f\n\n"%(ourText, ourKey['Win Percent'])
        
        for ourType in self.rent.selectedEvents:
            ourKey = self.rent.statsEvents[ourType]
            ourText = "%s%s -"%(ourText, ourType)
            ourText = "%s \n \nTotal Record: %s-%s-%s"%(ourText, ourKey['Wins'], ourKey['Losses'], ourKey['Draws'])
            ourText = "%s\nTotal Matches: %s"%(ourText, ourKey['Matches'])
            ourText = "%s\nWin Percent: %.2f\n\n"%(ourText, ourKey['Win Percent'])

        for ourDeck in self.rent.selectedDecks:
            ourKey = self.rent.statsDecks[ourDeck]
            ourText = "%s%s -"%(ourText, ourDeck)
            ourText = "%s \n \nTotal Record: %s-%s-%s"%(ourText, ourKey['Wins'], ourKey['Losses'], ourKey['Draws'])
            ourText = "%s\nTotal Matches: %s"%(ourText, ourKey['Matches'])
            ourText = "%s\nWin Percent: %.2f\n\n"%(ourText, ourKey['Win Percent'])
            
        self.statsText.setPlainText(ourText)
        
    def savePressed( self ):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'), 'Text Files (*.txt)') #returns (fileName, selectedFilter) 
        f = open(filename[0], 'w') 
        filedata = self.statsText.toPlainText() 
        f.write(filedata) 
        f.close()
        
    def copyPressed( self ):
        self.statsText.selectAll()
        self.statsText.copy()
        
    def closePressed( self ):
        self.hide()
        
    def assignWidgets( self ):
        self.saveStatsButton.clicked.connect(self.savePressed)
        self.copyStatsButton.clicked.connect(self.copyPressed)
        self.closeStatsButton.clicked.connect(self.closePressed)

