Travian Raider version 2.0
===========================

Information
-----------

|Project| Travian Raider |
|------|---------------------------|
|Author| Adrian Torres (Elkasitu) |
|Language| Python 2.7.6 |
|License| GPLv3 |
|Changelog| Read CHANGELOG.md |

About
-----

Version 2.0 of the Travian Raider program is different from the 1.x version in a couple of ways:
	
1. It now uses PySide (Qt Framework Python Bindings) for the main GUI design, it is cleaner, easier and Qter than Tkinter.
2. I've changed twill for mechanize, for two main reasons:
	1. I needed to work at a lower level for handling different web docs with BeautifulSoup
	2. I've noticed that it's way faster than twill, mainly because it doesn't arbitrarily print every output
3. The required modules to run the main application (TRGUI.py) are no longer included, so in order to use the source code you have to download the following packages:
	- PySide
	- Mechanize
	- BeautifulSoup
4. The core of the program has been slightly reworked, what used to be TravianRaider.py is now TRCore.py and has been slightly modified to work with mechanize,
   a bit of optimization here and there to make the program run faster (especially when executing raids from the raidlist). What used to be travianRaiderGUI.py
   is now TRGUI.py and has been completely rebuilt because of the change in GUI library.
5. In order to read and write into the raidlist.txt file, containing all the raids for the local user, the program now uses pickle instead of repr and eval, it is
   simply better than needlessly reinventing the wheel.
6. Within the GUI folder you'll find .ui files, which are the files built using the QtDesigner4 and transformed into .py files using the pyside-uic tool

Instructions
------------

1. Linux:
	- Install the Qt Libraries from the official website http://qt-project.org/downloads [4.8.5 for Linux Recommended]
	- Extract files to a folder
	- Launch the TRGUI executable

2. Windows:
	- Install the Qt Libraries from the official website http://qt-project.org/downloads [4.8.5 for Windows (VS 2008) Recommended]
	- If needed, install the msvc package included in the redist folder
	- Extract files to a folder
	- Launch TRGUI.exe
	
3. Mac:
	- No implementation yet
