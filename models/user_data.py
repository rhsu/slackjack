from models.deck import Deck


class UserData:
    def __init__(self, username):
        self.bet = 0
        self.dealer_hand = []
        self.deck = Deck()
        self.hand = []
        self.money = 100
        self.username = username

    def reset_hands(self):
        self.hand = []
        self.dealer_hand = []

    def reset_bets(self):
        self.bet = 0

    # def apply_lost(self):
    #     self.money -= self.bet()
    #     self.userdata["bet"] = 0
    #     pass

    # def apply_win(self):
    #     pass

    # def apply_tie(self):
    #     pass
