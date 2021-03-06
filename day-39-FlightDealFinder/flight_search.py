from wsgiref import headers
import requests
from dotenv import load_dotenv
import os
import requests
from pprint import pprint
from flight_data import FlightData
load_dotenv()

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_iata(self, query):
        endpoint = "https://tequila-api.kiwi.com/locations/query"

        params = {
            "term": query,
            "location_types": "city"
        }

        headers = {
            "apikey": TEQUILA_API_KEY,
        }

        response = requests.get(url=endpoint, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["locations"][0]["code"]


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"https://tequila-api.kiwi.com/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ??{flight_data.price}")
        return flight_data
