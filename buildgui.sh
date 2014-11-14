#!/bin/bash
rm ui_*.py
rm ui_*.pyc
pyside-uic Main.ui > ui_Main.py
pyside-uic ExportStats.ui > ui_ExportStats.py
pyside-uic Event.ui > ui_Event.py
