from apiClients import artist_client
from apiClients.api_common import get_response

def artist_select():
    print("====================================")
    print("How can I help?")
    options = ['1: Description', '2: Albums', '3: Tracks', '4: Tags', '5: Similar Artists', '6: Search']
    for option in options:
        print(option)
    selection = int(input())
    print("Enter artist name: ")
    artist = input()
    if selection == 1:
        info = get_response(artist_client.get_info(artist))
        print("====================================")
        print(f"Description for {artist}: ")
    elif selection == 2:
        info = get_response(artist_client.get_top_albums(artist))
        print("====================================")
        print(f"Albums by {artist}: ")
    elif selection == 3:
        info = get_response(artist_client.get_top_tracks(artist))
        print("====================================")
        print(f"Top tracks for {artist}: ")
    elif selection == 4:
        info = get_response(artist_client.get_top_tags(artist))
        print("====================================")
        print(f"Top tags for {artist}: ")
    elif selection == 5:
        info = get_response(artist_client.get_similar(artist))
        print("====================================")
        print(f"Artists similar to {artist}: ")
    elif selection == 6:
        info = get_response(artist_client.search)
        print("====================================")
        print(f"Artists that match \"{artist}\": ")
    else:
        print("Invalid selection.")
        artist_select()