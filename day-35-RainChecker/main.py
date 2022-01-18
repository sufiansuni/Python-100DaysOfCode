from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Constants
load_dotenv()

WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
MY_LAT = 1.441120
MY_LNG = 103.779230

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

client = Client(account_sid, auth_token, http_client=proxy_client)

TWILIO_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']
MY_PHONE_NUMBER = os.environ['MY_PHONE_NUMBER']


def get_weather_data():
    weather_base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    weather_params = {
        "lat": MY_LAT,
        "lon": MY_LNG,
        "exclude": "current,minutely,daily",
        "appid": WEATHER_API_KEY
    }

    response = requests.get(url=weather_base_url, params=weather_params)
    response.raise_for_status()
    data = response.json()
    return data


def check_rain():
    hourly_data = get_weather_data()["hourly"][:12]
    # print(hourly_data)
    for i in range(len(hourly_data)):
        weather_id = int(hourly_data[i]["weather"][0]["id"])
        if weather_id < 700:
            # print(f"Raining in {i} hours")
            return True
    return False


if check_rain():
    message = client.messages \
        .create(
            body="Bring An Umbrella. Rain in the next 12 hours.",
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )
    print("Rain incoming. SMS Sent. Message SID: ", message.sid)
else:
    print("Fine weather. No need to notify user.")
