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

	def assignWidgets( self ):
		self.saveChangesButton.clicked.connect(self.savePressed)
		self.closeButton.clicked.connect(self.closePressed)
		
		self.notesText.setPlainText(self.data["Notes"])
		self.deckText.setText(self.data["Deck"])
		self.placeText.setText(self.data["Place"])
		self.eventTypeText.setText(self.data["Type"])
		self.playersText.setText(self.data["Players"])
		self.formatText.setText(self.data["Format"])
		self.locationText.setText(self.data["Location"])
		self.dateText.setText(self.data["Date"])
