Set WshShell = CreateObject("WScript.Shell")
cmds=WshShell.RUN("travianRaiderGUI.py", 0, True)
Set WshShell = Nothing