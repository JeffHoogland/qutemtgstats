import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_DeckStats import Ui_DeckStats

class DeckStatsWindow(QDialog, Ui_DeckStats):
    def __init__(self, parent):
        super(DeckStatsWindow, self).__init__(parent)
        self.setupUi(self)
        self.frames = {}
        self.assignWidgets()
        self.rent = parent

    def updateGUI( self ):
        for frame in self.frames:
            self.frames[frame][0].hide()

        self.frames.clear()

        for deck in self.rent.selectedDecks:
            if deck != "Blank":
                #Each entry is a list with the first being a QFrame object, the second being a QVBoxLayout object, and 3-6 being QLabels
                self.frames[deck] = []
                self.frames[deck].append(QFrame(self.scrollAreaWidgetContents))
                self.frames[deck][0].setFrameShape(QFrame.StyledPanel)
                self.frames[deck][0].setFrameShadow(QFrame.Raised)
                self.frames[deck][0].setObjectName("%sFrame"%deck)

                self.frames[deck].append(QVBoxLayout(self.frames[deck][0]))

                self.frames[deck].append(QLabel(self.frames[deck][0]))
                self.frames[deck][2].setText("<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">%s:</span></p></body></html>"%deck)
                self.frames[deck].append(QLabel(self.frames[deck][0]))
                self.frames[deck][3].setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsDecks[deck]["Wins"], self.rent.statsDecks[deck]["Losses"], self.rent.statsDecks[deck]["Draws"]))
                self.frames[deck].append(QLabel(self.frames[deck][0]))
                self.frames[deck][4].setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsDecks[deck]["Matches"])
                self.frames[deck].append(QLabel(self.frames[deck][0]))
                self.frames[deck][5].setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsDecks[deck]["Win Percent"])

                for i in range(2, 6):
                    self.frames[deck][1].addWidget(self.frames[deck][i])

                self.horizontalLayout_2.addWidget(self.frames[deck][0])

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
        self.exportStatsButton.clicked.connect(lambda: self.rent.exportStatsPressed())
