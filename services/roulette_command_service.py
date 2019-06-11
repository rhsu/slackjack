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

        # Validation Token 3 here
        valid_color, color_error = self.__valid_color_bet()
        if not valid_color:
            valid_number, number_error = self.__valid_number_bet()
            if not valid_number:
                return False, f"{color_error} or {number_error}"

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

    def __valid_color_bet(self):
        valid_color_bets = set([
            "red", "black", "green", ICONS["red"], ICONS["black"], ICONS["green"]
        ])

        icon_color_mapping = {
            ICONS["red"]: "red",
            ICONS["black"]: "black",
            ICONS["green"]: "green"
        }

        bet_token = self.tokens[3]
        roulette_bet = self.user_data.roulette_bet

        if bet_token in valid_color_bets:
            if bet_token in icon_color_mapping:
                self.bet_number = icon_color_mapping["bet_token"]
            else:
                self.bet_number = bet_token
            return True, None
        else:
            return False, "Invalid Bet Color"

    def __valid_number_bet(self):
        try:
            self.bet_number = int(self.tokens[3])
        except ValueError:
            return False, "Invalid Bet Number"

        if self.bet_number <= 0 or self.bet_number > 28:
            return False, "Invalid Bet Number"

        return True, None
