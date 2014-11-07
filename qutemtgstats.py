#How many lines after the data we find certain data
EventDate = 0
EventType = 1
EventPlayers = 3
EventFormat = 5
EventLocation = 6
EventPlace = 7
EventID = 8
EventHistory = 10

import sys
import os
import platform
import datetime

def isDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.eventData = {}
        self.opponentData = {}
        self.filteredEventData = []
        
        self.selectedEvents = [ "Magic Pro Tour",
                                "Magic Pro Tour Qualifier",
                                "World Magic Cup Qualifier",
                                "8 players Side Events",
                                "Magic Celebration",
                                "Magic Tournament",
                                "Magic Grand Prix Trial",
                                "Magic Casual Event",
                                "Magic Prerelease",
                                "Magic WPN Premium Tournament",
                                "Magic Game Day",
                                "Public Event at Grand Prix",
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
                                
        self.masterEvents = [   "Magic Pro Tour",
                                "Magic Pro Tour Qualifier",
                                "World Magic Cup Qualifier",
                                "8 players Side Events",
                                "Magic Celebration",
                                "Magic Tournament",
                                "Magic Grand Prix Trial",
                                "Magic Casual Event",
                                "Magic Prerelease",
                                "Magic WPN Premium Tournament",
                                "Magic Game Day",
                                "Public Event at Grand Prix",
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
                                
        self.dates = {  "starting":"1991-01-01",
                        "ending":"2015-12-31" }
        
        self.assignWidgets()
    
    def phrasePressed( self ):
        self.rawData = self.statsPaste.toPlainText().split("\n")
        
        self.formatData()
    
    def updateFiltersPressed( self ):
        self.updateFilteredData()
        
    def formatData( self ):
        eventBreaks = []
        numberOfRows = len(self.rawData)
        
        for row in range(numberOfRows):
            if isDate(self.rawData[row-1][:10]):
                eventBreaks.append(row-1)
        
        for event in eventBreaks:
            startingRow = event
            
            if eventBreaks.index(event)+1 < len(eventBreaks):
                endingRow = eventBreaks[eventBreaks.index(event) + 1]
            else:
                endingRow = len(self.rawData)
            
            eventId = self.rawData[startingRow+EventID].split(":")[1].lstrip()
            eventPlace = self.rawData[startingRow+EventPlace].split(":")[1].lstrip()
            eventType = self.rawData[startingRow+EventType].split(":")[1].lstrip()
            eventPlayers = self.rawData[startingRow+EventPlayers].split(":")[1].lstrip()
            eventFormat = self.rawData[startingRow+EventFormat].split(":")[1].lstrip()
            eventLocation = self.rawData[startingRow+EventLocation].split(":")[1].lstrip()
            eventDate = self.rawData[startingRow+EventDate][:10]
            eventOpponents = []
            eventWins = 0
            eventLosses = 0
            eventDraws = 0
            
            for row in range(startingRow+EventHistory, endingRow):
                ourRound = self.rawData[row].split("\t")
                if len(ourRound) == 4:
                    if len(ourRound[3]):
                        if ourRound[1] == "Win":
                            eventOpponents.append([ourRound[3], "Win"])
                            eventWins += 1
                        elif ourRound[1] == "Loss":
                            eventOpponents.append([ourRound[3], "Loss"])
                            eventLosses += 1
                        elif ourRound[1] == "Draw":
                            eventOpponents.append([ourRound[3], "Draw"])
                            eventDraws += 1
                        
            self.eventData[eventId] = { "Place":eventPlace,
                                        "Type":eventType,
                                        "Players":eventPlayers,
                                        "Format":eventFormat,
                                        "Location":eventLocation,
                                        "Date":eventDate,
                                        "Opponents":eventOpponents,
                                        "Wins":eventWins,
                                        "Losses":eventLosses,
                                        "Draws":eventDraws}
                        
        self.updateFilteredData()
        
    def updateFilteredData( self ):
        self.filteredEventData = []
        self.opponentData = {}
        
        for eventId in self.eventData:
            if self.checkEvent(eventId) and self.checkFormat(self.eventData[eventId]["Format"]) and self.checkDate(self.eventData[eventId]["Date"]):
                self.filteredEventData.append(eventId)
                for opponent in self.eventData[eventId]["Opponents"]:
                    self.addMatch( self.eventData[eventId]["Opponents"][self.eventData[eventId]["Opponents"].index(opponent)][0], self.eventData[eventId]["Opponents"][self.eventData[eventId]["Opponents"].index(opponent)][1] )
        
        self.updateGUI()
        
    def updateGUI( self ):
        #Update opponents
        self.opponentTree.setSortingEnabled(False)
        self.opponentTree.clear()
        for opponent in self.opponentData:
            opponentItem =  TreeWidgetItem(self.opponentTree)
            opponentItem.setText(0, opponent)
            opponentItem.setText(1, unicode(self.opponentData[opponent]["Win"]))
            opponentItem.setText(2, unicode(self.opponentData[opponent]["Loss"]))
            opponentItem.setText(3, unicode(self.opponentData[opponent]["Draw"]))
            opponentItem.setText(4, unicode(self.opponentData[opponent]["Win"]+self.opponentData[opponent]["Loss"]+self.opponentData[opponent]["Draw"]))
            
            self.opponentTree.addTopLevelItem(opponentItem)
        
        self.opponentTree.setSortingEnabled(True)
        
        #Update events
        self.eventTree.setSortingEnabled(False)
        self.eventTree.clear()
        for eventId in self.filteredEventData:
            eventItem = TreeWidgetItem(self.eventTree)
            eventItem.setText(0, eventId)
            eventItem.setText(1, unicode(self.eventData[eventId]["Place"]))
            eventItem.setText(2, unicode(self.eventData[eventId]["Type"]))
            eventItem.setText(3, unicode(self.eventData[eventId]["Players"]))
            eventItem.setText(4, unicode(self.eventData[eventId]["Format"]))
            eventItem.setText(5, unicode(self.eventData[eventId]["Location"]))
            eventItem.setText(6, unicode(self.eventData[eventId]["Date"]))
            eventItem.setText(7, unicode(self.eventData[eventId]["Wins"]))
            eventItem.setText(8, unicode(self.eventData[eventId]["Losses"]))
            eventItem.setText(9, unicode(self.eventData[eventId]["Draws"]))
            eventItem.setText(10, unicode(str(self.eventData[eventId]["Opponents"])))
            
            self.eventTree.addTopLevelItem(eventItem)
        
        self.eventTree.setSortingEnabled(True)
        
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
        self.phraseButton.clicked.connect(self.phrasePressed)
        self.updateFiltersButton.clicked.connect(self.updateFiltersPressed)
        
        #Assign our many check boxes for filters
        self.CelebrationFilter.stateChanged.connect(lambda: self.checkChanged(self.CelebrationFilter, "event"))
        self.EightManFilter.stateChanged.connect(lambda: self.checkChanged(self.EightManFilter, "event"))
        self.FNMFilter.stateChanged.connect(lambda: self.checkChanged(self.FNMFilter, "event"))
        self.GPTFilter.stateChanged.connect(lambda: self.checkChanged(self.GPTFilter, "event"))
        self.PTQFilter.stateChanged.connect(lambda: self.checkChanged(self.PTQFilter, "event"))
        self.WMCQFilter.stateChanged.connect(lambda: self.checkChanged(self.WMCQFilter, "event"))
        self.gameDayFilter.stateChanged.connect(lambda: self.checkChanged(self.gameDayFilter, "event"))
        self.gpSideEventFilter.stateChanged.connect(lambda: self.checkChanged(self.gpSideEventFilter, "event"))
        self.grandPrixFilter.stateChanged.connect(lambda: self.checkChanged(self.grandPrixFilter, "event"))
        self.otherEventFilter.stateChanged.connect(lambda: self.checkChanged(self.otherEventFilter, "event"))
        self.premiumTournamentFilter.stateChanged.connect(lambda: self.checkChanged(self.premiumTournamentFilter, "event"))
        self.prereleaseFilter.stateChanged.connect(lambda: self.checkChanged(self.prereleaseFilter, "event"))
        self.proTourFilter.stateChanged.connect(lambda: self.checkChanged(self.proTourFilter, "event"))
        self.tournamentFilter.stateChanged.connect(lambda: self.checkChanged(self.tournamentFilter, "event"))
        
        self.boosterDraftFilter.stateChanged.connect(lambda: self.checkChanged(self.boosterDraftFilter, "format"))
        self.casualConFilter.stateChanged.connect(lambda: self.checkChanged(self.casualConFilter, "format"))
        self.casualLimFilter.stateChanged.connect(lambda: self.checkChanged(self.casualLimFilter, "format"))
        self.legacyFilter.stateChanged.connect(lambda: self.checkChanged(self.legacyFilter, "format"))
        self.modernFilter.stateChanged.connect(lambda: self.checkChanged(self.modernFilter, "format"))
        self.otherFormatFilter.stateChanged.connect(lambda: self.checkChanged(self.otherFormatFilter, "format"))
        self.sealedFilter.stateChanged.connect(lambda: self.checkChanged(self.sealedFilter, "format"))
        self.standardFilter.stateChanged.connect(lambda: self.checkChanged(self.standardFilter, "format"))
        self.twoHGSealedFilter.stateChanged.connect(lambda: self.checkChanged(self.twoHGSealedFilter, "format"))
        self.vintageFilter.stateChanged.connect(lambda: self.checkChanged(self.vintageFilter, "format"))
        
        #Callback for calendars
        self.startingDate.selectionChanged.connect(lambda: self.dateChanged(self.startingDate, "starting"))
        self.endingDate.selectionChanged.connect(lambda: self.dateChanged(self.endingDate, "ending"))
    
    def dateChanged( self, ourCalendar, dateType ):
        self.dates[dateType] = ourCalendar.selectedDate().toString("yyyy-MM-dd")
        
    def checkChanged( self, ourCheck, checkType ):
        if ourCheck.checkState() == Qt.Checked:
            if checkType == "event":
                self.selectedEvents.append(ourCheck.toolTip())
            elif checkType == "format":
                self.selectedFormats.append(ourCheck.toolTip())
        else:
            if checkType == "event":
                self.selectedEvents.remove(ourCheck.toolTip())
            elif checkType == "format":
                self.selectedFormats.remove(ourCheck.toolTip())

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
