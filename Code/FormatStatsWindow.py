import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_FormatStats import Ui_FormatStats

class FormatStatsWindow(QDialog, Ui_FormatStats):
    def __init__(self, parent):
        super(FormatStatsWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.rent = parent

    def updateGUI( self ):
        self.standardRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats["Standard"]["Wins"], self.rent.statsFormats["Standard"]["Losses"], self.rent.statsFormats["Standard"]["Draws"]))
        self.standardMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats["Standard"]["Matches"])
        self.standardWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats["Standard"]["Win Percent"])
        
        self.modernRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats["Modern"]["Wins"], self.rent.statsFormats["Modern"]["Losses"], self.rent.statsFormats["Modern"]["Draws"]))
        self.modernMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats["Modern"]["Matches"])
        self.modernWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats["Modern"]["Win Percent"])
        
        self.legacyRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats["Legacy"]["Wins"], self.rent.statsFormats["Legacy"]["Losses"], self.rent.statsFormats["Legacy"]["Draws"]))
        self.legacyMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats["Legacy"]["Matches"])
        self.legacyWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats["Legacy"]["Win Percent"])
        
        self.vintageRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats["Vintage"]["Wins"], self.rent.statsFormats["Vintage"]["Losses"], self.rent.statsFormats["Vintage"]["Draws"]))
        self.vintageMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats["Vintage"]["Matches"])
        self.vintageWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats["Vintage"]["Win Percent"])
        
        self.draftRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats["Booster Draft"]["Wins"], self.rent.statsFormats["Booster Draft"]["Losses"], self.rent.statsFormats["Booster Draft"]["Draws"]))
        self.draftMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats["Booster Draft"]["Matches"])
        self.draftWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats["Booster Draft"]["Win Percent"])
        
        self.sealedRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats["Sealed"]["Wins"], self.rent.statsFormats["Sealed"]["Losses"], self.rent.statsFormats["Sealed"]["Draws"]))
        self.sealedMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats["Sealed"]["Matches"])
        self.sealedWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats["Sealed"]["Win Percent"])
        
        self.twoHGRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats["2 HG Sealed"]["Wins"], self.rent.statsFormats["2 HG Sealed"]["Losses"], self.rent.statsFormats["2 HG Sealed"]["Draws"]))
        self.twoHGMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats["2 HG Sealed"]["Matches"])
        self.twoHGWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats["2 HG Sealed"]["Win Percent"])
        
        self.casualLimRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats["Casual - Limited"]["Wins"], self.rent.statsFormats["Casual - Limited"]["Losses"], self.rent.statsFormats["Casual - Limited"]["Draws"]))
        self.casualLimMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats["Casual - Limited"]["Matches"])
        self.casualLimWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats["Casual - Limited"]["Win Percent"])
        
        self.casualConRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats["Casual - Constructed"]["Wins"], self.rent.statsFormats["Casual - Constructed"]["Losses"], self.rent.statsFormats["Casual - Constructed"]["Draws"]))
        self.casualConMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats["Casual - Constructed"]["Matches"])
        self.casualConWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats["Casual - Constructed"]["Win Percent"])
        
        self.otherRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats["Other"]["Wins"], self.rent.statsFormats["Other"]["Losses"], self.rent.statsFormats["Other"]["Draws"]))
        self.otherMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats["Other"]["Matches"])
        self.otherWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats["Other"]["Win Percent"])

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
        self.exportStatsButton.clicked.connect(lambda: self.rent.exportStatsPressed())
