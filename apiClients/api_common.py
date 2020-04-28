import requests
import json

def get_api_key():
    return "4c6b4b4bdb3d061befb1ca04a70cf82e"

def get_response(query):
    response = requests.post("http://ws.audioscrobbler.com/2.0/?" + query + "&api_key=" + get_api_key() + "&format=json")
    return json.loads(response.text)
