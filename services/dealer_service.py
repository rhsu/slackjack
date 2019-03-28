from utils.hand_util import hand_sum


class DealerService:
    def __init__(self, user_data):
        self.user_data = user_data

    def dealer_hand(self):
        return self.user_data["dealer_hand"]

    def deck(self):
        return self.user_data["deck"]

    def init_dealer(self):
        if (len(self.dealer_hand()) != 0):
            raise RuntimeError("dealer is already initialized")
        self.dealer_hand().append(self.deck().deal())
        self.dealer_hand().append(self.deck().deal())

    def play(self):
        while(hand_sum(self.dealer_hand()) <= 16):
            self.dealer_hand().append(self.deck().deal())
        return self.dealer_hand()
