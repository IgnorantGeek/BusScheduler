import NextBus as NB 


cyride = NB.Agency('cyride')
cyride.initRoutes()
cyride.initAllStops()
print("Agency Initialized.")
window = NB.Window(cyride)
window.loop()