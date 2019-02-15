import py_nextbus

client = py_nextbus.NextBusClient(output_format='json')
agencies = client.get_agency_list()