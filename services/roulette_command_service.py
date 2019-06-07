from global_store import ROULETE_QUEUE
from utils.color_util import ICONS


class RouletteCommandService:
    # TODO put user_id on user_data
    def __init__(self, command, user_id, user_data):
        self.command = command
        self.user_id = user_id
        self.user_data = user_data

    def is_valid(self):
        tokens = self.command.split(" ")

        # look at all the tokens
        if len(tokens) != 4:
            return False, "Invalid *put* command"

        # look at token 1
        bet_amount = tokens[1]

        try:
            bet_amount = int(tokens[1])
        except ValueError:
            return False, "Invalid bet amount"

        if bet_amount <= 0:
            return False, "Invalid bet amount"

        if bet_amount > self.user_data.money:
            return False, "Invalid bet amount: not enough money"

        # look at token 2
        if tokens[2].lower() != "on":
            return False, "Invalid *put* command: missing *on* keyword"

        # look at token 3
        valid_color_bets = set([
            "red", "black", "green", ICONS["red"], ICONS["black"], ICONS["green"]])
        if tokens[3].lower() in valid_color_bets:
            ROULETE_QUEUE.add(self.user_id)
            if tokens[3] == ICONS["red"]:
                self.user_data.roulette_bet.append(("red", bet_amount))
            elif tokens[3] == ICONS["black"]:
                self.user_data.roulette_bet.append(("black", bet_amount))
            elif tokens[3] == ICONS["green"]:
                self.user_data.roulette_bet.append(("green", bet_amount))
            else:
                self.user_data.roulette_bet.append((tokens[3], bet_amount))
            return True, "success"

        bet_number = tokens[3]
        try:
            bet_number = int(tokens[3])
        except ValueError:
            return False, "Invalid bet type: Cant bet on %s" % bet_number

        if bet_number <= 0 or bet_number > 28:
            return False, "Invalid bet number"

        ROULETE_QUEUE.add(self.user_id)
        self.user_data.roulette_bet.append((bet_number, bet_amount))
        return True, "success"
