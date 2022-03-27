#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import pandas as pd


# data = pd.DataFrame.from_dict(DataManager())
# print(data["iataCode"])
data = pd.read_csv("Flight Deals - prices.csv")
# print(data)
flight_data = FlightData(data)
