import twill
import sys
sys.path.append("beautifulsoup")
from bs4 import BeautifulSoup
from StringIO import StringIO

# all twill output will be sent to a StringIO object and then dumped
twill.set_output(StringIO())

def troopParsing(soup, isHome, parsedSoup=None):
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

def troops():
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
    twill.commands.go(incomingUrl)
    soupIncoming = BeautifulSoup(twill.commands.show())
    twill.commands.go(outgoingUrl)
    soupOutgoing = BeautifulSoup(twill.commands.show())
    twill.commands.go(homeUrl)
    soupHome = BeautifulSoup(twill.commands.show())
    twill.commands.go(otherUrl)
    soupOther = BeautifulSoup(twill.commands.show())
    # finally, we assign the parsed troops to an entry in the dictionary
    truppen["incoming"] = troopParsing(soupIncoming, False)
    truppen["outgoing"] = troopParsing(soupOutgoing, False)
    truppen["home"] = troopParsing(soupHome, True)
    truppen["other"] = troopParsing(soupOther, False)
    return truppen
	
def totalTroops():
    truppen = troops()
    res = [0 for x in range(11)]
    for e in truppen:
        for k in range(len(truppen[e])):
            for i in range(len(truppen[e][k])):
                res[i] += truppen[e][k][i]
    return res
