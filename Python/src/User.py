import NextBus as NB
import time 

Test = NB.Agency('cyride')
print(Test.title)
print(Test.region)

Test.printRoutes()
#NB.printAgencies()