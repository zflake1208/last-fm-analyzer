import last_fm_api as api
from menus.common import line_break, prompt, is_valid
from graph import create_graph

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
    info = api.get_response(api.artist_client.get_info(artist))
    if is_valid(info):
        line_break()
        print(f"Description for {artist}: ")
        print(info['artist']['bio']['content'])
    else:
        description()

def albums():
    print("Enter artist name: ")
    artist = input()
    info = api.get_response(api.artist_client.get_top_albums(artist))
    if is_valid(info):
        line_break()
        print(f"Albums by {artist}: ")
        i = 1
        albums = []
        playcounts = []
        for album in info['topalbums']['album']:
            print(f"#{i}:")
            print("Album Name:", album['name'])
            print(f"Playcount: {int(album['playcount']):,}")
            albums.append(album['name'])
            playcounts.append(int(album['playcount']))
            if i != 10:
                print()
                i += 1
        create_graph("Albums", "Playcount", albums, playcounts)
    else:
        albums()


def tracks():
    print("Enter artist name: ")
    artist = input()
    info = api.get_response(api.artist_client.get_top_tracks(artist))
    if is_valid(info):
        line_break()
        print(f"Top tracks for {artist}: ")
        i = 1
        tracks = []
        playcounts = []
        for track in info['toptracks']['track']:
            print(f"#{i}:")
            print("Track Name:", track['name'])
            print(f"Playcount: {int(track['playcount']):,}")
            tracks.append(track['name'])
            playcounts.append(int(track['playcount']))
            if i != 10:
                print()
                i += 1
        create_graph("Tracks", "Playcount", tracks, playcounts)
    else:
        tracks()


def tags():
    print("Enter artist name: ")
    artist = input()
    info = api.get_response(api.artist_client.get_top_tags(artist))
    if is_valid(info):
        line_break()
        print(f"Top tags for {artist}: ")
        i = 1
        tags = []
        counts = []
        for tag in info['toptags']['tag']:
            print(f"#{i}:")
            print("Tag Name:", tag['name'])
            print(f"Count: {int(tag['count']):,}")
            tags.append(tag['name'])
            counts.append(int(tag['count']))
            if i != 10:
                print()
                i += 1
        create_graph("Tags", "Count", tags, counts)
    else:
        tags()


def similar_artists():
    print("Enter artist name: ")
    artist = input()
    info = api.get_response(api.artist_client.get_similar(artist))
    if is_valid(info):
        line_break()
        print(f"Artists similar to {artist}: ")
        i = 1
        artists = []
        matches  = []
        for artist in info['similarartists']['artist']:
            print(f"#{i}:")
            print("Artist:", artist['name'])
            print(f"Match: {float(artist['match']):.0%}")
            artists.append(artist['name'])
            matches.append(float(artist['match']) * 100)
            if i != 10:
                print()
                i += 1
        create_graph("Artist", "% Match", artists, matches)
    else:
        similar_artists()


def search():
    print("Enter artist name: ")
    artist = input()
    info = api.get_response(api.artist_client.search(artist))
    if is_valid(info):
        line_break()
        print(f"Artists that match \"{artist}\": ")
        i = 1
        artists = []
        listeners  = []
        for artist in info['results']['artistmatches']['artist']:
            print(f"#{i}: ")
            print("Artist:", artist['name'])
            print(f"Listeners: {int(artist['listeners']):,}")
            artists.append(artist['name'])
            listeners.append(int(artist['listeners']))
            if i != 10:
                print()
                i += 1
        create_graph("Artist", "Listeners", artists, listeners)
    else:
        search()
