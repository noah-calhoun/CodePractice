# Takes an input from a user that is an airport identifier, returns airport and weather data.

import json
import requests

# CORS callback method
def getAirport(API_id, airport_id, callback ):
    params = {
        'access_key': API_id,
        'callback':callback
    }

    url = f"http://api.aviationstack.com/v1/airports"
    res = requests.get(url, params)
    return res.text

def my_function(response_data):
    # Your custom callback function
    parsed_data = json.loads(response_data)
    if parsed_data.get('data'):
        firstCity = parsed_data['data'][0]
        city_iata = firstCity['city_iata_code']
        airport = firstCity['airport_name']
        print(f"city IATA: {city_iata}, airport: {airport}")
    else:
        print("no data")

def mainCallback():
    API_key = "389674525272f120bd88b9b0887c5149"
    # airport_id = input("Enter Airport ID: ").strip().upper()
    airport_id = "A"
    airport_data = getAirport(API_key, airport_id, my_function)

    # start_index = airport_data.find('{')
    # end_index = airport_data.rfind('}')
    # json_data = airport_data[start_index:end_index+1]

    # Call your custom callback function with the extracted JSON data
    my_function(airport_data)

    # parsed_data = json.loads(airport_data)
    # if parsed_data.get('data'):
    #     firstCity = parsed_data['data'][0]
    #     city_iata = firstCity['city_iata_code']
    #     airport = firstCity['airport_name']
    #     print(f"city IATA: {city_iata}, airport: {airport}")
    # else:
    #     print("no data")





# CORS proxy method
def get_weather_dataP(city_name):
    jsonp_callback = "jsoncallback"  # The JSONP callback parameter name supported by the API
    jsonp_url = f"http://jsonplaceholder.typicode.com/posts?callback={jsonp_callback}&q={city_name}"
    
    try:
        response = requests.get(jsonp_url)
        # The JSONP response will include the callback function, so we need to extract the JSON data
        data = requests.extract_json(response.text)
        return data
    except requests.JSONParseError as e:
        print(f"Error parsing JSONP response: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def getAirportP(API_id, airport_id, proxy_url ):
    params = {
        'access_key': API_id
    }

    url = f"http://api.aviationstack.com/v1/airports"
    res = requests.get(proxy_url + url, params)
    return res.text

def mainPROXY():
    API_key = "389674525272f120bd88b9b0887c5149"
    proxy_url = "https://cors-anywhere.herokuapp.com/"  # Example CORS proxy URL
    # airport_id = input("Enter Airport ID: ").strip().upper()
    airport_id = "A"
    airport_data = getAirportP(API_key, airport_id, proxy_url)

    parsed_data = json.loads(airport_data)
    if parsed_data.get('data'):
        firstCity = parsed_data['data'][0]
        city_iata = firstCity['city_iata_code']
        airport = firstCity['airport_name']
        print(f"city IATA: {city_iata}, airport: {airport}")
    else:
        print("no data")


if __name__ == '__main__':
    mainCallback()