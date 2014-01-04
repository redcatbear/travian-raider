import sys
import mechanize
from bs4 import BeautifulSoup


def betterCropFinder(server, x, y, i=1):
    b = mechanize.Browser()
    r = b.open("http://croppers.travibot.com/?l=en&server=%s&x=%s&y=%s&page=%d" % (server, x, y, i))
    rawData = r.read()
    soup = BeautifulSoup(rawData)
    rawData = soup.find("div", {"id": "croppers"})
    data = rawData.findAll("tr")
    processedData = [e.getText(strip=True, separator=" ") for e in data]
    processedData = [str(e) for e in processedData[1:]]
    processedData = [e[2:].replace("|", " ").split() for e in processedData]
    td = [e.findAll("td") for e in data[1:]]
    oasesType = [e[4].findAll("img") for e in td]
    oT = []
    for e in oasesType:
        p = []
        for sub in e:
            for c in str(sub):
                if c.isdigit():
                    p.append(int(c))
        oT.append(p)
    oasesAttr = []
    for i in range(len(processedData)):
        sub = []
        for j in range(len(processedData[i][4:])):
            if len(sub) == 0:
                sub.append([oT[i][j], int(processedData[i][j+4])])
            else:
                for k in range(len(sub)):
                    if oT[i][j] == sub[k][0]:
                        sub[k][1] += int(processedData[i][j+4])
                        break
                else:
                    sub.append([oT[i][j], int(processedData[i][j+4])])
                        
            oasesAttr.append(sub)
        processedData[i] = processedData[i][:4] + oasesAttr[i]
    return processedData

def cropFinder(b, cp, r, crop):
    posUrl = "position_details.php?x=%d&y=%d"
    x = cp[0]
    y = cp[1]
    cropTiles = []
    newY = y - r
    while newY < y + r:
        newX = x - r
        while newX < x + r:
            resp = b.open(posUrl % (newX, newY))
            rawData = resp.read()
            try:
                soup = BeautifulSoup(rawData)
                processedData = soup.find("table", {"id": "distribution"})
                rawDist = str(processedData.getText(strip=True, separator=" "))
                processedDist = rawDist.split()
                print processedDist
                if processedDist[-1] == crop or processedDist[-2] == crop:
                    cropTiles.append((newX, newY))
            except:
                pass
            newX += 1
        newY += 1
    return cropTiles
                
def main(b):
    return cropFinder(b, (-68, 7), 50, "15")  

def checkTribe(b):
    r = b.open("dorf1.php")
    html = r.get_data()
    soup = BeautifulSoup(html)
    tribe = str(soup.find("img", {"class": "nation"}))
    # we find a html tag that contains the name of the tribe
    # and we return a number according to the tribe found
    #print tribe
    if "nation1" in tribe:
        return "R"
    elif "nation2" in tribe:
        return "T"
    else:
        return "G"

def troopParsing(b, soup, isHome, parsedSoup=None):
    """Parses the soup into a troop-number list"""
    troops = []
    # main list to be returned
    try:
        parsedSoup = soup.findAll("td", {"class": "unit"})
    except:
        pass
    # finds all td tags in the soup with the class "unit"
    if not isHome:
        for i in range(len(parsedSoup)/11):
            # the loop runs as many times as there are troops arriving/going/at home
            troopL = []
            # troopL stores each troop set
            j = 0
            while j < 11:
                # iterates through a set of 11 or more elements (t1->t11)
                troopL.append(int(parsedSoup[j].contents[0]))
                # appends the content of the parsedSoup to troopL, since it's
                # a number representation, we cast it into an int
                j += 1
            troops.append(troopL)
            # finally we append each troopL to troops
            parsedSoup = parsedSoup[j:]
            # we've already parsed the first 11 elements of parsedSoup
    else:
        parsedSoup = parsedSoup[:11]
        troops = troopParsing(None, False, parsedSoup)
    return troops

def troops(b):
    # returns incoming, outgoing and home troops in a dictionary
    truppen = {}
    incomingUrl = "build.php?gid=16&tt=1&filter=1"
    # the url filter for incoming troops
    outgoingUrl = "build.php?gid=16&tt=1&filter=2"
    # the url filter for outgoing troops
    homeUrl = "build.php?gid=16&tt=1&filter=3"
    # the url filter for troops at home
    otherUrl = "build.php?gid=16&tt=1&filter=4"
    # the url filter for troops at other places
    # the following goes to each filter url and gets the soup of each
    # set of troops
    r = b.open(incomingUrl)
    soupIncoming = BeautifulSoup(r.get_data())
    r = b.open(outgoingUrl)
    soupOutgoing = BeautifulSoup(r.get_data())
    r = b.open(homeUrl)
    soupHome = BeautifulSoup(r.get_data())
    r = b.open(otherUrl)
    soupOther = BeautifulSoup(r.get_data())
    # finally, we assign the parsed troops to an entry in the dictionary
    truppen["incoming"] = troopParsing(b, soupIncoming, False)
    truppen["outgoing"] = troopParsing(b, soupOutgoing, False)
    truppen["home"] = troopParsing(b, soupHome, True)
    truppen["other"] = troopParsing(b, soupOther, False)
    return truppen
	
def totalTroops(b):
    truppen = troops(b)
    res = [0 for x in range(11)]
    for e in truppen:
        for k in range(len(truppen[e])):
            for i in range(len(truppen[e][k])):
                res[i] += truppen[e][k][i]
    return res
    
#print betterCropFinder("tx3.travian.fr", 100, 82)
