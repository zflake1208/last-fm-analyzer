from apiClients import tag_client
from apiClients.api_common import get_response

def tag_select():
    print("====================================")
    print("How can I help?")
    options = ['1: Description', '2: Similar Tags', '3: Top Albums', '4: Top Artists', '5: Top Tags', '6: Top Tracks', '7: Weekly Chart List']
    for option in options:
        print(option)
    selection = int(input())
    tag = ""
    if selection != 5:
        print("Enter tag: ")
        tag = input()
    if selection == 1:
        info = get_response(tag_client.get_info(tag))
        print("====================================")
        print(f"Description for \"{tag}\": ")
    elif selection == 2:
        info = get_response(tag_client.get_similar(tag))
        print("====================================")
        print(f"Tags similar to \"{tag}\": ")
    elif selection == 3:
        info = get_response(tag_client.get_top_albums(tag))
        print("====================================")
        print(f"Top albums tagged with \"{tag}\": ")
    elif selection == 4:
        info = get_response(tag_client.get_top_artists(tag))
        print("====================================")
        print(f"Top artists tagged with \"{tag}\": ")
    elif selection == 5:
        info = get_response(tag_client.get_top_tags())
        print("====================================")
        print(f"Top tags on Last.FM: ")
    elif selection == 6:
        info = get_response(tag_client.get_top_tracks(tag))
        print("====================================")
        print(f"Top tracks tagged with \"{tag}\": ")
    elif selection == 7:
        info = get_response(tag_client.get_weekly_chart_list(tag))
        print("====================================")
        print(f"Charts with \"{tag}\": ")
    else:
        print("Invalid selection.")
        tag_select()