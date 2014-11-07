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
                                
        
                                
        self.dates = {  "starting":"1991-01-01",
                        "ending":"2015-12-31" }
        
        self.statsReset()
        self.assignWidgets()
    
    def statsReset( self ):
        self.statsEvents = {    "Magic Pro Tour":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Magic Pro Tour Qualifier":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "World Magic Cup Qualifier":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Magic Grand Prix Trial":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Magic Prerelease":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Magic WPN Premium Tournament":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Magic Game Day":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Magic Grand Prix":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Friday Night Magic":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Other":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0}}
        self.statsFormats = {   "Standard":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Modern":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Legacy":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Vintage":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Booster Draft":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Sealed":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "2 HG Sealed":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Casual - Constructed":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Casual - Limited":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0},
                                "Other":{"Matches":0, "Wins":0, "Losses":0, "Draws":0, "Win Percent":0.0}}
    
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
            
            if eventType not in self.masterEvents:
                eventType = "Other"
            
            eventPlayers = self.rawData[startingRow+EventPlayers].split(":")[1].lstrip()
            eventFormat = self.rawData[startingRow+EventFormat].split(":")[1].lstrip()
            
            if eventFormat not in self.masterFormats:
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
                            eventOpponents.append([ourRound[3], "Win"])
                            eventWins += 1
                        elif ourRound[1] == "Loss":
                            eventOpponents.append([ourRound[3], "Loss"])
                            eventLosses += 1
                        elif ourRound[1] == "Draw":
                            eventOpponents.append([ourRound[3], "Draw"])
                            eventDraws += 1
            
            eventMatches = eventWins + eventLosses + eventDraws
            
            self.eventData[eventId] = { "Place":eventPlace,
                                        "Type":eventType,
                                        "Players":eventPlayers,
                                        "Format":eventFormat,
                                        "Location":eventLocation,
                                        "Date":eventDate,
                                        "Opponents":eventOpponents,
                                        "Wins":eventWins,
                                        "Losses":eventLosses,
                                        "Draws":eventDraws,
                                        "Matches":eventMatches}
                        
        self.updateFilteredData()
        
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
        
        #Update stats by format
        self.standardRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsFormats["Standard"]["Wins"], self.statsFormats["Standard"]["Losses"], self.statsFormats["Standard"]["Draws"]))
        self.standardMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsFormats["Standard"]["Matches"])
        self.standardWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsFormats["Standard"]["Win Percent"])
        
        self.modernRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsFormats["Modern"]["Wins"], self.statsFormats["Modern"]["Losses"], self.statsFormats["Modern"]["Draws"]))
        self.modernMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsFormats["Modern"]["Matches"])
        self.modernWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsFormats["Modern"]["Win Percent"])
        
        self.legacyRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsFormats["Legacy"]["Wins"], self.statsFormats["Legacy"]["Losses"], self.statsFormats["Legacy"]["Draws"]))
        self.legacyMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsFormats["Legacy"]["Matches"])
        self.legacyWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsFormats["Legacy"]["Win Percent"])
        
        self.vintageRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsFormats["Vintage"]["Wins"], self.statsFormats["Vintage"]["Losses"], self.statsFormats["Vintage"]["Draws"]))
        self.vintageMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsFormats["Vintage"]["Matches"])
        self.vintageWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsFormats["Vintage"]["Win Percent"])
        
        self.draftRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsFormats["Booster Draft"]["Wins"], self.statsFormats["Booster Draft"]["Losses"], self.statsFormats["Booster Draft"]["Draws"]))
        self.draftMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsFormats["Booster Draft"]["Matches"])
        self.draftWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsFormats["Booster Draft"]["Win Percent"])
        
        self.sealedRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsFormats["Sealed"]["Wins"], self.statsFormats["Sealed"]["Losses"], self.statsFormats["Sealed"]["Draws"]))
        self.sealedMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsFormats["Sealed"]["Matches"])
        self.sealedWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsFormats["Sealed"]["Win Percent"])
        
        self.twoHGRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsFormats["2 HG Sealed"]["Wins"], self.statsFormats["2 HG Sealed"]["Losses"], self.statsFormats["2 HG Sealed"]["Draws"]))
        self.twoHGMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsFormats["2 HG Sealed"]["Matches"])
        self.twoHGWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsFormats["2 HG Sealed"]["Win Percent"])
        
        self.casualLimRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsFormats["Casual - Limited"]["Wins"], self.statsFormats["Casual - Limited"]["Losses"], self.statsFormats["Casual - Limited"]["Draws"]))
        self.casualLimMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsFormats["Casual - Limited"]["Matches"])
        self.casualLimWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsFormats["Casual - Limited"]["Win Percent"])
        
        self.casualConRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsFormats["Casual - Constructed"]["Wins"], self.statsFormats["Casual - Constructed"]["Losses"], self.statsFormats["Casual - Constructed"]["Draws"]))
        self.casualConMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsFormats["Casual - Constructed"]["Matches"])
        self.casualConWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsFormats["Casual - Constructed"]["Win Percent"])
        
        self.otherRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsFormats["Other"]["Wins"], self.statsFormats["Other"]["Losses"], self.statsFormats["Other"]["Draws"]))
        self.otherMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsFormats["Other"]["Matches"])
        self.otherWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsFormats["Other"]["Win Percent"])
        
        #Update stats by event
        self.fnmRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsEvents["Friday Night Magic"]["Wins"], self.statsEvents["Friday Night Magic"]["Losses"], self.statsEvents["Friday Night Magic"]["Draws"]))
        self.fnmMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsEvents["Friday Night Magic"]["Matches"])
        self.fnmWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsEvents["Friday Night Magic"]["Win Percent"])
        
        self.gameDayRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsEvents["Magic Game Day"]["Wins"], self.statsEvents["Magic Game Day"]["Losses"], self.statsEvents["Magic Game Day"]["Draws"]))
        self.gameDayMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsEvents["Magic Game Day"]["Matches"])
        self.gameDayWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsEvents["Magic Game Day"]["Win Percent"])
        
        self.gptRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsEvents["Magic Grand Prix Trial"]["Wins"], self.statsEvents["Magic Grand Prix Trial"]["Losses"], self.statsEvents["Magic Grand Prix Trial"]["Draws"]))
        self.gptMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsEvents["Magic Grand Prix Trial"]["Matches"])
        self.gptWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsEvents["Magic Grand Prix Trial"]["Win Percent"])
        
        self.grandPrixRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsEvents["Magic Grand Prix"]["Wins"], self.statsEvents["Magic Grand Prix"]["Losses"], self.statsEvents["Magic Grand Prix"]["Draws"]))
        self.grandPrixMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsEvents["Magic Grand Prix"]["Matches"])
        self.grandPrixWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsEvents["Magic Grand Prix"]["Win Percent"])
        
        self.premiumRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsEvents["Magic WPN Premium Tournament"]["Wins"], self.statsEvents["Magic WPN Premium Tournament"]["Losses"], self.statsEvents["Magic WPN Premium Tournament"]["Draws"]))
        self.premiumMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsEvents["Magic WPN Premium Tournament"]["Matches"])
        self.premiumWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsEvents["Magic WPN Premium Tournament"]["Win Percent"])
        
        self.prereleaseRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsEvents["Magic Prerelease"]["Wins"], self.statsEvents["Magic Prerelease"]["Losses"], self.statsEvents["Magic Prerelease"]["Draws"]))
        self.prereleaseMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsEvents["Magic Prerelease"]["Matches"])
        self.prereleaseWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsEvents["Magic Prerelease"]["Win Percent"])
        
        self.proTourRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsEvents["Magic Pro Tour"]["Wins"], self.statsEvents["Magic Pro Tour"]["Losses"], self.statsEvents["Magic Pro Tour"]["Draws"]))
        self.proTourMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsEvents["Magic Pro Tour"]["Matches"])
        self.proTourWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsEvents["Magic Pro Tour"]["Win Percent"])
        
        self.ptqRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsEvents["Magic Pro Tour Qualifier"]["Wins"], self.statsEvents["Magic Pro Tour Qualifier"]["Losses"], self.statsEvents["Magic Pro Tour Qualifier"]["Draws"]))
        self.ptqMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsEvents["Magic Pro Tour Qualifier"]["Matches"])
        self.ptqWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsEvents["Magic Pro Tour Qualifier"]["Win Percent"])
        
        self.wmcqRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsEvents["World Magic Cup Qualifier"]["Wins"], self.statsEvents["World Magic Cup Qualifier"]["Losses"], self.statsEvents["World Magic Cup Qualifier"]["Draws"]))
        self.wmcqMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsEvents["World Magic Cup Qualifier"]["Matches"])
        self.wmcqWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsEvents["World Magic Cup Qualifier"]["Win Percent"])
        
        self.otherEventRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.statsEvents["Other"]["Wins"], self.statsEvents["Other"]["Losses"], self.statsEvents["Other"]["Draws"]))
        self.otherEventMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.statsEvents["Other"]["Matches"])
        self.otherEventWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.statsEvents["Other"]["Win Percent"])
        
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
        self.FNMFilter.stateChanged.connect(lambda: self.checkChanged(self.FNMFilter, "event", self.fnmFrame))
        self.GPTFilter.stateChanged.connect(lambda: self.checkChanged(self.GPTFilter, "event", self.gptFrame))
        self.PTQFilter.stateChanged.connect(lambda: self.checkChanged(self.PTQFilter, "event", self.ptqFrame))
        self.WMCQFilter.stateChanged.connect(lambda: self.checkChanged(self.WMCQFilter, "event", self.wmcqFrame))
        self.gameDayFilter.stateChanged.connect(lambda: self.checkChanged(self.gameDayFilter, "event", self.gameDayFrame))
        self.grandPrixFilter.stateChanged.connect(lambda: self.checkChanged(self.grandPrixFilter, "event", self.grandPrixFrame))
        self.otherEventFilter.stateChanged.connect(lambda: self.checkChanged(self.otherEventFilter, "event", self.otherEventFrame))
        self.premiumTournamentFilter.stateChanged.connect(lambda: self.checkChanged(self.premiumTournamentFilter, "event", self.premiumFrame))
        self.prereleaseFilter.stateChanged.connect(lambda: self.checkChanged(self.prereleaseFilter, "event", self.prereleaseFrame))
        self.proTourFilter.stateChanged.connect(lambda: self.checkChanged(self.proTourFilter, "event", self.proTourFrame))
        
        self.boosterDraftFilter.stateChanged.connect(lambda: self.checkChanged(self.boosterDraftFilter, "format", self.draftFrame))
        self.casualConFilter.stateChanged.connect(lambda: self.checkChanged(self.casualConFilter, "format", self.casualConFrame))
        self.casualLimFilter.stateChanged.connect(lambda: self.checkChanged(self.casualLimFilter, "format", self.casualLimFrame))
        self.legacyFilter.stateChanged.connect(lambda: self.checkChanged(self.legacyFilter, "format", self.legacyFrame))
        self.modernFilter.stateChanged.connect(lambda: self.checkChanged(self.modernFilter, "format", self.modernFrame))
        self.otherFormatFilter.stateChanged.connect(lambda: self.checkChanged(self.otherFormatFilter, "format", self.otherFrame))
        self.sealedFilter.stateChanged.connect(lambda: self.checkChanged(self.sealedFilter, "format", self.sealedFrame))
        self.standardFilter.stateChanged.connect(lambda: self.checkChanged(self.standardFilter, "format", self.standardFrame))
        self.twoHGSealedFilter.stateChanged.connect(lambda: self.checkChanged(self.twoHGSealedFilter, "format", self.twoHGFrame))
        self.vintageFilter.stateChanged.connect(lambda: self.checkChanged(self.vintageFilter, "format", self.vintageFrame))
        
        #Callback for calendars
        self.startingDate.selectionChanged.connect(lambda: self.dateChanged(self.startingDate, "starting"))
        self.endingDate.selectionChanged.connect(lambda: self.dateChanged(self.endingDate, "ending"))
    
    def dateChanged( self, ourCalendar, dateType ):
        self.dates[dateType] = ourCalendar.selectedDate().toString("yyyy-MM-dd")
        
    def checkChanged( self, ourCheck, checkType, frameObj ):
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
        
        frameObj.setVisible(ourCheck.checkState())

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
