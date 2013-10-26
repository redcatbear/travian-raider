#!/usr/bin/python

__author__ = "Adrian Torres"
__version__ = "1.3"

from Tkinter import *
import ttk
import time as timelib
import TravianRaider
import threading
import parsing

## Windows ##

# main window
root = Tk()
root.title("Travian Raider")

# frame holding all widgets
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# frame holding the troop view
troopview = ttk.Frame(mainframe, padding="3 3 12 12")
troopview.grid(column=2, row=6, sticky=(W))
troopview.columnconfigure(0, weight=1)
troopview.rowconfigure(0, weight=1)

# frame for raidlist manager
raidlistM = ttk.Frame(mainframe, padding="3 3 12 12")
raidlistM.grid(column=2, row=7, sticky=(N, W, E, S))
raidlistM.columnconfigure(0, weight=1)
raidlistM.rowconfigure(0, weight=1)

## Variables ##

# if the user is logged into the server
isLogged = False
usr = StringVar()
pwd = StringVar()
srv = StringVar()
# sets the server to the s7 COM server by default
srv.set("http://ts7.travian.com/")
# troop images, format: [[troop x for romans, troop x for gauls, troop x for teutons], [...]]
troops = []
for i in range(1, 11):
    troops.append([PhotoImage(file="img/t"+str(i)+"_R.gif"),
    		   PhotoImage(file="img/t"+str(i)+"_G.gif"),
    		   PhotoImage(file="img/t"+str(i)+"_T.gif")])
# hero is common for all, t11
troops.append(PhotoImage(file="img/hero.gif"))
# crossed swords image
swords = PhotoImage(file="img/swords.gif")
# textvariable for each entry label in troop selection screen, 0 by default
truppen = [StringVar() for i in range(11)]
for e in truppen:
	e.set("0")
# textvariable for each label in troop view screnn, 0 by default
truppenTV = [StringVar() for i in range(11)]
# coordinate variables
x = StringVar()
y = StringVar()
# tells the player if the connection to the server was successful
logged = StringVar()

raidManagerVar = []

## Widgets ##

# combobox for choosing tribe
tribe = ttk.Combobox(mainframe)
tribe.grid(column=2, row=4, sticky=(W, E))
tribe["state"] = "readonly"
tribe["values"] = ("Roman", "Gaul", "Teuton")
tribe.current(0)

## Entries ##

# username
usr_entry = ttk.Entry(mainframe, width=12, textvariable=usr)
usr_entry.grid(column=2, row=1, sticky=(W, E))

# password
pwd_entry = ttk.Entry(mainframe, width=12, textvariable=pwd, show="*")
pwd_entry.grid(column=2, row=2, sticky=(W, E))

# server
srv_entry = ttk.Entry(mainframe, width=12, textvariable=srv)
srv_entry.grid(column=2, row=3, sticky=(W, E))

# from t1 to t11 -> troop selection screen
t1_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[0])
t1_entry.grid(column=3, row=2, sticky=(W, E))

t2_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[1])
t2_entry.grid(column=3, row=4, sticky=(W, E))

t3_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[2])
t3_entry.grid(column=4, row=2, sticky=(W, E))

t4_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[3])
t4_entry.grid(column=4, row=4, sticky=(W, E))

t5_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[4])
t5_entry.grid(column=5, row=2, sticky=(W, E))

t6_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[5])
t6_entry.grid(column=5, row=4, sticky=(W, E))

t7_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[6])
t7_entry.grid(column=6, row=2, sticky=(W, E))

t8_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[7])
t8_entry.grid(column=6, row=4, sticky=(W, E))

t9_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[8])
t9_entry.grid(column=7, row=2, sticky=(W, E))

t10_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[9])
t10_entry.grid(column=7, row=4, sticky=(W, E))

t11_entry = ttk.Entry(mainframe, width=3, textvariable=truppen[10])
t11_entry.grid(column=8, row=2, sticky=(W, E))

# x coordinate
x_entry = ttk.Entry(mainframe, width=3, textvariable=x)
x_entry.grid(column=4, row=5, sticky=(W, E))

