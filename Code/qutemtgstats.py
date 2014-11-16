import sys
import os
import platform
import datetime

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Main import Ui_MainWindow

#Dialog windows broken out into seperate files to manage things easier
from ExportStatsWindow import ExportStatsWindow
from PasteWindow import PasteWindow
from FiltersWindow import FiltersWindow
from EventStatsWindow import EventStatsWindow
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
        self.eventStatsWindow = EventStatsWindow( self )
        self.formatStatsWindow = FormatStatsWindow( self )
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
        self.deckLists =    []
                                
        
                                
        self.dates = {  "starting":"1991-01-01",
                        "ending":"2015-12-31" }
        
        self.statsReset()
        self.assignWidgets()
        
    def dataLoadedSuccessful( self, dataDict ):
        self.eventData = dataDict
        self.updateFilteredData()
        self.dataLoaded = True
        self.adjustFiltersButton.setEnabled(True)
        self.statsFrame.setEnabled(True)
        self.listFrame.setEnabled(True)
        self.saveDataButton.setEnabled(True)
        self.dataLoadedLabel.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-style:italic;">Data Loaded</span></p></body></html>')
    
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
        
        for ourDeck in self.deckLists:
            self.statsDecks[ourDeck] = {"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0}
		
    def exportStatsPressed( self ):
        self.exportWindow.updateText()
        self.exportWindow.show()
        
    def updateFilteredData( self ):
        self.filteredEventData = []
        self.opponentData = {}
        self.statsReset()
        
        #Find opponents and events that meet our applied filters
        for eventId in self.eventData:
            if self.checkEvent(self.eventData[eventId]["Type"]) and self.checkFormat(self.eventData[eventId]["Format"]) and self.checkDate(self.eventData[eventId]["Date"]):
                self.filteredEventData.append(eventId)
                ourEvent = self.eventData[eventId]
                ourType = ourEvent["Type"]
                ourFormat = ourEvent["Format"]
                
                #Add stats data
                for tp in ["Wins", "Losses", "Draws", "Matches"]:
                    self.statsEvents[ourType][tp] += ourEvent[tp]
                    self.statsFormats[ourFormat][tp] += ourEvent[tp]
                
                #Add opponent data
                for opponent in ourEvent["Opponents"]:
                    self.addMatch( ourEvent["Opponents"][ourEvent["Opponents"].index(opponent)][0], ourEvent["Opponents"][ourEvent["Opponents"].index(opponent)][1] )
        
        #Calculate win %s within the filtered data
        for tp in self.statsEvents:
            if self.statsEvents[tp]["Matches"] > 0:
                self.statsEvents[tp]["Win Percent"] = float(self.statsEvents[tp]["Wins"]) / self.statsEvents[tp]["Matches"] * 100
            
        for tp in self.statsFormats:
            if self.statsFormats[tp]["Matches"] > 0:
                self.statsFormats[tp]["Win Percent"] = float(self.statsFormats[tp]["Wins"]) / self.statsFormats[tp]["Matches"] * 100
        
        self.updateGUI()
        
    def updateGUI( self ):
        self.eventListWindow.updateGUI()
        self.opponentListWindow.updateGUI()
        self.eventStatsWindow.updateGUI()
        self.formatStatsWindow.updateGUI()
        
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
        self.adjustFiltersButton.clicked.connect(lambda: self.filtersWindow.show())
        self.byFormatButton.clicked.connect(lambda: self.formatStatsWindow.show())
        self.byEventButton.clicked.connect(lambda: self.eventStatsWindow.show())
        self.listEventButton.clicked.connect(lambda: self.eventListWindow.show())
        self.listOpponentButton.clicked.connect(lambda: self.opponentListWindow.show())

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
