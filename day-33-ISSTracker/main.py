import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

iss_position_dict = response.json()['iss_position']
iss_position = (iss_position_dict['latitude'], iss_position_dict['longitude'])
print(iss_position)
