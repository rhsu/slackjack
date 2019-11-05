from services.service import Service

RED_SNAKE_NUMBERS = ["1", "5", "9", "12", "14", "16", "19", "23", "27", "30", "32", "34"]

class RedSnakeService(Service):

    def __init__(self, userdata, roulette_service):
        Service.__init__(self, userdata)
        self.roulette_service = roulette_service

    def play(self):
        if self.money() < 12:
            return "Cant play red snake. Not enough money."

        self.set_bet(12)

        number, color = self.roulette_service.spin()
        # from pdb import set_trace; set_trace()
        if color != "red":
            bet_amount = self._userdata.bet
            self.decrease_money(bet_amount)
            return f"Roulette wheel rolled: {color} {number}. You lost."
        elif number in RED_SNAKE_NUMBERS:
            bet_amount = self._userdata.bet
            self.increase_money(bet_amount * 35)
            return f"Roulette wheel rolled: {color} {number}. You won."
        else:
            bet_amount = self._userdata.bet
            self.decrease_money(bet_amount)
            return f"Roulette wheel rolled: {color} {number}. You lost."
