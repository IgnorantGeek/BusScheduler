import nextbus
import Tkinter as tk
#import RPi.GPIO as GPIO for use when interfacing with the RPiO pins

#agency
cyride = 'cyride'

#routes
gn = '952'
gs = '951'
bn = '862'
bs = '861'

#stops
tturn = '8860'
storm = '8870'


#query section
def prediction_query(agency, stop_id):
    query = nextbus.get_predictions_for_stop(agency, stop_id)
    if not query.predictions:
        return -1
    else:
        return query.predictions[0].minutes

#display section
window = tk.Tk()
window.title('Next Arrivals at Storm St./Towers Turnaround')
window.geometry('650x100')

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
#        the window flashes when it is running, not a big deal
#        there is an error when closing the window because the loop tries to run again after it was destroyed.
#        sometimes the display gets messed up with what number to display