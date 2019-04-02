class BettingService:
    def __init__(self, userdata, gameservice, bet):
        self.userdata = userdata
        self.gameservice = gameservice
        self.bet = bet
        pass

    def money(self):
        return self.userdata["money"]

    def username(self):
        return self.userdata["username"]

    # in the controller outside
    # check if bet is a number
    # check if bet is valid
    # let's start with betting as a decimal precision 2
    def bet(self):
        if self.bet > self.money:
            return "%s: Not enough money. Can't bet %s" % (
                self.username, self.money)

        self.userdata["money"] - self.bet
        return "%s: has bet %s" % (self.username, self.money)
