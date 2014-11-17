A cross-platform tool written in Python and Qt for calculating MTG Stats

![alt text](https://raw.githubusercontent.com/JeffHoogland/qutemtgstats/master/Screenshots/qute-filterspage.png "Filters Page") - ![alt text](https://raw.githubusercontent.com/JeffHoogland/qutemtgstats/master/Screenshots/qute-statspage.png "Stats Page")

By: [Jeff Hoogland](http://www.jeffhoogland.com/)

Installation -

Windows:
- Download the [latest build](https://github.com/JeffHoogland/qutemtgstats/blob/master/build/qutemtgstats-windows.zip?raw=true)
- Extract the zip file and run qutemtgstats

Other OS:
- Install python 2.7 and pyside
- Clone the latest sources
- Run **qutemtgstats.py**

Usage:
- Make sure you are logged into your Wizard's account [here](http://www.wizards.com/magic/planeswalkerpoints) in [Google Chrome](http://www.google.com/chrome/).
- Open [this link](https://www.wizards.com/Magic/PlaneswalkerPoints/History#type=EventsOnly).
- Press *ctrl+shift+j*
- In the console that opens run the command: **$("a.Expand").click()**
- Make sure you gave the previous command enough time to run! It takes a minute.
- Press *ctrl+a* to select the data followed by *ctrl+c* to copy the data
- Paste the data into the Raw Data tab in Qute
- Press Phrase Data and Enjoy!

TODO List:

- Add new events from an updated paste to saved data
- Stats by deck
- Pivot Tables on Stats Pages
- Graphs
- History over given intervals (watch improvement)
