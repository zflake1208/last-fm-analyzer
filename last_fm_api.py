from apiClients import album_client, artist_client, chart_client, geo_client, tag_client, track_client, album_client
import requests
import json

"""
Instantiate the client classes so that they are all available at once with a single call to 'import last_fm_api'.
"""
album_client = album_client.AlbumClient()
artist_client = artist_client.ArtistClient()
chart_client = chart_client.ChartClient()
geo_client = geo_client.GeoClient()
tag_client = tag_client.TagClient()
track_client = track_client.TrackClient()

def get_response(query):
    """
    Make the HTML POST request to Last.FM and convert to JSON format.
    album_client.get_api_key() is used since all clients share the same API key anyway.
    """
    response = requests.post("http://ws.audioscrobbler.com/2.0/?" + query + "&api_key=" + album_client.get_api_key() + "&format=json")
    return json.loads(response.text)