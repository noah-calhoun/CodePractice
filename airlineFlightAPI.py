# Takes an input from a user that is an airport identifier, returns airport and weather data.

import requests

def getAirport(API_id, airport_id ):
    params = {
        'access_key': API_id,
        'search': airport_id
    }

    url = "https://api.aviationstack.com/v1/airports"
    res = requests.get("http://api.aviationstack.com/v1/airports", params)
    return res.json()

def main():
    API_key = "389674525272f120bd88b9b0887c5149"

    airport_id = input("Enter Airport ID: ").strip().upper()
    airport_data = getAirport(API_key, airport_id)

    if airport_data:
        print(airport_data)
    
    else:
        print("no data")


if __name__ == '__main__':
    main()