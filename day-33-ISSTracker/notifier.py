from asyncore import loop
import requests
from datetime import datetime
import time

MY_LAT = 1.441120
MY_LNG = 103.779230

# Your position is within +5 or -5 degrees of the ISS position.

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def nearISS():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT+5) and (MY_LNG - 5) <= iss_longitude <= (MY_LNG+5):
        return True
    else:
        return False


def nightTime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)

    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


programOn = True

while programOn:
    if nearISS() and nightTime():
        # Supposed to send email
        print("Look Up! ISS Nearby!")
    else:
        print("Waiting...")
    time.sleep(60)
