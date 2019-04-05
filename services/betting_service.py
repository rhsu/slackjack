from services.service import Service


class BettingService(Service):
    def __init__(self, userdata, gameservice):
        Service.__init__(self, userdata)
        self.gameservice = gameservice

    def place_bet(self, amount):
        if self.money() == 0:
            return "%s: Can't play. Not enough money." % self.username()
        if amount > self.money():
            return "%s: Can't bet %s. Not enough money." % (
                self.username(), amount)
        if self.bet() != 0:
            return "%s: Bet already placed. Try `hit` or `stay`" % (
                self.username()
            )

        self.userdata["bet"] = amount
        result = self.gameservice.play()
        return "%s has bet %s. %s" % (self.username(), amount, result)
