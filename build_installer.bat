@echo off
echo ================================================
echo   AETHER-1 Production Installer Builder
echo ================================================

echo [1/5] Checking dependencies...
python -m pip install pyinstaller inno-setup-script --quiet

if not exist "dist" mkdir dist

echo [2/5] Building AETHER-1 executable...
pyinstaller --onefile --windowed --name AETHER1 ^
    --add-data "gui;gui" ^
    --add-data "suites;suites" ^
    --add-data "docs;docs" ^
    gui/hacker_gui.py

if errorlevel 1 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo [3/5] Creating desktop shortcut creator...
python gui/desktop_shortcut.py

echo [4/5] Building installer with Inno Setup...
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
    "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer\AETHER1_Setup.iss
) else (
    echo WARNING: Inno Setup not found. Please install it or use the .iss file manually.
)

echo [5/5] Done!
echo.
echo ================================================
echo   SUCCESS: AETHER1_Setup.exe created in installer\
echo   Desktop shortcut will be created on install
echo ================================================
pause