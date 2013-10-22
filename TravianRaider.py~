# Note to you faggot: Don't run the program, because it'll fuck up my
# raids xD
import sys
sys.path.append("/twill")
from twill.commands import *
# import mechanize
# This is the main library, 3rd-party so you have to pip install it
# or easy_install it, you can use mechanize if you want a more complete
# library (which is built around twill), but this does the job for me
import time

# Constants required to create the connection
USERNAME = "Elkas"
PASSWORD = "090198jo"
SERVER = "http://tx3.travian.co.uk/"
add_extra_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36")

def login(usr=USERNAME, pwd=PASSWORD, srv=SERVER):
    go(srv)
    fv("login", "name", usr)
    fv("login", "password", pwd)
    submit()
    if url(srv + "dorf1.php"):
    	return True
    return False

def checkResources():
    go("dorf1.php")
    http = show()
    startRes = http.find("stockBar")
    endRes = http.find("</ul>", startRes)
    resHTTP = http[startRes:endRes]
    sWar = resHTTP.find("<span class=\"value\" id=\"stockBarWarehouse\">") + 43
    eWar = resHTTP.find("</span>", sWar)
    sGra = resHTTP.find("<span class=\"value\" id=\"stockBarGranary\">") + 41
    eGra = resHTTP.find("</span>", sGra)
    sW = resHTTP.find("<span id=\"l1\" class=\"value\">") + 28
    eW = resHTTP.find("</span>", sW)
    sC = resHTTP.find("<span id=\"l2\" class=\"value\">") + 28
    eC = resHTTP.find("</span>", sC)
    sS = resHTTP.find("<span id=\"l3\" class=\"value\">") + 28
    eS = resHTTP.find("</span>", sS)
    sP = resHTTP.find("<span id=\"l4\" class=\"value\">") + 28
    eP = resHTTP.find("</span>", sP)
    warehouse = resHTTP[sWar:eWar]
    granary = resHTTP[sGra:eGra]
    wood = resHTTP[sW:eW]
    clay = resHTTP[sC:eC]
    stone = resHTTP[sS:eS]
    wheat = resHTTP[sP:eP]
    return (((wood, clay, stone), warehouse), (wheat, granary))

def raidOnce():
    go("build.php?tt=99&id=39")
    # for some reason twill can't check the "mark all" checkbox on
    # travian's farmlist menu, so I have to loop over every checkbox
    # element and turn it on
    br = get_browser()
    f = br.get_form("2")
    i = 0
    for c in f.controls:
        if c.name:
            if c.name[:4] == "slot":
                i += 1
        
    for k in range(6, 6+i):
        fv("2", k, "on")
    submit()
    print "The raid has been started!"

def raidGoldless():
    with open("raidlist.txt", "r+") as f:
        rawData = f.read()
        processedData = rawData.split("\n")
        data = [eval(x) for x in processedData[:-1]]
    for e in data:
        go("build.php?tt=2&id=39")
        fv("snd", "t1", str(e[2]))
        fv("snd", "t2", str(e[3]))
        fv("snd", "t3", str(e[4]))
        fv("snd", "t4", str(e[5]))
        fv("snd", "t5", str(e[6]))
        fv("snd", "t6", str(e[7]))
        fv("snd", "t7", str(e[8]))
        fv("snd", "t8", str(e[9]))
        fv("snd", "t9", str(e[10]))
        fv("snd", "t10", str(e[11]))
        try:
            fv("snd", "t11", str(e[12]))
        except:
            pass
        fv("snd", "x", str(e[1][0]))
        fv("snd", "y", str(e[1][1]))
        fv("snd", "c", str(e[0]))
        fv("snd", "s1", "ok")
        submit()
        time.sleep(1)
        fv("2", "s1", "ok")
        submit()
        time.sleep(1)

def raidIndefinetely(gold, t):

    while True:
        # main loop, which would run forever, but I'd turn it off when waking up
        # or when I come back from college
        if gold:
            raidOnce()
        else:
            raidGoldless()
        start = time.time()
        while True:
            # basically waits until all the troops are back home before launching
            # the next raid
            now = time.time()
            if now - start >= t:
                break
            time.sleep(10)


        

#raidIndefinetely()
    
