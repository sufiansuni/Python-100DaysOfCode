# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

# pprint(sheet_data)

for row in sheet_data:
    if row['iataCode'] == '':
        row['iataCode'] = "TESTING"

data_manager.destination_data = sheet_data

# pprint (data_manager.destination_data)

data_manager.update_destination_codes()
