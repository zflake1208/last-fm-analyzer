from apiClients import tag_client
from apiClients.api_common import get_response
from menus.common import line_break, prompt

def tag_select():
    line_break()
    prompt(['1: Description', '2: Similar Tags', '3: Top Albums', '4: Top Artists', '5: Top Tags', '6: Top Tracks', '7: Weekly Chart List'])
    selection = int(input())
    if selection == 1:
        description()
    elif selection == 2:
        similar_tags()
    elif selection == 3:
        top_albums()
    elif selection == 4:
        top_artists()
    elif selection == 5:
        top_tags()
    elif selection == 6:
        top_tracks()
    elif selection == 7:
        weekly_chart_list()
    else:
        print("Invalid selection.")
        tag_select()


def description():
    print("Enter tag: ")
    tag = input()
    info = get_response(tag_client.get_info(tag))
    line_break()
    print(f"Description for \"{tag}\": ")


def similar_tags():
    print("Enter tag: ")
    tag = input()
    info = get_response(tag_client.get_similar(tag))
    line_break()
    print(f"Tags similar to \"{tag}\": ")


def top_albums():
    print("Enter tag: ")
    tag = input()
    info = get_response(tag_client.get_top_albums(tag))
    line_break()
    print(f"Top albums tagged with \"{tag}\": ")


def top_artists():
    print("Enter tag: ")
    tag = input()
    info = get_response(tag_client.get_top_artists(tag))
    line_break()
    print(f"Top artists tagged with \"{tag}\": ")


def top_tags():
    info = get_response(tag_client.get_top_tags())
    line_break()
    print(f"Top tags on Last.FM: ")


def top_tracks():
    print("Enter tag: ")
    tag = input()
    info = get_response(tag_client.get_top_tracks(tag))
    line_break()
    print(f"Top tracks tagged with \"{tag}\": ")


def weekly_chart_list():
    print("Enter tag: ")
    tag = input()
    info = get_response(tag_client.get_weekly_chart_list(tag))
    line_break()
    print(f"Charts with \"{tag}\": ")
