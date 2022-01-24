from dotenv import load_dotenv
import os
import requests

load_dotenv()

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")


def get_exercise_info():
    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    params = {
        "query": input("Tell me which exercises you did: ")
    }

    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY
    }

    response = requests.post(
        url=endpoint,
        json=params,
        headers=headers)

    response.raise_for_status()
    print(response.text)


def get_exercise_sheet():
    endpoint = "https://api.sheety.co/2441cf3e4d3f8a33fc100d25122c24f8/myWorkouts/workouts"

    response = requests.get(url=endpoint)

    response.raise_for_status()
    print(response.json())


# get_exercise_info()
get_exercise_sheet()
