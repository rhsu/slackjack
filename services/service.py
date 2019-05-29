class Service:
    def __init__(self, userdata):
        self._userdata = userdata

    def username(self):
        return self._userdata.username

    def hand(self):
        return self._userdata.hand

    def deck(self):
        return self._userdata.deck

    def dealer_hand(self):
        return self._userdata.dealer_hand

    def bet(self):
        return self._userdata.bet

    def set_bet(self, value):
        self._userdata.bet = value
        self._userdata.money -= value
        return value

    def money(self):
        return self._userdata.money

    def roulette_bet_amount(self):
        return self._userdata.roulette_bet_amount

    def set_money(self, value):
        self._userdata.money = value
        return value
