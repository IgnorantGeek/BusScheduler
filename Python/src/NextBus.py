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

#Do I really need all this class stuff? Can I just have like an Agency class? You create that with a tag and it fills out some base stuff
#then you can use some of the functions to figure out what routes and stops you want. There can be a function that will pop up a window that
#tracks live predictions for whatever routes you specify. Would be easier than the class stuff, with the exception of the Agency class


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
    #an instance of the nextbus monitoring class. I want to build in a lot of functionality. Allowing for tracking specific stops,
    #specific routes, or whole agencies. Need to figure out how I want to implement this. Think about it from a user perspective.
    #How will someone use this library? What will someone be doing with said library?

#Creation of an agency will call the agencyList Feed URL and check that it is a valid agency with NextBus
class Agency:
    tag = ''
    title = ''
    region = ''
    routes = []

    class Route:
        tag = ''
        title = ''
        stops = []

        def __init__(self, tag, title):
            self.tag = tag
            self.title = title

        def initStops(self, Agency):
            url = routeConfig + Agency.tag + '&r=' + self.tag
            file = urlopen(url)
            tree = ET.parse(file)
            root = tree.getroot()
            route = root[0]
            for stop in route.findall('stop'):
                self.stops.append(Agency.Stop(stop.get('tag'), stop.get('title')))

    class Stop:
        tag = ''
        location = ''
        def __init(self, tag, locationTitle):
            self.tag = tag
            self.location = locationTitle

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
        self.initRoutes()

    def printRoutes(self):
        for route in self.routes:
            print(route.title)
            print(route.tag)
            print
    
    def initRoutes(self):
        file = urlopen(routeList + self.tag)
        tree = ET.parse(file)
        root = tree.getroot()
        for route in root.findall('route'):
            tag = route.get('tag')
            title = route.get('title')
            newRoute = self.Route(tag, title)
            self.routes.append(newRoute)
    
    def initAllStops(self):
        for route in self.routes:
            route.initStops(self)
        