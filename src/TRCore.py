#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TRCore.py

## Information ##

__author__ = "Adrian Torres"
__date__ = "2013-10-30"
__version__ = "1.0"

## Imports ##

import pickle
import sys
import mechanize

## Globals ##

b = mechanize.Browser()
b.addheaders[0] = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36")

## Functions ##

def read(filename):
    """ Reads the <filename> content and interprets its content thanks to the pickle module """
    try:
        # tries to open the file and load its content
        with open(filename, "r") as f:
            content = pickle.load(f)
    except:
        # if there is no file called <filename> or the file is empty
        content = []
    return content

def write(filename, content):
    """ Writes to <filename> the passed-in content """
    try:
        # tries to open the file and dump the passed-in content
        with open(filename, "w") as f:
            pickle.dump(content, f)
            c = True
    except:
        # if the previous task fails, we create the file
        with open(filename, "a") as f:
            pickle.dump([], f)
            c = False
    return c

def login(server, name, password):
    """ Logs the user into the specified server using name and password """
    returnValue = True
    if server and name and password:
        if server[-1] != "/":
            # we make sure the server address ends with "/" for further manipulation
            server = server + "/"
        # we log into the server
        try:
            r = b.open(server)
        except:
            return False
        b.select_form("login")
        b.form["name"] = name
        b.form["password"] = password
        r = b.submit()
        try:
            # if we can find the specified link, then we logged in successfully
            c = b.find_link(url="dorf2.php")
        except:
            # else, we didn't log into the server
            returnValue = False
    else:
        returnValue = False
    return returnValue

def addToRaidlist(raid, raidlist):
    """ Adds the passed-in raid to the passed-in raidlist """
    # we add the raid to the raidlist by extending the latest and
    # writting it into raidlist
    content = read(raidlist)
    content.append(raid)
    if not write(raidlist, content):
        write(raidlist, content)
        
def removeAtIndexes(raidlist, p):
    """ Removes the raids at the given indexes """
    content = read(raidlist)
    for i in p:
        content[i] = None
        # first writes None at the passed-in indexes
    write(raidlist, [e for e in content if e != None])
    # then writes all the non-empty elements (those who aren't None)
    
def editAtIndex(raidlist, row, col, newValue, flag=None):
    content = read(raidlist)
    if not flag:
        content[row][col+2] = newValue
        # if there is no flag, then we write the value at
        # [row][col+2] because the first two elements are unmutable
        # for now
    elif flag == "x":
        # again, coordinates are handled separately because of the
        # raidlist format (should change)
        content[row][1] = (newValue, content[row][1][1])
    elif flag == "y":
        content[row][1] = (content[row][1][0], newValue)
    # finally we write the modified content
    write(raidlist, content)

def deleteAll(raidlist):
    # deletes everything in raidlist
    open(raidlist, "w").close()

def raid(raidlist):
    """ Sends all the raids contained within the raidlist """
    # content is in the format [[t, (x, y), t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11], [...], ...]
    # where t is the send type (2 = reinforcement, 3 = attack, 4 = raid), (x, y) is the coordinates
    # and t1 -> t11 is from the basic troop to the hero
    content = read(raidlist)
    for e in content:
        r = b.open("build.php?tt=2&id=39")
        b.select_form("snd")
        b.form["c"] = [str(e[0])]
        b.form["x"] = str(e[1][0])
        b.form["y"] = str(e[1][1])
        for i in range(len(e[2:])):
            if i != 10:
                b.form["t"+str(i+1)] = str(e[2+i])
            else:
                # if we're sending element number 10 of e[2:] (t11 = Hero)
                # then we have to check if the hero's in town
                try:
                    b.form["t11"] = str(e[2+i])
                except:
                    pass
        # we submit once to prepare
        r = b.submit()
        # and once again to confirm
        b.select_form(nr=0)
        r = b.submit()
        yield 1
