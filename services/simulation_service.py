import random

class SimulationService:
    def __init__(self, roulette_service):
        self._roulette_service = roulette_service

    def simulate(self):
        colors = {
            "red": 0,
            "black": 0,
            "green": 0
        }

        numbers = {}

        for times in range(100000):
            number, color = self._roulette_service.spin()
            colors[color] += 1
            if number in numbers:
                numbers[number] += 1
            else:
                numbers[number] = 0

        red_times = colors["red"] / 1000
        black_times = colors["black"] / 1000
        green_times = colors["green"] / 1000

        color_result = f"out of 100000 spins... \n" \
                       f"red appeared {red_times}% times \n" \
                       f"black appeared {black_times}% times \n" \
                       f"green appeared {green_times}% times"

        return color_result

    def flip(self):
        results = {
            "heads": 0,
            "tails": 0
        }
        for times in range(100000):
            num = random.randint(0, 1)
            if num == 0:
                results["heads"] += 1
            elif num == 1:
                results["tails"] += 1

        head_times = results["heads"] / 1000
        tail_times = results["tails"] / 1000
        coin_result = f"out of 100000 flips... \n" \
                      f"heads appeared {head_times}% times \n" \
                      f"tails appeared {tail_times}% times \n"
        return coin_result
