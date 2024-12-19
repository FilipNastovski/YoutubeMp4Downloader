import os
import winshell
from win32com.client import Dispatch

def create_bat_shortcut(script_name, icon_name, shortcut_name):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, script_name)

    # Define the shortcut target path
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, shortcut_name + '.lnk')

    # Define the icon path (assuming the icon is in a subfolder 'Icon' inside the script directory)
    icon_path = os.path.join(script_dir, 'Icon', icon_name)  # Use os.path.join to create the correct path

    # Create the shortcut
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = script_path
    shortcut.WorkingDirectory = script_dir
    shortcut.IconLocation = icon_path  # Set the icon of the shortcut
    shortcut.save()

    print(f"Shortcut created at: {shortcut_path}")

if __name__ == '__main__':
    # Create a shortcuts for the .bat files and set the icon
    create_bat_shortcut('Downloader Script.bat', 'ProgramIcon.ico', 'Video Downloader')
    create_bat_shortcut('Url Script.bat', 'UrlIcon.ico', 'Url Getter')