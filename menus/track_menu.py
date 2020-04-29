import last_fm_api as api
from menus.common import line_break, prompt, is_valid
from graph import create_graph

def track_select():
    line_break()
    prompt(['1: Description', '2: Similar Songs', '3: Tags', '4: Search'])
    selection = int(input())
    line_break()
    if selection == 1:
        description()  
    elif selection == 2:
        similar_songs()
    elif selection == 3:
        tags()
    elif selection == 4:
        search()
    else:
        print("Invalid selection.")
        track_select()


def description():
    print("Enter track name: ")
    track = input()
    print("Enter artist name: ")
    artist = input()
    info = api.get_response(api.track_client.get_info(track, artist))
    if is_valid(info):
        line_break()
        print(f"Description for \"{track}\" by {artist}: ")
        print(info['track']['wiki']['content'])
        print("Playcount:", f"{int(info['track']['playcount']):,}")
        print("Listeners:", f"{int(info['track']['listeners']):,}")
    else:
        description()


def similar_songs():
    print("Enter track name: ")
    track = input()
    print("Enter artist name: ")
    artist = input()
    info = api.get_response(api.track_client.get_similar(track, artist))
    if is_valid(info):
        line_break()
        print(f"Tracks similar to \"{track}\" by {artist}: ")
        i = 1
        tracks = []
        matches = []
        for track in info['similartracks']['track']:
            print(f"#{i}: ")
            print("Track:", track['name'])
            print("Artist:", track['artist']['name'])
            print("Playcount:", f"{int(track['playcount']):,}")
            print("Match:", f"{float(track['match']):.0%}")
            tracks.append(f"{track['name']}\n({track['artist']['name']})")
            matches.append(float(track['match']) * 100)
            if i != 10:
                print()
            i += 1
        create_graph("Track", "Match %", tracks, matches)
    else:
        similar_songs()


def tags():
    print("Enter track name: ")
    track = input()
    print("Enter artist name: ")
    artist = input()
    info = api.get_response(api.track_client.get_top_tags(track, artist))
    if is_valid(info):
        line_break()
        print(f"Top tags for \"{track}\" by {artist}: ")
        i = 1
        tags = []
        counts = []
        for tag in info['tags']['tag']:
            print(f"#{i}: ")
            print("Tag:", tag['name'])
            print("Count:", tag['count'])
            tags.append(tag['name'])
            counts.append(int(tag['count']))
            if i != 10:
                print()
            i += 1
        create_graph("Tags", "Count", tags, counts)
    else:
        tags()


def search():
    print("Enter track name: ")
    track = input()
    info = api.get_response(api.track_client.search(track))
    if is_valid(info):
        line_break()
        print(f"Tracks that match \"{track}\": ")
        i = 1
        tracks = []
        listeners = []
        for track in info['results']['trackmatches']['track']:
            print(f"#{i}: ")
            print("Track:", track['name'])
            print("Artist:", track['artist'])
            print("Listeners:", f"{int(track['listeners']):,}")
            tracks.append(f"{track['name']}\n({track['artist']['name']})")
            listeners.append(int(track['listeners']))
            if i != 10:
                print()
            i += 1
        create_graph("Track", "Listeners", tracks, listeners)
    else:
        search()
