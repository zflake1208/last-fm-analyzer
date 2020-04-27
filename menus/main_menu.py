from menus.album_menu import album_select
from menus.artist_menu import artist_select
from menus.today_menu import today_select
from menus.tag_menu import tag_select
from menus.track_menu import track_select

def top_level():
    print("Select option: ")
    options = ['1: Album', '2: Artist', '3: Today\'s Hits', '4: Tag', '5: Track']
    for option in options:
        print(option)
    selection = int(input())
    if selection == 1:
        album_select()
    elif selection == 2:
        artist_select()
    elif selection == 3:
        today_select()
    elif selection == 4: 
        tag_select()
    elif selection == 5:
        track_select()
    else:
        print("Invalid selection.")
        top_level()
    last_step()

def last_step():
    print("====================================")
    print("Anything else? (Y/N)")
    selection = input()
    if selection.capitalize == "Y" or selection.capitalize == "YES":
        top_level()
    else:
        print("Goodbye.")
