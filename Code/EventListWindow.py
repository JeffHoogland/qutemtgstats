import os
import csv

from PySide.QtGui import *
from PySide.QtCore import *

from ui_EventList import Ui_EventList

from EventWindow import EventWindow

from builtins import str as text

class EventListWindow(QDialog, Ui_EventList):
    def __init__(self, parent):
        super(EventListWindow, self).__init__(parent)
        self.rent = parent
        self.setupUi(self)
        self.assignWidgets()
        self.csvList = []

    def updateGUI( self ):
        self.eventTree.setSortingEnabled(False)
        self.eventTree.clear()
        del self.csvList[:]
        self.csvList.append(["ID","Place","Type","Players","Format","Location","Date","Deck","Wins","Losses","Draws"])
        for eventId in self.rent.filteredEventData:
            eventItem = TreeWidgetItem(self.eventTree)
            eventItem.setText(0, eventId)
            eventItem.setText(1, text(self.rent.eventData[eventId]["Place"]))
            eventItem.setText(2, text(self.rent.eventData[eventId]["Type"]))
            eventItem.setText(3, text(self.rent.eventData[eventId]["Players"]))
            eventItem.setText(4, text(self.rent.eventData[eventId]["Format"]))
            eventItem.setText(5, text(self.rent.eventData[eventId]["Location"]))
            eventItem.setText(6, text(self.rent.eventData[eventId]["Date"]))
            eventItem.setText(7, text(self.rent.eventData[eventId]["Deck"]))
            eventItem.setText(8, text(self.rent.eventData[eventId]["Wins"]))
            eventItem.setText(9, text(self.rent.eventData[eventId]["Losses"]))
            eventItem.setText(10, text(self.rent.eventData[eventId]["Draws"]))
            
            self.eventTree.addTopLevelItem(eventItem)
            self.csvList.append([eventId, self.rent.eventData[eventId]["Place"], self.rent.eventData[eventId]["Type"],
                                    self.rent.eventData[eventId]["Players"], self.rent.eventData[eventId]["Format"],
                                    self.rent.eventData[eventId]["Location"], self.rent.eventData[eventId]["Date"],
                                    self.rent.eventData[eventId]["Deck"], self.rent.eventData[eventId]["Wins"],
                                    self.rent.eventData[eventId]["Losses"], self.rent.eventData[eventId]["Draws"]])
        
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
        filename = QFileDialog.getSaveFileName(self, 'Selection a location to save your data to:', os.getenv('HOME'), 'CSV Files (*.csv)') #returns (fileName, selectedFilter) 
        if filename[0]:
            with open(filename[0], "wb") as f:
                writer = csv.writer(f)
                writer.writerows(self.csvList)

            self.rent.messageBox( "Data exported successfully." )

    def assignWidgets( self ):
        self.adjustFiltersButton.clicked.connect(lambda: self.rent.filtersWindow.show())
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
