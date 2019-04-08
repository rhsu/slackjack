import random
from utils.color_util import determine_color


class RouletteService():
    def __init__(self):
        pass

    def spin(self):
        number = random.randint(1, 39)  # 38 - 2 is 36
        if number == 37:
            return "0"
        if number == 38:
            return "00"
        return str(number), determine_color(number)
