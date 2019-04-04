class BettingService:
    def __init__(self, userdata, gameservice):
        self.userdata = userdata
        self.gameservice = gameservice

    def money(self):
        return self.userdata["money"]

    def username(self):
        return self.userdata["username"]

    def bet(self):
        return self.userdata["bet"]

    def place_bet(self, amount):
        if self.money() == 0:
            return "%s: Can't play. Not enough money." % self.username()
        if amount > self.money():
            return "%s: Not enough money. Can't bet %s" % (
                self.username(), amount)
        if self.bet() != 0:
            return "%s has already placed a bet. try `hit` or `stay`" % (
                self.username()
            )

        self.userdata["bet"] = amount
        result = self.gameservice.play()
        return "%s: has bet %s. %s" % (self.username(), amount, result)
