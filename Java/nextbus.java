//This will be a program in java that will interface with the nextbus public xml feed.
//I'm tired of python, so we need to figure out how to read the xml or json feed and scan for the data we need.

//XML for Iowa State Route List http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=cyride

import java.io.*;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.*;
import java.lang.String;
import java.until.ArrayList;

public class PullXml
{
    //We want to pull the xml data and return it somehow. Figure out the implementation.
    public static void fill_agency()
    {

    }
}

public class Agency
{
    //some info about the agency to use for this next bus instance.
    //will contain a list of routes and stops to monitor
    String tag, title, regionTitle;
    ArrayList<Route> routes = new ArrayList<Route>();
    ArralList<Stop> stops = new ArrayList<Stop>();
    Agency(String tag)
    {
        //need to pull the xml data, fill in all the data for this agency when created.
    }
}

public class Route
{
    //a route in the specified agency
    String tag, title;
    ArrayList<Stop> stops = new ArrayList<Stop>();
}

public class Stop
{
    //a stop in the specified agency
    String tag, title;
    ArrayList<Route> routes = new ArrayList<Route>();

}

public class nextbus
{
    java.util.ArrayList<Agency> agencies = new ArrayList<Agency>();
    
    public void add_agency_by_tag(String tag)
    {
        Agency n = new Agency(tag);
        agencies.add(n);
    }
}   