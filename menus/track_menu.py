from apiClients import track_client
from apiClients.api_common import get_response
from menus.common import line_break, prompt

def track_select():
    line_break()
    prompt(['1: Description', '2: Similar Songs', '3: Tags', '4: Search'])
    selection = int(input())
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
    info = get_response(track_client.get_info(track, artist))
    line_break()
    print(f"Description for \"{track}\" by {artist}: ")


def similar_songs():
    print("Enter track name: ")
    track = input()
    print("Enter artist name: ")
    artist = input()
    info = get_response(track_client.get_similar(track, artist))
    line_break()
    print(f"Tracks similar to \"{track}\" by {artist}: ")


def tags():
    print("Enter track name: ")
    track = input()
    print("Enter artist name: ")
    artist = input()
    info = get_response(track_client.get_top_tags(track, artist))
    line_break()
    print(f"Top tags for \"{track}\" by {artist}: ")


def search():
    print("Enter track name: ")
    track = input()
    print("Enter artist name: ")
    artist = input()
    track = input()
    info = get_response(track_client.search(track))
    line_break()
    print(f"Tracks that match \"{track}\": ")