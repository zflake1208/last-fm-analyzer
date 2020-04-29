import last_fm_api as api
from menus.common import line_break, is_valid, prompt
from graph import create_graph

def today_select():
    line_break()
    print("Global stats or just one country?")
    options = ['1: Global', '2: Country']
    for option in options:
        print(option)
    selection = int(input())
    if selection == 1:
        global_select()
    elif selection == 2:
        country_select()
    else:
        print("Invalid selection.")
        today_select()


def global_select():
    line_break()
    prompt(['1: Top Artists', '2: Top Tracks', '3: Top Tags'])
    selection = int(input())
    if selection == 1:
        global_top_artists()
    elif selection == 2:
        global_top_tracks()
    elif selection == 3:
        global_top_tags()
    else:
        print("Invalid selection.")
        global_select()


def country_select():
    line_break()
    prompt(['1: Top Artists', '2: Top Tracks'])
    selection = int(input())
    if selection == 1:
        country_top_artists()
    elif selection == 2:
        country_top_tracks()
    else:
        print("Invalid selection.")
        country_select()


def global_top_artists():
    info = api.get_response(api.chart_client.get_top_artists())
    if is_valid(info):
        line_break()
        print(f"Today's top artists: ")
        i = 1
        artists = []
        playcounts = []
        for artist in info['artists']['artist']:
            print(f"#{i}: ")
            print("Artist:", artist['name'])
            print("Playcount:", f"{int(artist['playcount']):,}")
            print("Listeners:", f"{int(artist['listeners']):,}")
            artists.append(artist['name'])
            playcounts.append(int(artist['playcount']))
            if i != 10:
                print()
            i += 1
        create_graph("Artist", "Playcount", artists, playcounts)
    else:
        today_select()


def global_top_tracks():
    info = api.get_response(api.chart_client.get_top_tracks())
    if is_valid(info):
        line_break()
        print(f"Today's top tracks: ")
        i = 1
        tracks = []
        playcounts = []
        for track in info['tracks']['artist']:
            print(f"#{i}: ")
            print("Track:", track['name'])
            print("Artist:", track['artist']['name'])
            print("Playcount:", f"{int(track['playcount']):,}")
            print("Listeners:", f"{int(track['listeners']):,}")
            tracks.append(f"{track['name']}\n({track['artist']['name']})")
            playcounts.append(int(track['playcount']))
            if i != 10:
                print()
            i += 1
        create_graph("Track", "Playcount", tracks, playcounts)
    else:
        today_select()


def global_top_tags():
    info = api.get_response(api.chart_client.get_top_tags())
    if is_valid(info):
        line_break()
        print(f"Today's top tags: ")
        i = 1
        tags = []
        counts = []
        for tag in info['tags']['tag']:
            print(f"#{i}: ")
            print("Tag:", tag['name'])
            print("Count:", f"{int(tag['taggings']):,}")
            tags.append(tag['name'])
            counts.append(int(tag['taggings']))
            if i != 10:
                print()
            i += 1
        create_graph("Tag", "Count", tags, counts)
    else:
        today_select()


def country_top_artists():
    print("Enter country:")
    country = input()
    country = check_usa(country)
    info = api.get_response(api.geo_client.get_top_artists(country))
    if is_valid(info):
        line_break()
        print(f"Top artists in {country}: ")
        i = 1
        artists = []
        listeners = []
        for artist in info['topartists']['artist']:
            print(f"#{i}: ")
            print("Artist:", artist['name'])
            print("Listeners:", f"{int(artist['listeners']):,}")
            artists.append(artist['name'])
            listeners.append(int(artist['listeners']))
            if i != 10:
                print()
            i += 1
        create_graph("Artist", "Listeners", artists, listeners)
    else:
        country_top_artists()


def country_top_tracks():
    print("Enter country:")
    country = input()
    country = check_usa(country)
    info = api.get_response(api.geo_client.get_top_tracks(country))
    if is_valid(info):
        line_break()
        print(f"Top tracks in {country}: ")
        i = 1
        tracks = []
        listeners = []
        for track in info['tracks']['track']:
            print(f"#{i}: ")
            print("Track:", track['name'])
            print("Artist:", track['artist']['name'])
            print("Listeners:", f"{int(track['listeners']):,}")
            tracks.append(f"{track['name']}\n({track['artist']['name']})")
            listeners.append(int(track['listeners']))
            if i != 10:
                print()
            i += 1
        create_graph("Track", "Listeners", tracks, listeners)
    else:
        country_top_tracks()


def check_usa(country):
    america_names = ['USA', 'AMERICA', 'UNITED STATES', 'UNITED STATES OF AMERICA']
    if country.upper() in america_names:
        country = "united states"
    return country
