from services.service import Service
from utils.hand_util import hand_sum


class DealerService(Service):
    def __init__(self, user_data):
        Service.__init__(self, user_data)
        self._init_dealer()

    # TODO think about this one. Maybe this should just go into the constructor
    #      I think a new dealer_service is initialized every time anyways
    def _init_dealer(self):
        if (len(self.dealer_hand()) != 0):
            return
            # TODO figure out why this is crashing later.
            # raise RuntimeError("dealer is already initialized")
        self.dealer_hand().append(self.deck().deal())
        self.dealer_hand().append(self.deck().deal())

    def play(self):
        while(hand_sum(self.dealer_hand()) <= 16):
            self.dealer_hand().append(self.deck().deal())
        return self.dealer_hand()
