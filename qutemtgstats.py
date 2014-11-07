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

def checkDate(date_text):
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
        self.assignWidgets()
    
    def phrasePressed( self ):
        self.rawData = self.statsPaste.toPlainText().split("\n")
        
        self.formatData()
        
    def formatData( self ):
        eventBreaks = []
        numberOfRows = len(self.rawData)
        
        for row in range(numberOfRows):
            if checkDate(self.rawData[row-1][:10]):
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
            eventWins = 0
            eventLosses = 0
            eventDraws = 0
            
            for row in range(startingRow+EventHistory, endingRow):
                ourRound = self.rawData[row].split("\t")
                if len(ourRound) == 4:
                    if len(ourRound[3]):
                        self.addMatch(ourRound[3], ourRound[1])
                        if ourRound[1] == "Win":
                            eventWins += 1
                        elif ourRound[1] == "Loss":
                            eventLosses += 1
                        elif ourRound[1] == "Draw":
                            eventDraws += 1
                        
            self.eventData[eventId] = { "Place":eventPlace,
                                        "Type":eventType,
                                        "Players":eventPlayers,
                                        "Format":eventFormat,
                                        "Location":eventLocation,
                                        "Date":eventDate,
                                        "Wins":eventWins,
                                        "Losses":eventLosses,
                                        "Draws":eventDraws}
                                        
        self.updateGUI()
        
    def updateGUI( self ):
        #Update opponents
        self.opponentTree.setSortingEnabled(False)
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
        for eventId in self.eventData:
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
            
            self.eventTree.addTopLevelItem(eventItem)
        
        self.eventTree.setSortingEnabled(True)
        
    def addMatch( self, opponent, result ):
        """opponent is the opponent's name and result should be Win/Loss/Draw"""
        
        if opponent not in self.opponentData:
            self.opponentData[opponent] = {  "Win":0,
                                            "Loss":0,
                                            "Draw":0}
        
        self.opponentData[opponent][result] += 1
    
    def assignWidgets( self ):
        self.phraseButton.clicked.connect(self.phrasePressed)

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
