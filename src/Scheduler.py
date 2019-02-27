import NextBus as nb
import Tkinter as tk
import tkMessageBox
import time

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

def print_stops_for_route(agency, route_id):
        stops = nb.get_route_config(agency, route_id)
        print "Stops for the {} route".format(stops.route.title)
        for stop in stops.stops:
                print "Stop at {} has stop_id {}".format(stop.title, stop.tag)

def print_route_tags(agency):
        routes = nb.get_all_routes_for_agency(agency)
        print "Routes for agency {}".format(agency)
        for route in routes:
                print "Route {} has route_tag {}".format(route.title, route.tag)


#       arrival_times is the array of times to update in a loop. They are StringVars and so should 
#       get updated in the window whenever the StringVar array is updated
def prediction_to_window(agency, stop_id, *route_id):
        arrival_times = []
        def callback():
                if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
                        window.destroy()
        window = tk.Tk()
        window.protocol("WM_DELETE_WINDOW", callback)
        query = nb.get_predictions_for_stop(agency, stop_id)
        window.title('Next Arrivals at ' + query.stop_title)
        i = 0
        #this loop sets the window
        for route in route_id:
                for prediction in query.predictions:
                        route_title = prediction.direction.route.title
                        arrival_time = tk.StringVar()
                        arrival_time.set(prediction.minutes)
                        arrival_times.append(arrival_time)
                        if prediction.direction.route.tag == route:
                                tk.Label(window, text= route_title + ': ', font=("Arial Bold", 30)).grid(row=i,column=0)
                                tk.Label(window, textvariable=arrival_time, font=("Arial Bold", 30)).grid(row=i,column=1)
                                tk.Label(window, text=" minutes", font=("Arial Bold", 30)).grid(row=i,column=2)
                                window.update()
                                i = i+1
                                break
        
        #this loop should update all the times until the window is closed. Can't detect when the window closes properly
        for times in arrival_times:
                newq = nb.get_predictions_for_stop(agency, stop_id)
                for route in route_id:
                        for prediction in newq.predictions:
                                newtime = prediction.minutes
                                if prediction.direction.route.tag == route:
                                        times.set(newtime)
                                        break
                #time.sleep(20)

        window.mainloop()

#this function isn't really used anymore. Going to keep it around for the hell of it
def update_route_time(window, row_num, agency, stop_id, route_id):
        query = nb.get_predictions_for_stop(agency, stop_id)
        for prediction in query.predictions:
                prediction_tag = prediction.direction.route.tag
                arrival = prediction.minutes
                if prediction_tag == route_id:
                        tk.Label(window, text=arrival, font=("Arial Bold", 30)).grid(row=row_num,column=1)

#MAIN:
print_route_tags(cyride)
print('\n')
print_stops_for_route(cyride,gs)
#prediction_to_window(cyride,lfriley,gs,blue)

#ISSUES: 
#       I can't figure out how to run a loop until the window closes. The window.state() == 'normal' feature doesn't seem
#       to work properly. Either run into an infinite loop scenario or have to throw a python error every time the app closes
#
#       Potential idea: Create Arrival time classes that will store the the arrival time of a specific route. Then have a function
#       that will pull a new query from get_predictions, update all the arrival times, and refresh the tkinter window.