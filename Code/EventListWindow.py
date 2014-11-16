import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_EventList import Ui_EventList

from EventWindow import EventWindow

class EventListWindow(QDialog, Ui_EventList):
    def __init__(self, parent):
        super(EventListWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.rent = parent

    def updateGUI( self ):
        self.eventTree.setSortingEnabled(False)
        self.eventTree.clear()
        for eventId in self.rent.filteredEventData:
            eventItem = TreeWidgetItem(self.eventTree)
            eventItem.setText(0, eventId)
            eventItem.setText(1, unicode(self.rent.eventData[eventId]["Place"]))
            eventItem.setText(2, unicode(self.rent.eventData[eventId]["Type"]))
            eventItem.setText(3, unicode(self.rent.eventData[eventId]["Players"]))
            eventItem.setText(4, unicode(self.rent.eventData[eventId]["Format"]))
            eventItem.setText(5, unicode(self.rent.eventData[eventId]["Location"]))
            eventItem.setText(6, unicode(self.rent.eventData[eventId]["Date"]))
            eventItem.setText(7, unicode(self.rent.eventData[eventId]["Deck"]))
            eventItem.setText(8, unicode(self.rent.eventData[eventId]["Wins"]))
            eventItem.setText(9, unicode(self.rent.eventData[eventId]["Losses"]))
            eventItem.setText(10, unicode(self.rent.eventData[eventId]["Draws"]))
            
            self.eventTree.addTopLevelItem(eventItem)
        
        self.eventTree.setSortingEnabled(True)
        for i in range(11):
            self.eventTree.resizeColumnToContents(i)

    def cancelPressed( self ):
        self.hide()

    def eventSelected( self, ourEvent, ourColumn ):
		eventId = ourEvent.text(0)
		
		if not self.rent.eventData[eventId]["WindowObject"]:
			self.rent.eventData[eventId]["WindowObject"] = EventWindow( self.rent, eventId )
			
		self.rent.eventData[eventId]["WindowObject"].show()

    def exportStatsPressed( self ):
        pass

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
        self.exportStatsButton.clicked.connect(self.exportStatsPressed)
        self.eventTree.itemDoubleClicked.connect(self.eventSelected)

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
