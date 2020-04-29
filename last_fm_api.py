from apiClients import album_client, artist_client, chart_client, geo_client, tag_client, track_client, album_client
import requests
import json

album_client = album_client.AlbumClient()
artist_client = artist_client.ArtistClient()
chart_client = chart_client.ChartClient()
geo_client = geo_client.GeoClient()
tag_client = tag_client.TagClient()
track_client = track_client.TrackClient()

def get_response(query):
    response = requests.post("http://ws.audioscrobbler.com/2.0/?" + query + "&api_key=" + album_client.get_api_key() + "&format=json")
    return json.loads(response.text)