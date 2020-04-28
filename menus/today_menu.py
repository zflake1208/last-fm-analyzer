from apiClients import geo_client, chart_client
from apiClients.api_common import get_response
from menus.common import line_break, is_valid, prompt

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
    info = get_response(chart_client.get_top_artists())
    if is_valid(info):
        line_break()
        print(f"Today's top artists: ")
        i = 1
        for artist in info['artists']['artist']:
            print(f"#{i}: ")
            print("Artist:", artist['name'])
            print("Playcount:", f"{int(artist['playcount']):,}")
            print("Listeners:", f"{int(artist['listeners']):,}")
            if i != 10:
                print()
            i += 1
    else:
        today_select()


def global_top_tracks():
    info = get_response(chart_client.get_top_tracks())
    if is_valid(info):
        line_break()
        print(f"Today's top tracks: ")
        i = 1
        for track in info['tracks']['artist']:
            print(f"#{i}: ")
            print("Track:", track['name'])
            print("Artist:", track['artist']['name'])
            print("Playcount:", f"{int(track['playcount']):,}")
            print("Listeners:", f"{int(track['listeners']):,}")
            if i != 10:
                print()
            i += 1
    else:
        today_select()


def global_top_tags():
    info = get_response(chart_client.get_top_tags())
    if is_valid(info):
        line_break()
        print(f"Today's top tags: ")
        i = 1
        for tag in info['tags']['tag']:
            print(f"#{i}: ")
            print("Tag:", tag['name'])
            print("Count:", f"{int(tag['taggings']):,}")
            if i != 10:
                print()
            i += 1
    else:
        today_select()


def country_top_artists():
    print("Enter country:")
    country = input()
    country = check_usa(country)
    info = get_response(geo_client.get_top_artists(country))
    if is_valid(info):
        line_break()
        print(f"Top artists in {country}: ")
        i = 1
        for artist in info['topartists']['artist']:
            print(f"#{i}: ")
            print("Artist:", artist['name'])
            print("Listeners:", f"{int(artist['listeners']):,}")
            if i != 10:
                print()
            i += 1
    else:
        country_top_artists()


def country_top_tracks():
    print("Enter country:")
    country = input()
    country = check_usa(country)
    info = get_response(geo_client.get_top_tracks(country))
    if is_valid(info):
        line_break()
        print(f"Top tracks in {country}: ")
        i = 1
        for track in info['tracks']['track']:
            print(f"#{i}: ")
            print("Track:", track['name'])
            print("Artist:", track['artist']['name'])
            print("Listeners:", f"{int(track['listeners']):,}")
            if i != 10:
                print()
            i += 1
    else:
        country_top_tracks()


def check_usa(country):
    america_names = ['USA', 'AMERICA', 'UNITED STATES', 'UNITED STATES OF AMERICA']
    if country.upper() in america_names:
        country = "united states"
    return country
