#!/usr/bin/env python
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

#It could help. We can just see what data we get from the predictions that will be the active requests. Do we create a window class? You could 
#Pass in agencies that you want to track and be able to switch between them in a window. That would be super cool if we can get it to work.


import xml.etree.ElementTree as ET
from urllib2 import urlopen
import tkinter as tk

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

# Need to handle instances where someone isn't able to create their agency. Essentially handle times where someone enters the wrong tag




class Agency:
    tag = ''
    title = ''
    region = ''
    routes = []

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
        self.initAgency()
    
    class Route:
        tag = ''
        title = ''
        stops = []

        def __init__(self, tag, title):
            self.tag = tag
            self.title = title
    
    class Stop:
        tag = ''
        location = ''

        def __init__(self, tag, locationTitle):
            self.tag = tag
            self.location = locationTitle

    def printRoutes(self):
        for route in self.routes:
            print(route.title)
            print(route.tag)
            print
    
    def initAgency(self):
        file = urlopen(routeConfig + self.tag)
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            newRoute = self.Route(child.attrib.get('tag'), child.attrib.get('title'))
            for grandchild in child:
                if grandchild.tag == 'stop':
                    newStop = self.Stop(grandchild.attrib.get('tag'), grandchild.attrib.get('title'))
                    newRoute.stops.append(newStop)
            self.routes.append(newRoute)

    

#tk.mainloop is a substitute for the following while loop:
# while True:
#   tk.update_idletasks()
#   tk.update()
class Window:
    win = tk.Tk()
    agency = ''

    def __init__(self, Agency):
        self.win.title(Agency.title + " Predictions")
        self.agency = Agency
        self.win.geometry("500x200") #change me to make window bigger
    
    def loop(self):
        self.win.mainloop()