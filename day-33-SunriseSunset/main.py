from tkinter import OFF
import requests
import datetime

MY_LAT = 1.441120
MY_LNG = 103.779230

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunrise_hour = sunrise.split("T")[1].split(':')[0]
sunset_hour = sunset.split("T")[1].split(':')[0]
time_now = datetime.datetime.now()

print(sunrise_hour)
print(sunset_hour)
print(time_now.hour)
