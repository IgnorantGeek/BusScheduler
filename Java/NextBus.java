//This will be a program in java that will interface with the nextbus public xml feed.
//I'm tired of python, so we need to figure out how to read the xml or json feed and scan for the data we need.

//XML for Iowa State Route List http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=cyride

import java.io.*;
import java.net.*;
import org.w3c.dom.*;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import java.lang.String;
import java.util.ArrayList;

public class NextBus
{
    ArrayList<Agency> agencies = new ArrayList<Agency>();
    
    public void add_agency_by_tag(String tag)
    {
        Agency n = new Agency(tag);
        agencies.add(n);
    }

    class Agency
    {
        //some info about the agency to use for this next bus instance.
        //will contain a list of routes and stops to monitor
        String tag, title, regionTitle;
        ArrayList<Route> routes = new ArrayList<Route>();
        ArrayList<Stop> stops = new ArrayList<Stop>();
        Agency(String tag)
        {
            Document query = XMLtoDoc.routeConfig(tag);
            if (query == null) 
            {
                System.out.println("Could not find an agency with tag: " + tag);
                return;
            } //check this line, make sure we are handling errors in the correct way.
            NodeList list = query.getElementsByTagName("route");
            for (int i = 0; i < list.getLength(); i++)
            {
                Route newroute = new Route();
                Node n = list.item(i);
                if (n.getNodeType() == Node.ELEMENT_NODE) 
                {
                    Element e = (Element) n;
                    newroute.tag = e.getAttribute("tag");
                    newroute.title = e.getAttribute("title");
                    NodeList stops = e.getElementsByTagName("stop");
                    for (int j = 0; j < stops.getLength(); j++)
                    {
                        Stop newstop = new Stop();
                        Node m = stops.item(j);
                        if (m.getNodeType() == Node.ELEMENT_NODE)
                        {
                            Element E = (Element) m;
                            newstop.tag = E.getAttribute("tag");
                            newstop.title = E.getAttribute("title");
                            newroute.stops.add(newstop);
                            this.stops.add(newstop);
                        }
                    }
                }
                this.routes.add(newroute);
            }
        }

        public void print_routes()
        {
            for (int i = 0; i < routes.size(); i++)
            {
                routes.get(i).print();
            }
        }
    }

    class Route
    {
        //a route in the specified agency
        String tag, title;
        ArrayList<Stop> stops = new ArrayList<Stop>();
        public void print()
        {
            System.out.println("Route Title: " + this.title);
            System.out.println("Route Tag: " + this.tag);
        }
        public void print_stops()
        {
            System.out.println("Stops on route " + this.title + ": \n");
            for (int i = 0; i < stops.size(); i++)
            {
                stops.get(i).print();
            }
        }
    }

    class Stop
    {
        //a stop in the specified agency
        String tag, title;
        public void print()
        {
            System.out.println("Stop Title: " + this.title);
            System.out.println("Stop Tag: " + this.tag);
        }
    }   
}