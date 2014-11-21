import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_EventStats import Ui_EventStats

class EventStatsWindow(QDialog, Ui_EventStats):
    def __init__(self, parent):
        super(EventStatsWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.frames = {}
        self.rent = parent

    def updateGUI( self ):
        for frame in self.frames:
            self.frames[frame][0].hide()

        self.frames.clear()

        for ourEvent in self.rent.selectedEvents:
            if ourEvent != "Blank":
                #Each entry is a list with the first being a QFrame object, the second being a QVBoxLayout object, and 3-6 being QLabels
                self.frames[ourEvent] = []
                self.frames[ourEvent].append(QFrame(self.scrollAreaWidgetContents))
                self.frames[ourEvent][0].setFrameShape(QFrame.StyledPanel)
                self.frames[ourEvent][0].setFrameShadow(QFrame.Raised)
                self.frames[ourEvent][0].setObjectName("%sFrame"%ourEvent)

                self.frames[ourEvent].append(QVBoxLayout(self.frames[ourEvent][0]))

                self.frames[ourEvent].append(QLabel(self.frames[ourEvent][0]))
                self.frames[ourEvent][2].setText("<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">%s:</span></p></body></html>"%ourEvent)
                self.frames[ourEvent].append(QLabel(self.frames[ourEvent][0]))
                self.frames[ourEvent][3].setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsEvents[ourEvent]["Wins"], self.rent.statsEvents[ourEvent]["Losses"], self.rent.statsEvents[ourEvent]["Draws"]))
                self.frames[ourEvent].append(QLabel(self.frames[ourEvent][0]))
                self.frames[ourEvent][4].setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsEvents[ourEvent]["Matches"])
                self.frames[ourEvent].append(QLabel(self.frames[ourEvent][0]))
                self.frames[ourEvent][5].setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsEvents[ourEvent]["Win Percent"])

                for i in range(2, 6):
                    self.frames[ourEvent][1].addWidget(self.frames[ourEvent][i])

                self.horizontalLayout_2.addWidget(self.frames[ourEvent][0])

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
        self.exportStatsButton.clicked.connect(lambda: self.rent.exportStatsPressed())
