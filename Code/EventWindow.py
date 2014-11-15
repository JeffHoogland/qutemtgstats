import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Event import Ui_Event

'''"ID":eventId,
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
                                        "Notes":"",'''

class EventWindow(QDialog, Ui_Event):
    def __init__(self, parent, eventId):
        super(EventWindow, self).__init__(parent)
        self.rent = parent
        self.data = parent.eventData[eventId]
        
        self.setupUi(self)
        self.assignWidgets()
        
        self.setWindowTitle(unicode("%s Event Data"%eventId))
        
    def savePressed( self ):
        self.data["Notes"] = self.notesText.toPlainText()
        self.data["Deck"] = self.deckText.text()
        self.data["Place"] = self.placeText.text()
        self.data["Type"] = self.eventTypeText.text()
        self.data["Players"] = self.playersText.text()
        self.data["Format"] = self.formatText.text()
        self.data["Location"] = self.locationText.text()
        self.data["Date"] = self.dateText.text()
        
        self.rent.updateGUI()
        self.rent.messageBox( "Event changes saved." )
        
    def closePressed( self ):
        self.hide()
        
    def roundSelected( self, ourRound, ourColumn  ):
        ourIndex = int(ourRound.text(0)) - 1
        
        deckName, ok = QInputDialog.getText(self, "Qute Input",
                                     "Enter Deck Name:")
                                     
        if ok and deckName:
            self.data["Opponents"][ourIndex][3].setData(3, 0, deckName)

    def assignWidgets( self ):
        self.saveChangesButton.clicked.connect(self.savePressed)
        self.closeButton.clicked.connect(self.closePressed)
        self.roundTree.itemDoubleClicked.connect(self.roundSelected)
        
        self.notesText.setPlainText(self.data["Notes"])
        self.deckText.setText(self.data["Deck"])
        self.placeText.setText(self.data["Place"])
        self.eventTypeText.setText(self.data["Type"])
        self.playersText.setText(self.data["Players"])
        self.formatText.setText(self.data["Format"])
        self.locationText.setText(self.data["Location"])
        self.dateText.setText(self.data["Date"])
        
        #Add match data
        matchItem =  TreeWidgetItem(self.resultsTree)
        matchItem.setText(0, unicode(self.data["Wins"]))
        matchItem.setText(1, unicode(self.data["Losses"]))
        matchItem.setText(2, unicode(self.data["Draws"]))
        matchItem.setText(3, unicode(self.data["Matches"]))
            
        self.resultsTree.addTopLevelItem(matchItem)
        for i in range(4):
            self.resultsTree.resizeColumnToContents(i)
        
        for opponent in self.data["Opponents"]:
            roundItem = TreeWidgetItem(self.roundTree)
            roundItem.setText(0, unicode(self.data["Opponents"].index(opponent)+1))
            roundItem.setText(1, unicode(opponent[0]))
            roundItem.setText(2, unicode(opponent[1]))
            roundItem.setText(3, unicode(opponent[2]))
            
            opponent[3] = roundItem
            
            self.roundTree.addTopLevelItem(roundItem)
        
        for i in range(4):
            self.roundTree.resizeColumnToContents(i)

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
