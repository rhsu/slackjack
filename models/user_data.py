from models.deck import Deck


class UserData:
    def __init__(self, username):
        self.bet = 0
        self.dealer_hand = []
        self.deck = Deck()
        self.hand = []
        self.username = username
