import nextbus as next

#agency
local = 'cyride'

#routes
gsouth = '951'
gnorth = '952'
bsouth = '861'
bnorth = '862'

#stops
towers = '8860'

print(next.get_predictions_for_stop(local, towers))

#so I know how to pull the data into an xml from nextbus. Now I just need to parse the xml for relevent data
#then print the data wherever it needs to go