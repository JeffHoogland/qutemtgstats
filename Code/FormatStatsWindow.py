import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_FormatStats import Ui_FormatStats

class FormatStatsWindow(QDialog, Ui_FormatStats):
    def __init__(self, parent):
        super(FormatStatsWindow, self).__init__(parent)
        self.setupUi(self)
        self.assignWidgets()
        self.frames = {}
        self.rent = parent

    def updateGUI( self ):
        for frame in self.frames:
            self.frames[frame][0].hide()

        self.frames.clear()

        for ourFormat in self.rent.selectedFormats:
            if ourFormat != "Blank":
                #Each entry is a list with the first being a QFrame object, the second being a QVBoxLayout object, and 3-6 being QLabels
                self.frames[ourFormat] = []
                self.frames[ourFormat].append(QFrame(self.scrollAreaWidgetContents))
                self.frames[ourFormat][0].setFrameShape(QFrame.StyledPanel)
                self.frames[ourFormat][0].setFrameShadow(QFrame.Raised)
                self.frames[ourFormat][0].setObjectName("%sFrame"%ourFormat)

                self.frames[ourFormat].append(QVBoxLayout(self.frames[ourFormat][0]))

                self.frames[ourFormat].append(QLabel(self.frames[ourFormat][0]))
                self.frames[ourFormat][2].setText("<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">%s:</span></p></body></html>"%ourFormat)
                self.frames[ourFormat].append(QLabel(self.frames[ourFormat][0]))
                self.frames[ourFormat][3].setText("<p><b>Overall Record:</b></p> <p>%s-%s-%s</p>"%(self.rent.statsFormats[ourFormat]["Wins"], self.rent.statsFormats[ourFormat]["Losses"], self.rent.statsFormats[ourFormat]["Draws"]))
                self.frames[ourFormat].append(QLabel(self.frames[ourFormat][0]))
                self.frames[ourFormat][4].setText("<p><b>Total Matches:</b></p> <p>%s</p>"%self.rent.statsFormats[ourFormat]["Matches"])
                self.frames[ourFormat].append(QLabel(self.frames[ourFormat][0]))
                self.frames[ourFormat][5].setText("<p><b>Win Percent:</b></p> <p>%.2f</p>"%self.rent.statsFormats[ourFormat]["Win Percent"])

                for i in range(2, 6):
                    self.frames[ourFormat][1].addWidget(self.frames[ourFormat][i])

                self.horizontalLayout_2.addWidget(self.frames[ourFormat][0])

    def cancelPressed( self ):
        self.hide()

    def assignWidgets( self ):
        self.cancelButton.clicked.connect(self.cancelPressed)
        self.exportStatsButton.clicked.connect(lambda: self.rent.exportStatsPressed())
