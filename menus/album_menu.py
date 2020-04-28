from apiClients import album_client
from apiClients.api_common import get_response
from menus.common_menu import line_break, prompt, is_valid

def album_select():
    line_break()
    prompt(['1: Description', '2: Tags', '3: Search albums'])
    selection = int(input())
    line_break()
    if selection == 1:
       description()
    elif selection == 2:
        tags()
    elif selection == 3:
        search()
    else:
        print("Invalid selection.")
        album_select()


def description():
    print("Enter album name: ")
    album = input()
    print("Enter artist name: ")
    artist = input()
    info = get_response(album_client.get_info(album, artist))
    if is_valid(info):
        line_break()
        print(f"Description for \"{album}\" by {artist}: ")
        print(info['album']['wiki']['content'])
    else:
        description()


def tags():
    print("Enter album name: ")
    album = input()
    print("Enter artist name: ")
    artist = input()
    info = get_response(album_client.get_top_tags(album, artist))
    if is_valid(info):
        line_break()
        print(f"Tags associated with \"{album}\" by {artist}: ")
        for tag in info['toptags']['tag']:
            if not "album" in str(tag['name']) and not "own" in str(tag['name']):
                print(tag['name'])
    else:
        tags()


def search():
    print("Enter album name: ")
    album = input()
    info = get_response(album_client.search(album))
    if is_valid(info):
        line_break()
        print(f"Albums that match \"{album}\": ")
        i = 1
        for album in info['results']['albummatches']:
            print(f"#{i}")
            print("Album: ", album['name'])
            print("Artist: ", album['artist'])
            if i != 10:
                print()
                i += 1
    else:
        search()