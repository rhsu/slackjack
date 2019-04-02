from utils.hand_util import hand_sum


class DealerService:
    def __init__(self, user_data):
        self.user_data = user_data
        self._init_dealer()

    def dealer_hand(self):
        return self.user_data["dealer_hand"]

    def deck(self):
        return self.user_data["deck"]

    # TODO think about this one. Maybe this should just go into the constructor
    #      I think a new dealer_service is initialized every time anyways
    def _init_dealer(self):
        if (len(self.dealer_hand()) != 0):
            print("Initializing dealer but dealer didn't exist")
            return
            # TODO figure out why this is crashing later.
            # raise RuntimeError("dealer is already initialized")
        self.dealer_hand().append(self.deck().deal())
        self.dealer_hand().append(self.deck().deal())

    def play(self):
        while(hand_sum(self.dealer_hand()) <= 16):
            self.dealer_hand().append(self.deck().deal())
        return self.dealer_hand()