# y coordinate
y_entry = ttk.Entry(mainframe, width=3, textvariable=y)
y_entry.grid(column=6, row=5, sticky=(W, E))

## Labels ##

# from t1 to t11 -> troop image label
t1 = ttk.Label(mainframe)
t1.grid(column=3, row=1, sticky=(W, E))

t2 = ttk.Label(mainframe)
t2.grid(column=3, row=3, sticky=(W, E))

t3 = ttk.Label(mainframe)
t3.grid(column=4, row=1, sticky=(W, E))

t4 = ttk.Label(mainframe)
t4.grid(column=4, row=3, sticky=(W, E))

t5 = ttk.Label(mainframe)
t5.grid(column=5, row=1, sticky=(W, E))

t6 = ttk.Label(mainframe)
t6.grid(column=5, row=3, sticky=(W, E))

t7 = ttk.Label(mainframe)
t7.grid(column=6, row=1, sticky=(W, E))

t8 = ttk.Label(mainframe)
t8.grid(column=6, row=3, sticky=(W, E))

t9 = ttk.Label(mainframe)
t9.grid(column=7, row=1, sticky=(W, E))

t10 = ttk.Label(mainframe)
t10.grid(column=7, row=3, sticky=(W, E))

t11 = ttk.Label(mainframe)
t11.grid(column=8, row=1, sticky=(W, E))

t1tv = ttk.Label(troopview)
t1tv.grid(column=2, row=1, sticky=(W, E))

t2tv = ttk.Label(troopview)
t2tv.grid(column=3, row=1, sticky=(W, E))

t3tv = ttk.Label(troopview)
t3tv.grid(column=4, row=1, sticky=(W, E))

t4tv = ttk.Label(troopview)
t4tv.grid(column=5, row=1, sticky=(W, E))

t5tv = ttk.Label(troopview)
t5tv.grid(column=6, row=1, sticky=(W, E))

t6tv = ttk.Label(troopview)
t6tv.grid(column=7, row=1, sticky=(W, E))

t7tv = ttk.Label(troopview)
t7tv.grid(column=8, row=1, sticky=(W, E))

t8tv = ttk.Label(troopview)
t8tv.grid(column=9, row=1, sticky=(W, E))

t9tv = ttk.Label(troopview)
t9tv.grid(column=10, row=1, sticky=(W, E))

t10tv = ttk.Label(troopview)
t10tv.grid(column=11, row=1, sticky=(W, E))

t11tv = ttk.Label(troopview)
t11tv.grid(column=12, row=1, sticky=(W, E))

troopsRM = []
for i in range(13):
    troopsRM.append(ttk.Label(raidlistM))
    troopsRM[i].grid(column=i+2, row=1)
    if i == 11:
        troopsRM[i]["text"] = "X"
    elif i == 12:
        troopsRM[i]["text"] = "Y"

for i in range(len(truppenTV)):
    ttk.Label(troopview, textvariable=truppenTV[i]).grid(column=i+2, row=2)

# puts all the labels into a convenient list, for further manipulation
troopLabels = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
troopLabelsTV = [t1tv, t2tv, t3tv, t4tv, t5tv, t6tv, t7tv, t8tv, t9tv, t10tv]

# coordinates labels
ttk.Label(mainframe, text="X:").grid(column=3, row=5, sticky=(W, E))
ttk.Label(mainframe, text="Y:").grid(column=5, row=5, sticky=(W, E))
# islogged label
loggedLabel = ttk.Label(mainframe, textvariable=logged)
loggedLabel.grid(column=1, row=5, sticky=(E))

# username, password, server and tribe labels
ttk.Label(mainframe, text="Username: ").grid(column=1, row=1, sticky=(E))
ttk.Label(mainframe, text="Password: ").grid(column=1, row=2, sticky=(E))
ttk.Label(mainframe, text="Server URL: ").grid(column=1, row=3, sticky=(E))
ttk.Label(mainframe, text="Tribe: ").grid(column=1, row=4, sticky=(E))

raidManagerCheck = []
raidManagerLabels = []

## Functions ##

