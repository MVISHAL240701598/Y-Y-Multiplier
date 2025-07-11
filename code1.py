import os


def open_app(app_name):
    try:
        os.startfile(app_name)
    except Exception as e:
        print(f"Error opening {app_name}: {e}")
while True:
    open_app("notepad.exe") 
    open_app("calc.exe")
    open_app("mspaint.exe")
    open_app("explorer.exe")
    open_app("cmd.exe")
    open_app("powershell.exe")
    open_app("wordpad.exe")
    open_app("chrome.exe")
    open_app("firefox.exe")
    open_app("edge.exe")
    open_app("vlc.exe")
    open_app("spotify.exe")
    open_app("steam.exe")
    open_app("discord.exe")
    open_app("skype.exe")

