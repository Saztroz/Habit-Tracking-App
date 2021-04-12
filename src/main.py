import requests
from datetime import datetime


USERNAME = "your username"
TOKEN = "asdgads124sasdg"

pixela_endpoint = "https://pixe.la/v1/users" 

user_params = {
    "token": "asdgads124sasdg",
    "username": "your username",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycle Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? ")
}


response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)



