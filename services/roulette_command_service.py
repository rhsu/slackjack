from global_store import ROULETE_QUEUE


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
        if tokens[3].lower() == "red" or tokens[3].lower() == "black":
            ROULETE_QUEUE.append(self.user_id)
            self.user_data.roulette_bet = tokens[3]
            self.user_data.roulette_bet_amount = bet_amount
            return True, "success"

        bet_number = tokens[3]
        try:
            bet_number = int(tokens[3])
        except ValueError:
            return False, "Invalid bet type: Cant bet on %s" % bet_number

        if bet_number <= 0 or bet_number > 28:
            return False, "Invalid bet number"

        ROULETE_QUEUE.append(self.user_id)
        self.user_data.roulette_bet = tokens[3]
        self.user_data.roulette_bet_amount = bet_amount
        return True, "success"
