import requests
import os
import datetime

TODAY = datetime.datetime.now()
TODAY_FORMATTED = TODAY.strftime("%Y%m%d")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.environ.get("PIX_USER")
TOKEN = os.environ.get("PIX_TOKEN")
headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_parameters = {
#     "id": "graph1",
#     "name": "Coding",
#     "unit": "commit",
#     "type": "int",
#     "color": "ajisai",
# }

def create_graph(id, name, unit, type, color):
    graph_parameters = {
        "id": id,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color,
    }
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)

def post_pixel(quantity, date=TODAY_FORMATTED):
    post_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
    post_pixel_parameters = {
        "date": date,
        "quantity": quantity,
    }
    requests.post(url=post_pixel_endpoint, json=post_pixel_parameters, headers=headers)
    
def update_pixel(quantity, date=TODAY_FORMATTED):
    update_pixel_parameters = {
        "quantity": quantity,
    }
    update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{date}"
    requests.put(url=update_pixel_endpoint, json=update_pixel_parameters, headers=headers)

def delete_pixel(date=TODAY_FORMATTED):
    delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{date}"
    requests.delete(url=delete_pixel_endpoint, headers=headers)