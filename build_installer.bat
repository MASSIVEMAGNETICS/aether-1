@echo off
echo Building AETHER-1 One-Click Installer...
pyinstaller --onefile --windowed gui/hacker_gui.py --name AETHER1
iscc installer\AETHER1_Setup.iss
echo Installer created: installer\AETHER1_Setup.exe
echo Desktop shortcut will be created on install.