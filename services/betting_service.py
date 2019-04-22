from services.service import Service


class BettingService(Service):
    def __init__(self, userdata, gameservice):
        Service.__init__(self, userdata)
        self.gameservice = gameservice

    def place_bet(self, amount):
        if self.money() == 0:
            return f"{self.username()}: Can't play. Not enough money."
        if amount > self.money():
            return f"{self.username()}: Can't bet {amount}. Not enough money."
        if self.bet() != 0:
            return f"{self.username()}: Bet already placed. Try `hit` or `stay`"

        self.set_bet(amount)
        result = self.gameservice.play()
        return "%s has bet %s. %s" % (self.username(), amount, result)
