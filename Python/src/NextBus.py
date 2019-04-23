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

def printRoutesInAgency(tag):
    file = urlopen(routeList + tag)
    tree = ET.parse(file)
    root = tree.getroot()
    for route in root.findall('route'):
        print("Route Title: {}".format(route.get('title')))
        print("Route Tag: {}".format(route.get('tag')))
# Need to handle instances where someone isn't able to create their agency. Essentially handle times where someone enters the wrong tag




class Agency:
    tag = ''
    title = ''
    region = ''
    routes = []
    stops = []

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
        title = ''

        def __init__(self, tag, title):
            self.tag = tag
            self.title = title
        
        def compare(self, Stop):
            if self.tag == Stop.tag:
                return True
            else:
                return False

    def printRoutes(self):
        for route in self.routes:
            print("{} : {}".format(route.title, route.tag))

    def printStopsInRoutes(self):
        for route in self.routes:
            for stop in route.stops:
                print("{} : {}".format(stop.title, stop.tag))
    
    def printStops(self):
        for stop in self.stops:
            print("{} : {}".format(stop.title, stop.tag))
    
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
                    i = 0
                    while i < len(self.stops):
                        
                        i += 1
            newRoute.stops.sort(key=lambda x: x.tag)
            self.routes.append(newRoute)
        self.stops.sort(key=lambda x: x.title)


class NextBus:

    class Window:
        #tk.mainloop is a substitute for the following while loop:
        # while True:
        #   tk.update_idletasks()
        #   tk.update()
        win = tk.Tk()
        agency = ''
        # Tkinter can:
        #               ________________                      
        #              |                |_____    __          
        #              |  SUCK MY ASS   |     |__|  |_________
        #              |________________|     |::|  |        /
        # /\**/\       |                \.____|::|__|      <  
        #( o_o  )_     |                      \::/  \._______\
        # (u--u   \_)  |                                      
        #  (||___   )==\                                      
        #,dP"/b/=( /P"/b\                                     
        #|8 || 8\=== || 8                                     
        #`b,  ,P  `b,  ,P                                     
        #  """`     """`                                      
        def __init__(self, Agency):
            self.win.title(Agency.title + " Predictions")
            self.agency = Agency
            self.win.geometry("500x200") #change me to make window bigger
        
        def loop(self):
            self.win.mainloop()



    class Cli:
        print("Welcome to the NextBus tracker, v1.6.31. Please enter a command, or type \'Help\' for a list of options.")
        response = raw_input('---> ')
        

class Prediction:
    x = 69
    #Under Construction