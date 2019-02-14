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