class BettingService:
    def __init__(self, userdata, gameservice):
        self.userdata = userdata
        self.gameservice = gameservice
        pass

    def money(self):
        return self.userdata["money"]

    def username(self):
        return self.userdata["username"]

    # in the controller outside
    # check if bet is a number
    # check if bet is valid
    # let's start with betting as a decimal precision 2
    def bet(self, amount):
        if amount > self.money():
            return "%s: Not enough money. Can't bet %s" % (
                self.username(), amount)

        self.userdata["bet"] = amount
        result = self.gameservice.play()
        return "%s: has bet %s. %s" % (self.username(), amount, result)
