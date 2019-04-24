def determine_color(number):
    """
    In number ranges from 1 to 10 and 19 to 28, odd numbers are red and even are black.
    In ranges from 11 to 18 and 29 to 36, odd numbers are black and even are red.
    """
    if number >= 1 and number <= 10:
        return "black" if number % 2 == 0 else "red"
    elif number <= 19 and number <= 28:
        return "black" if number % 2 == 0 else "red"
    else:
        return "red" if number % 2 == 0 else "black"
