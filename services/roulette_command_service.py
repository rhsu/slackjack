from global_store import ROULETE_QUEUE
from utils.color_util import ICONS


class RouletteCommandService:
    # TODO put user_id on user_data
    def __init__(self, command, user_id, user_data):
        self.tokens = command.split(" ")
        self.user_id = user_id
        self.user_data = user_data
        self.bet_amount = None
        self.bet_number = None

    def is_valid(self):
        # look for all the tokens
        if len(self.tokens) != 4:
            return False, "Invalid *put* command"

        success_1, error_1 = self.__validation_token_1()
        if not success_1:
            return False, error_1

        success_2, error_2 = self.__validation_token_2()
        if not success_2:
            return False, error_2

        success_3, error_3 = self.__validation_token_3()
        if not success_3:
            return False, error_3

        ROULETE_QUEUE.add(self.user_id)
        self.user_data.roulette_bet.append((self.bet_number, self.bet_amount))
        return True, "success"

    def __validation_token_1(self):
        try:
            self.bet_amount = int(self.tokens[1])
        except ValueError:
            return False, "Invalid bet amount"

        if self.bet_amount <= 0:
            return False, "Invalid bet amount"

        if self.bet_amount > self.user_data.money:
            return False, "Invalid bet amount: not enough money"
        return True, None

    def __validation_token_2(self):
        if self.tokens[2].lower() != "on":
            return False, "Invalid *put* command: missing *on* keyword"
        return True, None

    # TODO break this into smaller functions
    def __validation_token_3(self):
        valid_color_bets = set([
            "red", "black", "green", ICONS["red"], ICONS["black"], ICONS["green"]
        ])

        if self.tokens[3].lower() in valid_color_bets:
            ROULETE_QUEUE.add(self.user_id)
            if self.tokens[3] == ICONS["red"]:
                self.user_data.roulette_bet.append(("red", self.bet_amount))
            elif self.tokens[3] == ICONS["black"]:
                self.user_data.roulette_bet.append(("black", self.bet_amount))
            elif self.tokens[3] == ICONS["green"]:
                self.user_data.roulette_bet.append(("green", self.bet_amount))
            else:
                self.user_data.roulette_bet.append((self.tokens[3], self.bet_amount))
            return True, "success"

        self.bet_number = self.tokens[3]
        try:
            self.bet_number = int(self.tokens[3])
        except ValueError:
            return False, "Invalid bet type: Cant bet on %s" % self.bet_number

        if self.bet_number <= 0 or self.bet_number > 28:
            return False, "Invalid bet number"

        return True, None
