import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_Filters import Ui_Filters

class FiltersWindow(QDialog, Ui_Filters):
    def __init__(self, parent):
        super(FiltersWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.rent = parent
        
        self.qObjects = {   "Formats":{},
                            "Events":{},
                            "Decks":{}}

    def updateGUI( self ):
        for ourFormat in self.rent.formatsList:
            if ourFormat not in self.qObjects["Formats"]:
                ourItem = self.qObjects["Formats"][ourFormat] = QListWidgetItem(self.formatListWidget)
                ourItem.setText(ourFormat)
                ourItem.setCheckState(Qt.Checked)
                ourItem.setToolTip(ourFormat)
            
        for ourEvent in self.rent.eventsList:
            if ourEvent not in self.qObjects["Events"]:
                ourItem = self.qObjects["Events"][ourEvent] = QListWidgetItem(self.eventListWidget)
                ourItem.setText(ourEvent)
                ourItem.setCheckState(Qt.Checked)
                ourItem.setToolTip(ourEvent)
            
        for ourDeck in self.rent.decksList:
            if ourDeck not in self.qObjects["Decks"]:
                ourItem = self.qObjects["Decks"][ourDeck] = QListWidgetItem(self.deckListWidget)
                ourItem.setText(ourDeck)
                ourItem.setCheckState(Qt.Checked)
                ourItem.setToolTip(ourDeck)

    def dateChanged( self, ourCalendar, dateType ):
        self.rent.dates[dateType] = ourCalendar.selectedDate().toString("yyyy-MM-dd")
        
    def checkChanged( self, ourCheck, checkType, frameObj ):
        if ourCheck.checkState() == Qt.Checked:
            if checkType == "event":
                self.rent.selectedEvents.append(ourCheck.toolTip())
            elif checkType == "format":
                self.rent.selectedFormats.append(ourCheck.toolTip())
            elif checkType == "deck":
                self.rent.selectedDecks.append(ourCheck.toolTip())
        else:
            if checkType == "event":
                self.rent.selectedEvents.remove(ourCheck.toolTip())
            elif checkType == "format":
                self.rent.selectedFormats.remove(ourCheck.toolTip())
            elif checkType == "deck":
                self.rent.selectedDecks.remove(ourCheck.toolTip())
        
        frameObj.setVisible(ourCheck.checkState())

    def cancelPressed( self ):
        self.hide()
        
    def checkToggle( self, ourCheck, ourName, ourList ):
        if ourCheck.checkState() == Qt.Checked:
            if ourName not in ourList:
                ourList.append(ourName)
        else:
            if ourName in ourList:
                ourList.remove(ourName)

    def updateFiltersPressed( self ):
        for ourFormat in self.qObjects["Formats"]:
            self.checkToggle(self.qObjects["Formats"][ourFormat], ourFormat, self.rent.selectedFormats)
            
        for ourEvent in self.qObjects["Events"]:
            self.checkToggle(self.qObjects["Events"][ourEvent], ourEvent, self.rent.selectedEvents)
        
        for ourDeck in self.qObjects["Decks"]:
            self.checkToggle(self.qObjects["Decks"][ourDeck], ourDeck, self.rent.selectedDecks)
        
        self.rent.updateGUI()
        self.hide()
        self.rent.messageBox( "Filters successfully applied" )
        

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)

        self.updateFiltersButton.clicked.connect(self.updateFiltersPressed)
        
        #Callback for calendars
        #self.startingDate.selectionChanged.connect(lambda: self.dateChanged(self.startingDate, "starting"))
        #self.endingDate.selectionChanged.connect(lambda: self.dateChanged(self.endingDate, "ending"))
