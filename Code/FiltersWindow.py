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

    def dateChanged( self, ourCalendar, dateType ):
        self.rent.dates[dateType] = ourCalendar.selectedDate().toString("yyyy-MM-dd")
        
    def checkChanged( self, ourCheck, checkType, frameObj ):
        if ourCheck.checkState() == Qt.Checked:
            if checkType == "event":
                self.rent.selectedEvents.append(ourCheck.toolTip())
            elif checkType == "format":
                self.rent.selectedFormats.append(ourCheck.toolTip())
        else:
            if checkType == "event":
                self.rent.selectedEvents.remove(ourCheck.toolTip())
            elif checkType == "format":
                self.rent.selectedFormats.remove(ourCheck.toolTip())
        
        frameObj.setVisible(ourCheck.checkState())

    def cancelPressed( self ):
        self.hide()

    def updateFiltersPressed( self ):
        self.rent.updateFilteredData()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)

        self.updateFiltersButton.clicked.connect(self.updateFiltersPressed)
        
        #Assign our many check boxes for filters
        self.FNMFilter.stateChanged.connect(lambda: self.checkChanged(self.FNMFilter, "event", self.rent.eventStatsWindow.fnmFrame))
        self.GPTFilter.stateChanged.connect(lambda: self.checkChanged(self.GPTFilter, "event", self.rent.eventStatsWindow.gptFrame))
        self.PTQFilter.stateChanged.connect(lambda: self.checkChanged(self.PTQFilter, "event", self.rent.eventStatsWindow.ptqFrame))
        self.WMCQFilter.stateChanged.connect(lambda: self.checkChanged(self.WMCQFilter, "event", self.rent.eventStatsWindow.wmcqFrame))
        self.gameDayFilter.stateChanged.connect(lambda: self.checkChanged(self.gameDayFilter, "event", self.rent.eventStatsWindow.gameDayFrame))
        self.grandPrixFilter.stateChanged.connect(lambda: self.checkChanged(self.grandPrixFilter, "event", self.rent.eventStatsWindow.grandPrixFrame))
        self.otherEventFilter.stateChanged.connect(lambda: self.checkChanged(self.otherEventFilter, "event", self.rent.eventStatsWindow.otherEventFrame))
        self.premiumTournamentFilter.stateChanged.connect(lambda: self.checkChanged(self.premiumTournamentFilter, "event", self.rent.eventStatsWindow.premiumFrame))
        self.prereleaseFilter.stateChanged.connect(lambda: self.checkChanged(self.prereleaseFilter, "event", self.rent.eventStatsWindow.prereleaseFrame))
        self.proTourFilter.stateChanged.connect(lambda: self.checkChanged(self.proTourFilter, "event", self.rent.eventStatsWindow.proTourFrame))
        
        self.boosterDraftFilter.stateChanged.connect(lambda: self.checkChanged(self.boosterDraftFilter, "format", self.rent.formatStatsWindow.draftFrame))
        self.casualConFilter.stateChanged.connect(lambda: self.checkChanged(self.casualConFilter, "format", self.rent.formatStatsWindow.casualConFrame))
        self.casualLimFilter.stateChanged.connect(lambda: self.checkChanged(self.casualLimFilter, "format", self.rent.formatStatsWindow.casualLimFrame))
        self.legacyFilter.stateChanged.connect(lambda: self.checkChanged(self.legacyFilter, "format", self.rent.formatStatsWindow.legacyFrame))
        self.modernFilter.stateChanged.connect(lambda: self.checkChanged(self.modernFilter, "format", self.rent.formatStatsWindow.modernFrame))
        self.otherFormatFilter.stateChanged.connect(lambda: self.checkChanged(self.otherFormatFilter, "format", self.rent.formatStatsWindow.otherFrame))
        self.sealedFilter.stateChanged.connect(lambda: self.checkChanged(self.sealedFilter, "format", self.rent.formatStatsWindow.sealedFrame))
        self.standardFilter.stateChanged.connect(lambda: self.checkChanged(self.standardFilter, "format", self.rent.formatStatsWindow.standardFrame))
        self.twoHGSealedFilter.stateChanged.connect(lambda: self.checkChanged(self.twoHGSealedFilter, "format", self.rent.formatStatsWindow.twoHGFrame))
        self.vintageFilter.stateChanged.connect(lambda: self.checkChanged(self.vintageFilter, "format", self.rent.formatStatsWindow.vintageFrame))
        
        #Callback for calendars
        self.startingDate.selectionChanged.connect(lambda: self.dateChanged(self.startingDate, "starting"))
        self.endingDate.selectionChanged.connect(lambda: self.dateChanged(self.endingDate, "ending"))
