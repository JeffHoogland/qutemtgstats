import sys
import os
import platform
import datetime
import cPickle as pickle

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Main import Ui_MainWindow

#Dialog windows broken out into seperate files to manage things easier
from ExportStatsWindow import ExportStatsWindow
from PasteWindow import PasteWindow
from HelpWindow import HelpWindow
from FiltersWindow import FiltersWindow
from EventStatsWindow import EventStatsWindow
from DeckStatsWindow import DeckStatsWindow
from FormatStatsWindow import FormatStatsWindow
from EventListWindow import EventListWindow
from OpponentListWindow import OpponentListWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.dataLoaded = False
        self.setupUi(self)
        
        #Create our sub-window objects
        self.exportWindow = ExportStatsWindow( self )
        self.pasteWindow = PasteWindow( self )
        self.helpWindow = HelpWindow( self )
        self.eventStatsWindow = EventStatsWindow( self )
        self.formatStatsWindow = FormatStatsWindow( self )
        self.deckStatsWindow = DeckStatsWindow( self )
        self.eventListWindow = EventListWindow( self )
        self.opponentListWindow = OpponentListWindow( self )
        self.filtersWindow = FiltersWindow( self )
        
        self.eventData = {}
        self.opponentData = {}
        self.filteredEventData = []
        
        self.statsEvents = {}
        self.statsFormats = {}
        self.statsDecks = {}
        
        self.selectedEvents = [ "Magic Pro Tour",
                                "Magic Pro Tour Qualifier",
                                "World Magic Cup Qualifier",
                                "Magic Grand Prix Trial",
                                "Magic Prerelease",
                                "Magic WPN Premium Tournament",
                                "Magic Game Day",
                                "Magic Grand Prix",
                                "Friday Night Magic",
                                "Other"]
        self.selectedFormats = ["Standard",
                                "Modern",
                                "Legacy",
                                "Vintage",
                                "Booster Draft",
                                "Sealed",
                                "2 HG Sealed",
                                "Casual - Constructed",
                                "Casual - Limited",
                                "Other"]
        self.selectedDecks = []
                                
        self.masterEvents = [   "Magic Pro Tour",
                                "Magic Pro Tour Qualifier",
                                "World Magic Cup Qualifier",
                                "Magic Grand Prix Trial",
                                "Magic Prerelease",
                                "Magic WPN Premium Tournament",
                                "Magic Game Day",
                                "Magic Grand Prix",
                                "Friday Night Magic"]
        self.masterFormats = [  "Standard",
                                "Modern",
                                "Legacy",
                                "Vintage",
                                "Booster Draft",
                                "Sealed",
                                "2 HG Sealed",
                                "Casual - Constructed",
                                "Casual - Limited"]
        self.decksList =    []
                                
        
                                
        self.dates = {  "starting":"1991-01-01",
                        "ending":"2015-12-31" }
        
        self.statsReset()
        self.assignWidgets()
        
    def dataLoadedSuccessful( self, dataDict ):
        self.eventData = dict(self.eventData.items() + dataDict.items())
        self.updateGUI()
        self.dataLoaded = True
        self.adjustFiltersButton.setEnabled(True)
        self.statsFrame.setEnabled(True)
        self.listFrame.setEnabled(True)
        self.saveDataButton.setEnabled(True)
        self.dataLoadedLabel.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-style:italic;">Data Loaded</span></p></body></html>')
        self.messageBox( "Data successfully imported." )
    
    def messageBox( self, ourMessage, ourTitle="Qute Confirm" ):
		msgBox = QMessageBox()
                msgBox.setWindowTitle(ourTitle)
		msgBox.setText(ourMessage)
		msgBox.exec_()
    
    def statsReset( self ):
        for ourEvent in self.selectedEvents:
            self.statsEvents[ourEvent] = {"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0}
        
        for ourFormat in self.selectedFormats:
            self.statsFormats[ourFormat] = {"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0}
        
        for ourDeck in self.decksList:
            self.statsDecks[ourDeck] = {"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0}
		
    def exportStatsPressed( self ):
        self.exportWindow.updateText()
        self.exportWindow.show()
        
    def savePressed( self ):
        filename = QFileDialog.getSaveFileName(self, 'Selection a location to save your data to:', os.getenv('HOME')) #returns (fileName, selectedFilter) 
        self.clearObjects()
        pickle.dump( self.eventData, open( filename[0], "wb" ))
        self.messageBox( "Data successfully saved." )
        
    def loadPressed( self ):
        filename = QFileDialog.getOpenFileName(self, 'Select stored data:', os.getenv('HOME')) #returns (fileName, selectedFilter)
        self.dataLoadedSuccessful(pickle.load( open( filename[0], "rb" )))
        
    def clearObjects( self ):
        for ourEvent in self.eventData:
            if self.eventData[ourEvent]["WindowObject"]:
                self.eventData[ourEvent]["WindowObject"].done(0)
                self.eventData[ourEvent]["WindowObject"] = None
            for i in range(len(self.eventData[ourEvent]["Opponents"])):
                self.eventData[ourEvent]["Opponents"][i][3] = ""
        
    def updateFilteredData( self ):
        self.filteredEventData = []
        self.opponentData = {}
        self.deckCheck()
        self.statsReset()
        
        #Find opponents and events that meet our applied filters
        for eventId in self.eventData:
            if self.checkEvent(self.eventData[eventId]["Type"]) and self.checkFormat(self.eventData[eventId]["Format"]) and self.checkDate(self.eventData[eventId]["Date"]):
                self.filteredEventData.append(eventId)
                ourEvent = self.eventData[eventId]
                ourType = ourEvent["Type"]
                ourFormat = ourEvent["Format"]
                ourDeck = ourEvent["Deck"]
                
                #Add stats data
                for tp in ["Wins", "Losses", "Draws", "Matches"]:
                    self.statsEvents[ourType][tp] += ourEvent[tp]
                    self.statsFormats[ourFormat][tp] += ourEvent[tp]
                    if ourDeck:
                        self.statsDecks[ourDeck][tp] += ourEvent[tp]
                
                #Add opponent data
                ourCounter = 0
                for opponent in ourEvent["Opponents"]:
                    self.addMatch( ourEvent["Opponents"][ourCounter][0], ourEvent["Opponents"][ourCounter][1] )
                    ourCounter += 1
        
        #Calculate win %s within the filtered data
        for tp in self.statsEvents:
            if self.statsEvents[tp]["Matches"] > 0:
                self.statsEvents[tp]["Win Percent"] = float(self.statsEvents[tp]["Wins"]) / self.statsEvents[tp]["Matches"] * 100
            
        for tp in self.statsFormats:
            if self.statsFormats[tp]["Matches"] > 0:
                self.statsFormats[tp]["Win Percent"] = float(self.statsFormats[tp]["Wins"]) / self.statsFormats[tp]["Matches"] * 100
        
        for tp in self.statsDecks:
            if self.statsDecks[tp]["Matches"] > 0:
                self.statsDecks[tp]["Win Percent"] = float(self.statsDecks[tp]["Wins"]) / self.statsDecks[tp]["Matches"] * 100
        
    def updateGUI( self ):
        self.updateFilteredData()
        self.eventListWindow.updateGUI()
        self.opponentListWindow.updateGUI()
        self.eventStatsWindow.updateGUI()
        self.formatStatsWindow.updateGUI()
        self.deckStatsWindow.updateGUI()
        
    def deckCheck( self ):
        del self.decksList[:]
        for ourEvent in self.eventData:
            if self.eventData[ourEvent]["Deck"] and self.eventData[ourEvent]["Deck"] not in self.decksList:
                self.decksList.append(self.eventData[ourEvent]["Deck"])
                
        #Hard code selectedDecks to match decksList for now. Maybe add decks to be fiterable later
        self.selectedDecks = self.decksList
        
    def addMatch( self, opponent, result ):
        """opponent is the opponent's name and result should be Win/Loss/Draw"""
        
        if opponent not in self.opponentData:
            self.opponentData[opponent] = {  "Win":0,
                                            "Loss":0,
                                            "Draw":0}
        
        self.opponentData[opponent][result] += 1
        
    def checkDate( self, eventDate ):
        eventDateFormatted = datetime.datetime.strptime(eventDate, "%Y-%m-%d")
        startingDateFormatted = datetime.datetime.strptime(self.dates["starting"], "%Y-%m-%d")
        endingDateFormatted = datetime.datetime.strptime(self.dates["ending"], "%Y-%m-%d")
        
        if eventDateFormatted >= startingDateFormatted and eventDateFormatted <= endingDateFormatted:
            return True
        else:
            return False
        
    def checkEvent( self, eventType ):
        if eventType in self.masterEvents:
            if eventType in self.selectedEvents:
                return True
            else:
                return False
        else:
            if "Other" in self.selectedEvents:
                return True
            else:
                return False
    
    def checkFormat( self, formatType ):
        if formatType in self.masterFormats:
            if formatType in self.selectedFormats:
                return True
            else:
                return False
        else:
            if "Other" in self.selectedFormats:
                return True
            else:
                return False
    
    def assignWidgets( self ):
        self.pasteDataFromSiteButton.clicked.connect(lambda: self.pasteWindow.show())
        self.helpButton.clicked.connect(lambda: self.helpWindow.show())
        self.adjustFiltersButton.clicked.connect(lambda: self.filtersWindow.show())
        self.byFormatButton.clicked.connect(lambda: self.formatStatsWindow.show())
        self.byEventButton.clicked.connect(lambda: self.eventStatsWindow.show())
        self.byDeckButton.clicked.connect(lambda: self.deckStatsWindow.show())
        self.listEventButton.clicked.connect(lambda: self.eventListWindow.show())
        self.listOpponentButton.clicked.connect(lambda: self.opponentListWindow.show())
        self.saveDataButton.clicked.connect(self.savePressed)
        self.loadFromFileButton.clicked.connect(self.loadPressed)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    ret = app.exec_()
