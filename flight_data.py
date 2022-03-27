from flight_search import flight_search
import pandas as pd
from notification_manager import send_mail
import datetime
from datetime import date

from_date = date.today()
to_date = from_date + datetime.timedelta(days=180)
airport = "LHR"


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, flight_data: pd.DataFrame):
        self.flight_data = flight_data
        self.search_flights()

    def search_flights(self):
        for index, row in self.flight_data.iterrows():
            # print(row["iataCode"])
            flight_details = flight_search(airport, row["iataCode"], from_date, to_date)
            price = flight_details["data"][0]["price"]
            if price <= row["lowestPrice"]:
                message = f"You can go to {row['city']} for {price}"
                send_mail(message)
                break
            # break
            # print(flight_details)
