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

query = next.get_predictions_for_stop(local, towers)

#so query will store the results of the get_predictions call
#and I just need to parse that for relevant info