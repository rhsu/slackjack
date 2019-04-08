# TODO. I don't think I need this anymore
class Service:
    def __init__(self, userdata):
        self.userdata = userdata

    def username(self):
        return self.userdata.username

    def hand(self):
        return self.userdata.hand

    def deck(self):
        return self.userdata.deck

    def dealer_hand(self):
        return self.userdata.dealer_hand

    def bet(self):
        return self.userdata.bet

    def money(self):
        return self.userdata.money