def removeRaid():
    try:
        ind = []
        # holds the indexes of checked boxes
        for i in range(len(raidManagerCheck)):
            if raidManagerVar[i].get() == 1:
                # if the checkboxes is True, then we append to ind
                ind.append(i)
        with open("raidlist.txt", "r") as f:
            # we open, we read, we store, we close
            text = f.read()
        # we split by \n
        rawData = text.split("\n")
        raidlist = [eval(x) for x in rawData[:-1]]
        # we evaluate each element of rawData, except the last one
        # which is an empty string
        for i in ind:
            # we delete the corresponding element from these lists
            del raidlist[i]
            raidManagerCheck[i].grid_forget()
            # grid_forget() ungrids the element from the screen
            del raidManagerCheck[i]
            del raidManagerVar[i]
            for e in raidManagerLabels[i]:
                # we grid forget each element (label) in the raidManagerLabels[i]
                e.grid_forget()
            del raidManagerLabels[i]
        with open("raidlist.txt", "w") as f:
            # we open, we write, we close
            for e in raidlist:
                f.write(repr(e) + "\n")
    except:
        pass

def combo(*args):
    # executed when the combobox's state has been changed
    try:
        # tries to get the current combobox state
        t = tribe.current()
    except:
            pass
    if t == 0:
            # if the combobox selection index is 0, then romans is the chosen tribe
        for i in range(len(troopLabels)):
            troopLabels[i]['image'] = troops[i][0]
        for i in range(len(troopLabelsTV)):
            troopLabelsTV[i]['image'] = troops[i][0]
        for i in range(len(troopsRM[:10])):
            troopsRM[i]['image'] = troops[i][0]
    elif t == 1:
            # if the combobox selection index is 1, then gauls is the chosen tribe
        for i in range(len(troopLabels)):
            troopLabels[i]['image'] = troops[i][1]
        for i in range(len(troopLabels)):
            troopLabelsTV[i]['image'] = troops[i][1]
        for i in range(len(troopsRM[:10])):
            troopsRM[i]['image'] = troops[i][1]
    else:
        # if the combobox selection index is 2, then teutons is the chosen tribe
        for i in range(len(troopLabels)):
            troopLabels[i]['image'] = troops[i][2]
        for i in range(len(troopLabels)):
            troopLabelsTV[i]['image'] = troops[i][2]
        for i in range(len(troopsRM[:10])):
            troopsRM[i]['image'] = troops[i][2]
    # finally, t11 is chosen for all tribes, the hero
    for e in truppenTV:
        e.set("0")
    t11['image'] = troops[-1]
    t11tv['image'] = troops[-1]
    troopsRM[10]['image'] = troops[-1]

def login():
    logButton.state(["disabled"])
    # executed when the login button is pressed, or return is pressed
    global isLogged
    # we use isLogged as a global, for other functions which won't work if the user isn't logged in
    try:
        # we try to get the variables required for logging in
        USR = usr.get()
        PWD = pwd.get()
        SRV = srv.get()
        # we assign isLogged to whatever login returns
        isLogged = TravianRaider.login(USR, PWD, SRV)
    except:
        pass
    if isLogged:
        # if the user successfully logged in, we send a positive message
        loggedLabel['foreground'] = "green"
        logged.set("Success!")
        # and then we clear the entry fields
        usr_entry.delete(0, 'end')
        pwd_entry.delete(0, 'end')
        displayIt()
    else:
        # if not, we send a negative message and we let the player
        # change his credentials
        loggedLabel['foreground'] = "red"
        logged.set("Failure!")
    timelib.sleep(2)
    logged.set("")
    logButton.state(["!disabled"])

def raid():
    # executed when the raid button is pressed, sends a raid
    # according to raidlist.txt
    if isLogged:
	# if the user is logged in, proceed to raid
    	TravianRaider.raidGoldless()
        loggedLabel['foreground'] = "green"
        logged.set("Raid successful!")
        timelib.sleep(2)
        logged.set("")
    else:
        loggedLabel['foreground'] = "red"
        logged.set("Not logged!")
        timelib.sleep(2)
        logged.set("")

