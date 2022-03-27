import requests
from  api import *

def flight_search(origin, destination, from_date, to_date):
    api_endpoint = "https://tequila-api.kiwi.com/v2/search"
    flight_params ={
        "fly_from": origin,
        "fly_to": destination,
        "date_from": from_date,
        "date_to": to_date,
    }
    headers = {
        "apikey": flight_search_api_key
    }
    response = requests.get(url=api_endpoint, params=flight_params, headers=headers)
    status = response.status_code
    return response.json()


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    #It will return a list of flights that match the search criteria.

    pass
