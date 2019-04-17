#ISU agency
cyride = 'cyride'

#routes for testing
gn = '952'
gs = '951'
bn = '862'
bs = '861'
orange = '940'
card = '930'
blue = '830'

#stops for testing
tturn = '8860'
storm = '8870'
bessey = '2500'
laverne = '2040'
lfriley = '2041'


import xml.etree.ElementTree as ET
from urllib2 import urlopen

agencyList = "http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList"
routeList = "http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a="
routeConfig = "http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a="

def printAgencies():
    file = urlopen(agencyList)
    tree = ET.parse(file)
    root = tree.getroot()
    for agency in root.findall('agency'):
        print("Title: {}".format(agency.get('title')))
        print("Tag: {} ".format(agency.get('tag')))
        print("Region: {}\n".format(agency.get('regionTitle')))

class NextBus:
    #an instance of the nextbus monitoring class. I want to build in a lot of functionality. Allowing for tracking specific stops,
    #specific routes, or whole agencies. Need to figure out how I want to implement this. Think about it from a user perspective.
    #How will someone use this library? What will someone be doing with said library?
    agencies = []
    routes = []
    stops = []


class Agency:
    tag = ''
    title = ''
    region = ''

    def __init__(self, tag):
        file = urlopen(agencyList)
        tree = ET.parse(file)
        root = tree.getroot()
        for agency in root.findall('agency'):
            if agency.get('tag') == tag:
                self.tag = agency.get('tag')
                self.title = agency.get('title')
                self.region = agency.get('regionTitle')
                break

class Route:
    tag = ''
    title = ''
    stops = []

    def __init__(self, tag, title):
        self.tag = tag
        self.title = title

    def printStops(self, agencyTag):
        url = routeConfig + 'agencyTag' + '&r=' + self.tag
        file = urlopen(url)
        tree = ET.parse(file)
        root = tree.getroot()
        route = root[0]
        for stop in route.findall('stop'):
            print("Stop Title: {}".format(stop.get('title')))
            print("Stop Tag: {}\n".format(stop.get('tag')))

class Stop:
    x = 6