import nextbus

query = nextbus.get_predictions_for_stop('cyride', '8860')

querystr = str(query) #converts the query to a string which I can parse
print(nextbus.get_predictions_for_stop('cyride', '8860'))