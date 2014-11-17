#!/bin/bash
rm Code/ui_*.py
rm Code/ui_*.pyc
pyside-uic UIs/Main.ui > Code/ui_Main.py
pyside-uic UIs/ExportStats.ui > Code/ui_ExportStats.py
pyside-uic UIs/Event.ui > Code/ui_Event.py
pyside-uic UIs/EventList.ui > Code/ui_EventList.py
pyside-uic UIs/EventStats.ui > Code/ui_EventStats.py
pyside-uic UIs/DeckStats.ui > Code/ui_DeckStats.py
pyside-uic UIs/Filters.ui > Code/ui_Filters.py
pyside-uic UIs/FormatStats.ui > Code/ui_FormatStats.py
pyside-uic UIs/OpponentList.ui > Code/ui_OpponentList.py
pyside-uic UIs/Paste.ui > Code/ui_Paste.py
pyside-uic UIs/Help.ui > Code/ui_Help.py
