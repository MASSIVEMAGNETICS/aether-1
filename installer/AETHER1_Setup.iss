[Setup]
AppName=AETHER-1
AppVersion=1.0
DefaultDirName={pf}\AETHER1
OutputDir=installer
OutputBaseFilename=AETHER1_Setup
Compression=lzma2
SolidCompression=yes

[Files]
Source: "dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "gui\hacker_gui.py"; DestDir: "{app}"

[Icons]
Name: "{commondesktop}\AETHER-1"; Filename: "{app}\AETHER1.exe"; WorkingDir: "{app}"

[Run]
Filename: "{app}\AETHER1.exe"; Description: "Launch AETHER-1"; Flags: nowait postinstall skipifsilent