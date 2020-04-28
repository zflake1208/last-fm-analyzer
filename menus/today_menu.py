from apiClients import geo_client, chart_client
from apiClients.api_common import get_response
from menus.common import line_break, is_valid

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
    options = ['1: Top Artists', '2: Top Tracks', '3: Top Tags']
    for option in options:
        print(option)
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
    options = ['1: Top Artists', '2: Top Tracks']
    for option in options:
        print(option)
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
    line_break()
    print(f"Today's top artists: ")


def global_top_tracks():
    info = get_response(chart_client.get_top_tracks())
    line_break()
    print(f"Today's top tracks: ")


def global_top_tags():
    info = get_response(chart_client.get_top_tags())
    line_break()
    print(f"Today's top tags: ")


def country_top_artists():
    print("Enter country:")
    country = input()
    info = get_response(geo_client.get_top_artists(country))
    line_break()
    print(f"Top artists in {country}: ")


def country_top_tracks():
    print("Enter country:")
    country = input()
    info = get_response(geo_client.get_top_tracks(country))
    line_break()
    print(f"Top tracks in {country}: ")