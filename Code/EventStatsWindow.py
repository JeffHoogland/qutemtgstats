import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_EventStats import Ui_EventStats

class EventStatsWindow(QDialog, Ui_EventStats):
    def __init__(self, parent):
        super(EventStatsWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.rent = parent

    def updateGUI( self ):
        self.fnmRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents["Friday Night Magic"]["Wins"], self.rent.statsEvents["Friday Night Magic"]["Losses"], self.rent.statsEvents["Friday Night Magic"]["Draws"]))
        self.fnmMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents["Friday Night Magic"]["Matches"])
        self.fnmWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents["Friday Night Magic"]["Win Percent"])
        
        self.gameDayRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents["Magic Game Day"]["Wins"], self.rent.statsEvents["Magic Game Day"]["Losses"], self.rent.statsEvents["Magic Game Day"]["Draws"]))
        self.gameDayMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents["Magic Game Day"]["Matches"])
        self.gameDayWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents["Magic Game Day"]["Win Percent"])
        
        self.gptRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents["Magic Grand Prix Trial"]["Wins"], self.rent.statsEvents["Magic Grand Prix Trial"]["Losses"], self.rent.statsEvents["Magic Grand Prix Trial"]["Draws"]))
        self.gptMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents["Magic Grand Prix Trial"]["Matches"])
        self.gptWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents["Magic Grand Prix Trial"]["Win Percent"])
        
        self.grandPrixRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents["Magic Grand Prix"]["Wins"], self.rent.statsEvents["Magic Grand Prix"]["Losses"], self.rent.statsEvents["Magic Grand Prix"]["Draws"]))
        self.grandPrixMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents["Magic Grand Prix"]["Matches"])
        self.grandPrixWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents["Magic Grand Prix"]["Win Percent"])
        
        self.premiumRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents["Magic WPN Premium Tournament"]["Wins"], self.rent.statsEvents["Magic WPN Premium Tournament"]["Losses"], self.rent.statsEvents["Magic WPN Premium Tournament"]["Draws"]))
        self.premiumMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents["Magic WPN Premium Tournament"]["Matches"])
        self.premiumWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents["Magic WPN Premium Tournament"]["Win Percent"])
        
        self.prereleaseRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents["Magic Prerelease"]["Wins"], self.rent.statsEvents["Magic Prerelease"]["Losses"], self.rent.statsEvents["Magic Prerelease"]["Draws"]))
        self.prereleaseMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents["Magic Prerelease"]["Matches"])
        self.prereleaseWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents["Magic Prerelease"]["Win Percent"])
        
        self.proTourRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents["Magic Pro Tour"]["Wins"], self.rent.statsEvents["Magic Pro Tour"]["Losses"], self.rent.statsEvents["Magic Pro Tour"]["Draws"]))
        self.proTourMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents["Magic Pro Tour"]["Matches"])
        self.proTourWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents["Magic Pro Tour"]["Win Percent"])
        
        self.ptqRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents["Magic Pro Tour Qualifier"]["Wins"], self.rent.statsEvents["Magic Pro Tour Qualifier"]["Losses"], self.rent.statsEvents["Magic Pro Tour Qualifier"]["Draws"]))
        self.ptqMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents["Magic Pro Tour Qualifier"]["Matches"])
        self.ptqWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents["Magic Pro Tour Qualifier"]["Win Percent"])
        
        self.wmcqRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents["World Magic Cup Qualifier"]["Wins"], self.rent.statsEvents["World Magic Cup Qualifier"]["Losses"], self.rent.statsEvents["World Magic Cup Qualifier"]["Draws"]))
        self.wmcqMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents["World Magic Cup Qualifier"]["Matches"])
        self.wmcqWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents["World Magic Cup Qualifier"]["Win Percent"])
        
        self.otherEventRecord.setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents["Other"]["Wins"], self.rent.statsEvents["Other"]["Losses"], self.rent.statsEvents["Other"]["Draws"]))
        self.otherEventMatches.setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents["Other"]["Matches"])
        self.otherEventWinPercent.setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents["Other"]["Win Percent"])

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
        self.exportStatsButton.clicked.connect(lambda: self.rent.exportStatsPressed())
