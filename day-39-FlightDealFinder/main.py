# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

# pprint(sheet_data)

flight_search = FlightSearch()

for row in sheet_data:
    row['iataCode'] = flight_search.get_iata(row['city'])

data_manager.destination_data = sheet_data

# pprint (data_manager.destination_data)

data_manager.update_destination_codes()
