#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  setup.py

import sys
from cx_Freeze import setup, Executable

executables = [Executable("TRGUI.py", icon="exe.ico", base="Win32GUI", appendScriptToExe=True, appendScriptToLibrary=False)]

setup(
	name = "Travian Raider",
	version = "2.1",
	description = "A toolset for the browser game Travian",
	executables = executables)
