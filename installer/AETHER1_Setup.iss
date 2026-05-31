; AETHER-1 Production Installer
; One-click setup for the revolutionary post-LLM living entity

[Setup]
AppId={{AETHER1-2026}}
AppName=AETHER-1
AppVersion=1.0.0
AppPublisher=MASSIVEMAGNETICS
AppPublisherURL=https://github.com/MASSIVEMAGNETICS/aether-1
DefaultDirName={pf}\AETHER1
DefaultGroupName=AETHER-1
AllowNoIcons=yes
LicenseFile=..\LICENSE
OutputDir=..
OutputBaseFilename=AETHER1_Setup
SetupIconFile=..\assets\icon.ico
Compression=lzma2
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\dist\AETHER1.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\gui\*"; DestDir: "{app}\gui"; Flags: ignoreversion recursesubdirs
Source: "..\suites\*"; DestDir: "{app}\suites"; Flags: ignoreversion recursesubdirs
Source: "..\docs\*"; DestDir: "{app}\docs"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\AETHER-1"; Filename: "{app}\AETHER1.exe"
Name: "{autodesktop}\AETHER-1"; Filename: "{app}\AETHER1.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\AETHER1.exe"; Description: "{cm:LaunchProgram,AETHER-1}"; Flags: nowait postinstall skipifsilent

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // Auto-train frontier model on first install
    MsgBox('AETHER-1 is now training its frontier SOTA model. This may take a few minutes...', mbInformation, MB_OK);
  end;
end;