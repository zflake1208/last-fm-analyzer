from apiClients import artist_client
from apiClients.api_common import get_response
from menus.common import line_break, prompt, is_valid

def artist_select():
    line_break()
    prompt(['1: Description', '2: Albums', '3: Tracks', '4: Tags', '5: Similar Artists', '6: Search'])
    selection = int(input())
    line_break()
    if selection == 1:
        description()
    elif selection == 2:
        albums()
    elif selection == 3:
        tracks()
    elif selection == 4:
        tags()
    elif selection == 5:
        similar_artists()
    elif selection == 6:
        search()
    else:
        print("Invalid selection.")
        artist_select()


def description():
    print("Enter artist name: ")
    artist = input()
    info = get_response(artist_client.get_info(artist))
    if is_valid(info):
        line_break()
        print(f"Description for {artist}: ")
        print(info['artist']['bio']['content'])
    else:
        description()

def albums():
    print("Enter artist name: ")
    artist = input()
    info = get_response(artist_client.get_top_albums(artist))
    if is_valid(info):
        line_break()
        print(f"Albums by {artist}: ")
        i = 1
        for album in info['topalbums']['album']:
            print(f"#{i}: ")
            print("Album Name:", album['name'])
            print(f"Playcount: {int(album['playcount']):,}")
            if i != 10:
                print()
                i += 1
    else:
        albums()


def tracks():
    print("Enter artist name: ")
    artist = input()
    info = get_response(artist_client.get_top_tracks(artist))
    if is_valid(info):
        line_break()
        print(f"Top tracks for {artist}: ")
        i = 1
        for track in info['toptracks']['track']:
            print(f"#{i}: ")
            print("Track Name:", track['name'])
            print(f"Playcount: {int(track['playcount']):,}")
            if i != 10:
                print()
                i += 1
    else:
        tracks()


def tags():
    print("Enter artist name: ")
    artist = input()
    info = get_response(artist_client.get_top_tags(artist))
    if is_valid(info):
        line_break()
        print(f"Top tags for {artist}: ")
        i = 1
        for tag in info['toptags']['tag']:
            print(f"#{i}: ")
            print("Tag Name:", tag['name'])
            print(f"Count: {int(tag['count']):,}")
            if i != 10:
                print()
                i += 1
    else:
        tags()


def similar_artists():
    print("Enter artist name: ")
    artist = input()
    info = get_response(artist_client.get_similar(artist))
    if is_valid(info):
        line_break()
        print(f"Artists similar to {artist}: ")
        i = 1
        for artist in info['similarartists']['artist']:
            print(f"#{i}: ")
            print("Artist:", artist['name'])
            print(f"Match: {float(artist['match']):.0%}")
            if i != 10:
                print()
                i += 1
    else:
        similar_artists()


def search():
    print("Enter artist name: ")
    artist = input()
    info = get_response(artist_client.search(artist))
    if is_valid(info):
        line_break()
        print(f"Artists that match \"{artist}\": ")
        i = 1
        for artist in info['results']['artistmatches']['artist']:
            print(f"#{i}: ")
            print("Artist:", artist['name'])
            print(f"Listeners: {int(artist['listeners']):,}")
            if i != 10:
                print()
                i += 1
    else:
        search()
