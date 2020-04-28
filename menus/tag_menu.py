from apiClients import tag_client
from apiClients.api_common import get_response
from menus.common import line_break, prompt, is_valid

def tag_select():
    line_break()
    prompt(['1: Description', '2: Top Albums', '3: Top Artists', '4: Top Tags', '5: Top Tracks'])
    selection = int(input())
    line_break()
    if selection == 1:
        description()
    elif selection == 2:
        top_albums()
    elif selection == 3:
        top_artists()
    elif selection == 4:
        top_tags()
    elif selection == 5:
        top_tracks()
    else:
        print("Invalid selection.")
        tag_select()


def description():
    print("Enter tag: ")
    tag = input()
    info = get_response(tag_client.get_info(tag))
    if is_valid(info):
        line_break()
        print(f"Description for \"{tag}\": ")
        print(info['tag']['wiki']['content'])
    else:
        description()


def top_albums():
    print("Enter tag: ")
    tag = input()
    info = get_response(tag_client.get_top_albums(tag))
    if is_valid(info):
        line_break()
        print(f"Top albums tagged with \"{tag}\": ")
        i = 1
        for album in info['albums']['album']:
            print(f"#{i}:", f"\"{album['name']}\" by", album['artist']['name'])
            i += 1
    else:
        top_albums()


def top_artists():
    print("Enter tag: ")
    tag = input()
    info = get_response(tag_client.get_top_artists(tag))
    if is_valid(info):
        line_break()
        print(f"Top artists tagged with \"{tag}\": ")
        i = 1
        for artist in info['topartists']['artist']:
            print(f"#{i}:", artist['name'])
            i += 1
    else:
        top_artists()


def top_tags():
    info = get_response(tag_client.get_top_tags())
    if is_valid(info):
        line_break()
        print(f"Top tags on Last.FM: ")
        i = 1
        for tag in info['toptags']['tag']:
            print(f"#{i}: ")
            print("Tag:", tag['name'])
            print("Count:", f"{int(tag['count']):,}")
            if i != 10:
                print()
            i += 1
    else:
        tag_select()


def top_tracks():
    print("Enter tag: ")
    tag = input()
    info = get_response(tag_client.get_top_tracks(tag))
    if is_valid(info):
        line_break()
        print(f"Top tracks tagged with \"{tag}\": ")
        i = 1
        for track in info['tracks']['track']:
            print(f"#{i}:", f"\"{track['name']}\" by", track['artist']['name'])
            i += 1
    else:
        top_tracks()
