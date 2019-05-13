import random
from utils.color_util import determine_color


class RouletteService():
    def __init__(self):
        pass

    def spin(self):
        # 1 to 36 are roulette numbers
        # 37 is 0
        # 38 is 00
        number = random.randint(1, 38)
        if number == 37:
            return "0", "green"
        if number == 38:
            return "00", "green"
        return str(number), determine_color(number)
