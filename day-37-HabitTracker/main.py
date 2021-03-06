# Imports
import requests
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")

# Step 1: Create A Pixela Account

pixela_base_url = "https://pixe.la/"
pixela_username = "sufiansuni"


def create_pixela_account():
    user_params = {
        "token": PIXELA_TOKEN,
        "username": pixela_username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(
        url=f"{pixela_base_url}v1/users", json=user_params)
    # response.raise_for_status()
    print(response.text)


def create_graph():
    graph_config = {
        "id": "graph1",
        "name": "Walking Graph",
        "unit": "Km",
        "type": "float",
        "color": "sora"
    }

    headers = {"X-USER-TOKEN": PIXELA_TOKEN}

    response = requests.post(
        url=f"{pixela_base_url}v1/users/{pixela_username}/graphs", json=graph_config, headers=headers)
    # response.raise_for_status()
    print(response.text)


def add_pixel(graphID, date, quantity):
    pixel_data = {
        "date": date,
        "quantity": quantity
    }

    headers = {"X-USER-TOKEN": PIXELA_TOKEN}

    response = requests.post(
        url=f"{pixela_base_url}v1/users/{pixela_username}/graphs/{graphID}", json=pixel_data, headers=headers)
    # response.raise_for_status()
    print(response.text)


def update_pixel(graphID, date, quantity):
    pixel_data = {
        "date": date,
        "quantity": quantity
    }

    headers = {"X-USER-TOKEN": PIXELA_TOKEN}

    response = requests.put(
        url=f"{pixela_base_url}v1/users/{pixela_username}/graphs/{graphID}", json=pixel_data, headers=headers)
    # response.raise_for_status()
    print(response.text)


def delete_graph(graphID):
    headers = {"X-USER-TOKEN": PIXELA_TOKEN}

    response = requests.post(
        url=f"{pixela_base_url}v1/users/{pixela_username}/graphs/{graphID}", headers=headers)
    # response.raise_for_status()
    print(response.text)


# create_pixela_account()
# create_graph()
# add_pixel("graph1", "20220121", "0.1")

# now = datetime.datetime.now()
# formatted_now = now.strftime("%Y%m%d")
# print(formatted_now)

# other http methods, update and delete
# requests.put(...)
# requests.delete(...)
