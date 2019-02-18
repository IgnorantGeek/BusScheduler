import nextbus
import Tkinter as tk
#import RPi.GPIO as GPIO for use when interfacing with the RPiO pins

#agency
cyride = 'cyride'

#routes
gn = '952'
gs = '951' #probably dont need this
bn = '862'
bs = '861' #or this

#stops
tturn = '8860'
storm = '8870'


#query section
goldq = nextbus.get_predictions_for_stop(cyride, tturn)
brownq = nextbus.get_predictions_for_stop(cyride, storm)
if not goldq.predictions:
    goldtime = -1
    #keeps there from being an error when using the pop command
else:
    goldtime = goldq.predictions[0].minutes
if not brownq.predictions:
    browntime = -1
else:
    browntime = brownq.predictions[0].minutes


#display section
window = tk.Tk()
#window.geometry('600x100') leaves this in auto 
window.title('Next Arrivals at Storm St./Towers Turnaround')
tk.Label(window, text="Next Gold North: ", font=("Arial Bold", 30)).grid(row=0,column=0)
tk.Label(window, text=goldtime, font=("Arial Bold", 30)).grid(row=0,column=1)
tk.Label(window, text="Next Brown North: ", font=("Arial Bold", 30)).grid(row=1,column=0)
tk.Label(window, text=browntime, font=("Arial Bold", 30)).grid(row=1,column=1)


#the loop. We will need to run it and then refresh every so often (depending on the max pull freqency)
window.mainloop()
