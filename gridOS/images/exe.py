import cx_Freeze
import os
import time

executables = [cx_Freeze.Executable('gridOS.py')]


cx_Freeze.setup(name = 'Grid OS', version = '1.0.0', options = {'build_exe': {'packages':['pygame', 'pickle', 'win32api', 'tkMessageBox'], 'include_files':[
"booting.png",
"calendar.png",
"cd-player.png",
"cross31 (1).png",
"cross31.png",
"exclamation-mark-inside-a-circle.png",
"file.png",
"gridtech_logo_v2.jpg",
"logo.png",
"notifications-button.png",
"open-folder-icon.png",
"power-button-outline.png",
"settings.png",
"shutdown.png",
"turn-notifications-on-button.png",
"web66.png",]}}, executables = executables)
