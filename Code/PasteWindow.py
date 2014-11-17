#How many lines after the data we find certain data
EventDate = 0
EventType = 1
EventPlayers = 3
EventFormat = 5
EventLocation = 6
EventPlace = 7
EventID = 8
EventHistory = 10

import os
import datetime

#Quick function for quick usage to see if text is a valid date of the YYYY-MM-DD format
def isDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Paste import Ui_Paste

class PasteWindow(QDialog, Ui_Paste):
    def __init__(self, parent ):
        super(PasteWindow, self).__init__(parent)
        self.rent = parent
        self.eventData = {}
        
        self.setupUi(self)
        self.assignWidgets()

    def prasePressed( self ):
        self.rawData = self.statsPaste.toPlainText().split("\n")
        self.formatData()
        self.rent.messageBox( "Data successfully imported." )

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
            if eventId not in self.rent.eventData:
                eventPlace = self.rawData[startingRow+EventPlace].split(":")[1].lstrip()
                eventType = self.rawData[startingRow+EventType].split(":")[1].lstrip()
                
                if eventType not in self.rent.masterEvents:
                    eventType = "Other"
                
                eventPlayers = self.rawData[startingRow+EventPlayers].split(":")[1].lstrip()
                eventFormat = self.rawData[startingRow+EventFormat].split(":")[1].lstrip()
                
                if eventFormat not in self.rent.masterFormats:
                    eventFormat = "Other"
                
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
                                eventWins += 1
                            elif ourRound[1] == "Loss":
                                eventLosses += 1
                            elif ourRound[1] == "Draw":
                                eventDraws += 1
                            #Name, result, deck, TreeWidgetItem object
                            eventOpponents.append([ourRound[3], ourRound[1], "", None])
                
                eventMatches = eventWins + eventLosses + eventDraws
                
                self.eventData[eventId] = { "ID":eventId,
                                            "Place":eventPlace,
                                            "Type":eventType,
                                            "Players":eventPlayers,
                                            "Format":eventFormat,
                                            "Location":eventLocation,
                                            "Date":eventDate,
                                            "Opponents":eventOpponents,
                                            "Wins":eventWins,
                                            "Losses":eventLosses,
                                            "Draws":eventDraws,
                                            "Matches":eventMatches,
                                            "Deck":"",
                                            "Notes":"",
                                            "WindowObject":None }
        
        self.hide()
        self.rent.dataLoadedSuccessful(self.eventData)

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.praseButton.clicked.connect(self.prasePressed)
        self.cancelButton.clicked.connect(self.cancelPressed)
