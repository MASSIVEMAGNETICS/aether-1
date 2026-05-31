import os
import sys

try:
    import winshell
    from win32com.client import Dispatch
except ImportError:
    print("Installing required packages for shortcut creation...")
    os.system("pip install pywin32 winshell")
    import winshell
    from win32com.client import Dispatch

def create_desktop_shortcut():
    try:
        desktop = winshell.desktop()
        shortcut_path = os.path.join(desktop, "AETHER-1.lnk")
        
        # Path to the installed executable
        target = os.path.join(os.environ.get("ProgramFiles", "C:\\Program Files"), "AETHER1", "AETHER1.exe")
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = os.path.dirname(target)
        shortcut.IconLocation = target + ",0"
        shortcut.Description = "Launch AETHER-1 - The Living Post-LLM Entity"
        shortcut.save()
        
        print("[SUCCESS] Desktop shortcut created at:", shortcut_path)
    except Exception as e:
        print(f"[WARNING] Could not create desktop shortcut: {e}")

if __name__ == "__main__":
    create_desktop_shortcut()