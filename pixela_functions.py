import requests
import os
import datetime
import webbrowser
from dotenv import load_dotenv
from tkinter import messagebox
load_dotenv()

TODAY = datetime.datetime.now()
TODAY_FORMATTED = TODAY.strftime("%Y%m%d")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIX_USER")
TOKEN = os.getenv("PIX_TOKEN")
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
    response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
    messagebox.showinfo(title="Result", message=response.text)
    

def post_pixel(quantity, date):
    post_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
    post_pixel_parameters = {
        "date": date,
        "quantity": quantity,
    }
    response = requests.post(url=post_pixel_endpoint, json=post_pixel_parameters, headers=headers)
    messagebox.showinfo(title="Result", message=response.text)
    
def update_pixel(quantity, date):
    update_pixel_parameters = {
        "quantity": quantity,
    }
    update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{date}"
    response = requests.put(url=update_pixel_endpoint, json=update_pixel_parameters, headers=headers)
    messagebox.showinfo(title="Result", message=response.text)

def delete_pixel(date):
    delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{date}"
    response = requests.delete(url=delete_pixel_endpoint, headers=headers)
    messagebox.showinfo(title="Result", message=response.text)

def open_link():
    url = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1.html"
    webbrowser.open(url)