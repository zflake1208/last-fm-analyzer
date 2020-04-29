"""
Common methods for the menus.
"""

def line_break():
    print("====================================")

def prompt(options):
    print("How can I help?")
    for option in options:
        print(option)

def is_valid(response):
    if response.get("error"):
        print(response['message'])
        return False
    else:
        return True