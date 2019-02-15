import nextbus

query = nextbus.get_predictions_for_stop('cyride', '8860')

print('Towers Turnaround')
print('\n')

for preds in query.predictions:
    route = preds.direction.route.title
    print("Route {} will arrive in {} minutes".format(route,preds.minutes))