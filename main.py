import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "test",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime(day=7, year=2021, month=12)

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "11.0",
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)


