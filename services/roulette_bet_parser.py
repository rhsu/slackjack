class RouletteBetParser:
    def __init__(self, user_data, user_input):
        # TODO
        # user types in "bet on 31 black for 21"
        # user_input = thing.split(" ", 2)[2]
        self.user_data = user_data
        self.user_input = user_input

    def process(self):
        guess, bet = self.user_input.split("for")
        number, color = guess.split(" ")
        self.user_data["bet"] = bet
