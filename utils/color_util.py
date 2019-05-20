import os


def determine_color(number):
    """
    In number ranges from 1 to 10 and 19 to 28, odd numbers are red and even are black.
    In ranges from 11 to 18 and 29 to 36, odd numbers are black and even are red.
    """
    # from pdb import set_trace; set_trace()
    if number >= 1 and number <= 10:
        return "black" if number % 2 == 0 else "red"
    elif number >= 19 and number <= 28:
        return "black" if number % 2 == 0 else "red"
    else:
        return "red" if number % 2 == 0 else "black"
    raise "not sure how it got here"


def determine_icon(color):
    if not is_color(color):
        return color
    display_color = ""
    if color == "red":
        display_color = os.environ.get('RED_ICON', ":red_circle:")
    elif color == "black":
        display_color = os.environ.get('BLACK_ICON', ":black_circle:")
    elif color == "green":
        display_color = os.environ.get('GREEN_ICON', "")
    return display_color


def is_color(color):
    return color in set(["red", "black", "green"])
