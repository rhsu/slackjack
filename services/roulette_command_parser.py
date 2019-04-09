class RouletteCommandParser:
    def __init__(self, command):
        self.command = command

    def is_valid(self):
        tokens = self.command.split(" ")

        # look at all the tokens
        if len(tokens) != 4:
            return False, "Invalid *put* command"

        # look at token 1
        bet_amount = tokens[1]
        # from pdb import set_trace; set_trace()
        try:
            bet_amount = int(tokens[1])
        except ValueError:
            return False, "Invalid bet amount"
            if bet_amount <= 0:
                return False, "Invalid bet amount"

        # look at token 2
        if tokens[2].lower() != "on":
            return False, "Invalid *put* command: missing *on* keyword"

        from pdb import set_trace; set_trace()

        # look at token 3
        if tokens[3].lower() == "red" or tokens[3].lower() == "black":
            return True, "success"

        bet_number = tokens[3]
        try:
            bet_number = int(tokens[3])
        except ValueError:
            return False, "Invalid bet number"
            if bet_number <= 0:
                return False, "Invalid bet number"

        return True, "success"
