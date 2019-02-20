import nextbus
import Tkinter as tk

#ISU agency
cyride = 'cyride'

#routes for testing
gn = '952'
gs = '951'
bn = '862'
bs = '861'

#stops for testing
tturn = '8860'
storm = '8870'

def print_stops_for_route(agency, route_id):
        stops = nextbus.get_route_config(agency, route_id)
        for stop in stops.stops:
                print "Stop at {} has stop_id {}".format(stop.title, stop.tag)

def print_route_tags(agency):
        routes = nextbus.get_all_routes_for_agency(agency)
        for route in routes:
                print "Route {} has route_tag {}".format(route.title, route.tag)

# Can probably integrate the above method here. Pass in the routes and stops you want predictions for and it will
# pull up a window with the readout
def prediction_to_window(agency, stop_id, *route_id):
        window = tk.Tk()
        query = nextbus.get_predictions_for_stop(agency, stop_id) #scan this query for the specified route_id
        #how can we pass in multiple routes? We don't want endless parameters so how can we allow a user to 
        #used send_to_window(agency, stop_id, route_id, route_id, route_id, etc.)
        for route in route_id:
                for prediction in query.predictions:
                        #search for the specified route id in predictions, if you get a match send the first prediction
                        #you find to the window method below. So we will probably need to run that in here
                        route_title = prediction.direction.route.title
                        arrival_time = prediction.minutes
                        if prediction.direction.route.tag == route:
                                tk.Label(window, text= route_title + ': ', font=("Arial Bold", 30)).grid(row=0,column=0)
                                tk.Label(window, text=arrival_time, font=("Arial Bold", 30)).grid(row=0,column=1)
                                tk.Label(window, text=" minutes", font=("Arial Bold", 30)).grid(row=0,column=2)
                                window.update()
                                break
        window.title('Next Arrivals')
        window.mainloop()


#main
#prediction_to_window(cyride,tturn, gn, bn)

#issues: 
#        the window flashes when it is running, not a big  but kind of annoying
#        fixed the error when closing but now the window does not continuously update. Need a loop at the end of prediction_to_window() method
#        sometimes the display gets messed up with what number to display
#        need to fix the labels so this can be more of a multipurpose app
#        handle printing -1 value for no prediction (fix with update v1.0)