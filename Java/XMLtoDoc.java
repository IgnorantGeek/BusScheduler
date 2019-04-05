import java.io.*;
import java.net.*;
import org.w3c.dom.*;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import java.lang.String;
import java.util.ArrayList;
 
 
 /*TODO
    This class needs finished first. Figure out what methods we need to pull the info for a specific agency
    Will need prediction methods, config methods, etc. Anything that directly interacts with NextBus' public XML feed
    Needs to be in this class.
    */
    public class XMLtoDoc
    {
        //We want to pull the xml data and return it somehow. Figure out the implementation.
        static String agencyList = "http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList";
        static String routeList = "http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=";
        static String routeConfig = "http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=";
        static Document agencyList()
        {
            try {
                DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                DocumentBuilder db = dbf.newDocumentBuilder();
                Document doc = db.parse(new URL(agencyList).openStream());
                return doc;
            } catch (Exception e) {
                System.out.println(e.getMessage());
                return null;
            }
        }

        static Document routeList(String agencyTag)
        {
            String url = routeList.concat(agencyTag);
            try {
                DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                DocumentBuilder db = dbf.newDocumentBuilder();
                Document doc = db.parse(new URL(url).openStream());
                return doc;
            } catch (Exception e) {
                System.out.println(e.getMessage());
                return null;
            }
        }

        static Document routeConfig(String agencyTag)
        {
            String url = routeConfig.concat(agencyTag);
            try {
                DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                DocumentBuilder db = dbf.newDocumentBuilder();
                Document doc = db.parse(new URL(url).openStream());
                return doc;
            } catch (Exception e) {
                System.out.println(e.getMessage());
                return null;
            }
        }

        static Document routeConfig(String agencyTag, String routeTag)
        {
            String url = routeConfig.concat(agencyTag);
            url.concat("&r=");
            url.concat(routeTag);
            try {
                DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                DocumentBuilder db = dbf.newDocumentBuilder();
                Document doc = db.parse(new URL(url).openStream());
                return doc;
            } catch (Exception e) {
                System.out.println(e.getMessage());
                return null;
            }
        }
    }