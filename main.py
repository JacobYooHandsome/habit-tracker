import requests
import datetime
from tkinter import *
import os

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.environ.get("PIX_USER")
TOKEN = os.environ.get("PIX_TOKEN")

pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Coding",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.datetime.now()
today_formatted = today.strftime("%Y%m%d")

post_pixel_parameters = {
    "date": today_formatted,
    "quantity": "1",
}

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_parameters, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today_formatted}"

update_pixel_parameters = {
    "quantity": "2"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_parameters, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today_formatted}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)

window = Tk()
window.title("Habit Tracker")

