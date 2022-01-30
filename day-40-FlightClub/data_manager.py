import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        endpoint = "https://api.sheety.co/2441cf3e4d3f8a33fc100d25122c24f8/flightDeals/prices"

        response = requests.get(url=endpoint)

        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for row in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(
                url=f"https://api.sheety.co/2441cf3e4d3f8a33fc100d25122c24f8/flightDeals/prices/{row['id']}",
                json=new_data
            )
            print(response.text)
    
    def get_customer_emails(self):
        customers_endpoint = "https://api.sheety.co/2441cf3e4d3f8a33fc100d25122c24f8/flightDeals/users"
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
