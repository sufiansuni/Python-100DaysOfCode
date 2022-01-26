from wsgiref import headers
import requests
from dotenv import load_dotenv
import os
import requests
from pprint import pprint

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
