import requests
from api import *

def DataManager():
    # This class is responsible for talking to the Google Sheet.
    with requests.get(url= flight_data_sheet_url) as response:
        data = response.json()
        # data.to_csv("Flight Deals - prices.csv")
        return data["prices"]


