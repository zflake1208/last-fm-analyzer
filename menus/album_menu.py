from apiClients import album_client
from apiClients.api_common import get_response

def album_select():
    print("====================================")
    print("How can I help?")
    options = ['1: Description', '2: Tags', '3: Search albums']
    for option in options:
        print(option)
    selection = int(input())
    print("Enter album name: ")
    album = input()
    artist = ""
    if selection != 3:
        print("Enter artist name: ")
        artist = input()
    if selection == 1:
        info = get_response(album_client.get_info(album, artist))
        print("====================================")
        print(f"Description for \"{album}\" by {artist}: ")
        print(info['album']['wiki']['content'])
    elif selection == 2:
        info = get_response(album_client.get_top_tags(album, artist))
        print("====================================")
        print(f"Tags associated with \"{album}\" by {artist}: ")
        for tag in info['toptags']['tag']:
            if not "album" in str(tag['name']) and not "own" in str(tag['name']):
                print(tag['name'])
    elif selection == 3:
        info = get_response(album_client.search(album))
        print("====================================")
        print(f"Albums that match \"{album}\": ")
        i = 0
        for album in info['results']['albummatches']:
            print(f"#{i}: ")
            print("Album: ", album['name'])
            print("Artist: ", album['artist'])
    else:
        print("Invalid selection.")
        album_select()