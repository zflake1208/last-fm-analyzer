from apiClients import track_client
from apiClients.api_common import get_response

def track_select():
    print("====================================")
    print("How can I help?")
    options = ['1: Description', '2: Similar Songs', '3: Tags', '4: Search']
    for option in options:
        print(option)
    selection = int(input())
    print("Enter track name: ")
    track = input()
    artist = ""
    if selection != 4:
        print("Enter artist name: ")
        artist = input()
    if selection == 1:
        info = get_response(track_client.get_info(track, artist))
        print("====================================")
        print(f"Description for \"{track}\" by {artist}: ")
    elif selection == 2:
        info = get_response(track_client.get_similar(track, artist))
        print("====================================")
        print(f"Tracks similar to \"{track}\" by {artist}: ")
    elif selection == 3:
        info = get_response(track_client.get_top_tags(track, artist))
        print("====================================")
        print(f"Top tags for \"{track}\" by {artist}: ")
    elif selection == 4:
        info = get_response(track_client.search(track))
        print("====================================")
        print(f"Tracks that match \"{artist}\": ")
    else:
        print("Invalid selection.")
        track_select()