import nextbus
import Tkinter as tk

#ISU agency
cyride = 'cyride'

#routes I use
gn = '952'
gs = '951'
bn = '862'
bs = '861'

#stops by me
tturn = '8860'
storm = '8870'

def get_stops_for_route(agency, route):
        stops = nextbus.get_route_config(agency, route)
        for stop in stops.stops:
                print "Stop at {} has stop_id {}".format(stop.title, stop.tag)

def get_route_tags(agency):
        routes = nextbus.get_all_routes_for_agency(agency)
        for route in routes:
                print "Route {} has route_tag {}".format(route.title, route.tag)

def prediction_query(agency, stop_id):
        query = nextbus.get_predictions_for_stop(agency, stop_id)
        if not query.predictions:
                return -1
        else:
                return query.predictions[0].minutes

# Can probably integrate the above method here. Pass in the routes and stops you want predictions for and it will
# pull up a window with the readout
def send_to_window():
        window = tk.Tk()
        window.title('Next Arrivals at Storm St./Towers Turnaround')
        while window:
                goldtime = prediction_query(cyride, tturn)
                browntime = prediction_query(cyride, storm)
                tk.Label(window, text="Next Gold North: ", font=("Arial Bold", 30)).grid(row=0,column=0)
                tk.Label(window, text=goldtime, font=("Arial Bold", 30)).grid(row=0,column=1)
                tk.Label(window, text="  minutes", font=("Arial Bold", 30)).grid(row=0,column=2)
                tk.Label(window, text="Next Brown North: ", font=("Arial Bold", 30)).grid(row=1,column=0)
                tk.Label(window, text=browntime, font=("Arial Bold", 30)).grid(row=1,column=1)
                tk.Label(window, text="  minutes", font=("Arial Bold", 30)).grid(row=1,column=2)
                window.update()
        window.mainloop()


#issues: 
#        the window flashes when it is running, not a big  but kind of annoying
#        there is a python error when closing the window because the loop tries to run again after it was destroyed, error in tk.Label()
#        sometimes the display gets messed up with what number to display **hasnt happened in a while, untested**
#        need to fix the labels so this can be more of a multipurpose app
#        handle printing -1 value for no prediction (fix with update v1.0)