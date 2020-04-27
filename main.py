from apiClients import album, api_common
import requests
import json

print("Enter album: ")
alb = input()
print("Enter artist: ")
artist = input()

query = "http://ws.audioscrobbler.com/2.0/?"
query += album.get_info(artist, alb)
query += "&api_key=" + api_common.get_api_key()
query += "&format=json"

response = requests.post(query)
info = json.loads(response.text)

print(info['album']['name'])