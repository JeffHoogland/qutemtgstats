#!/bin/bash
rm Code/ui_*.py
rm Code/ui_*.pyc
pyside-uic UIs/Main.ui > Code/ui_Main.py
pyside-uic UIs/ExportStats.ui > Code/ui_ExportStats.py
pyside-uic UIs/Event.ui > Code/ui_Event.py