def addToRaidlist(*args):
    try:
        # adds the current troop and coordinate setup to the raidlist.txt file
        values = [int(i.get()) for i in truppen]
        # values gets all the entry textvariables, casts them into integers
        # and makes a list of it
        q = ([4, (int(x.get()), int(y.get()))] + values)
        # q adds values to the basic parameters
        with open("raidlist.txt", "a") as f:
            f.write(repr(q)+"\n")
        # writes the string representation of q, which will then be
        # imported and evaluated by a TravianRaider function
    except:
        pass
    # we update the display
    displayRaidlist()

def troopDisplay(*args):
    try:
        truppen = parsing.totalTroops()
        for i in range(len(truppenTV)):
            truppenTV[i].set(truppen[i])
    except:
        loggedLabel['foreground'] = "red"
        logged.set("Not logged!")
        timelib.sleep(2)
        logged.set("")

def displayRaidlist(*args):
    with open("raidlist.txt", "r+") as f:
        # opens the raidlist
        text = f.read()
        # reads its contents
        nLines = text.count("\n")
        # counts the number of lines to see how many times does it have
        # to create the label widgets
        newText = text.split("\n")
        # we split it by newlines
        lists = [eval(x) for x in newText[:-1]]
        # we eval each string in newText, which is a list, except the
        # last element which is an empty string
    for i in range(1, nLines+1):
        toApp = []
        # toApp contains elements to append to raidManagerLabels, for
        # further manipulation (ungrid, delete)
        for j in range(2, 14):
            if j == 2:
                # if j == 2 then it's the coordinates tuple which we have
                # to process differently
                toApp.append(ttk.Label(raidlistM, text=lists[i-1][j-1][0]))
                toApp[0].grid(column=13, row=i+1, sticky=(W, E))
                toApp.append(ttk.Label(raidlistM, text=lists[i-1][j-1][1]))
                toApp[1].grid(column=14, row=i+1, sticky=(W, E))
            else:
                # normal widgets
                toApp.append(ttk.Label(raidlistM, text=lists[i-1][j-1]))
                toApp[j-1].grid(column=j-1, row=i+1, sticky=(W, E))
                # we add one IntVar object for each checkbox
        raidManagerVar.append(IntVar())
        # we append each checkbox to the checkbox list
        raidManagerCheck.append(ttk.Checkbutton(raidlistM, variable=raidManagerVar[i-1]))
        raidManagerCheck[i-1].grid(column=0, row=i+1)
        # we append the list of widgets to raidManagerLabels
        raidManagerLabels.append(toApp)
        
## Other ##

def logIt(*args):
    # creates and starts a thread whenever it's called
    # which allows for logging in again if login failed
    t1 = threading.Thread(target=login)
    t1.start()

def raidIt(*args):
    # creates and starts a thread whenever it's called
    # which allows for sending multiple raids multiple times
    # without exiting the program
    t2 = threading.Thread(target=raid)
    t2.start()

def displayIt(*args):
    # creates and starts a thread whenever it's called
    t3 = threading.Thread(target=troopDisplay)
    t3.start()

def removeIt(*args):
    t4 = threading.Thread(target=removeRaid)
    t4.start()

## Buttons ##

logButton = ttk.Button(mainframe, text="Log in", command=logIt)
logButton.grid(column=2, row=5, sticky=(W, E))
ttk.Button(mainframe, text="Add to raidlist", command=addToRaidlist).grid(column=3, row=6, columnspan=3, sticky=(W, E))
ttk.Button(mainframe, text="Raid!", image=swords, compound="left", command=raidIt).grid(column=6, row=6, columnspan=3, sticky=(W, E))
ttk.Button(mainframe, text="Display troops!", command=displayIt).grid(column=1, row=6, sticky=(W, E))
ttk.Button(mainframe, text="Delete", command=removeIt).grid(column=1, row=7, sticky=(W, E))

## Execution ##

combo()
displayRaidlist()

# fives each child of mainframe 5px padding on all sides
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

usr_entry.focus()
# sets the focus on the usr_entry entry widget
tribe.bind("<<ComboboxSelected>>", combo)
# when the combobox state is changed, executes the combo function
root.bind("<Return>", logIt)
# if return is pressed, the logIt function starts

# main loop
root.mainloop()
