from apiClients import geo_client, chart_client
from apiClients.api_common import get_response

def today_select():
    print("====================================")
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
        info = get_response(chart_client.get_top_artists())
        print("====================================")
        print(f"Today's top artists: ")
    elif selection == 2:
        info = get_response(chart_client.get_top_tracks())
        print("====================================")
        print(f"Today's top tracks: ")
    elif selection == 3:
        info = get_response(chart_client.get_top_tags())
        print("====================================")
        print(f"Today's top tags: ")
    else:
        print("Invalid selection.")
        global_select()

def country_select():
    options = ['1: Top Artists', '2: Top Tracks']
    for option in options:
        print(option)
    selection = int(input())
    print("Enter country:")
    country = input()
    if selection == 1:
        info = get_response(geo_client.get_top_artists(country))
        print("====================================")
        print(f"Top artists in {country}: ")
    elif selection == 2:
        info = get_response(geo_client.get_top_tracks(country))
        print("====================================")
        print(f"Top tracks in {country}: ")
    else:
        print("Invalid selection.")
        country_select()