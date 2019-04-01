from global_store import GLOBAL_STORE
from utils.hand_util import hand_sum, hand_string
from services.dealer_service import DealerService


class EndgameService:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_data = GLOBAL_STORE[user_id]

    def _reset(self):
        self.user_data["hand"] = []
        self.user_data["dealer_hand"] = []

    def determine(self):
        players_hand = self.user_data["hand"]
        player_sum = hand_sum(players_hand)
        if not len(players_hand):
            return "Can't stand. Must `play` or `hit` first"
        # TODO pass this in as a parameter
        dealer_service = DealerService(self.user_data)
        dealer_service.init_dealer()
        dealer_hand = dealer_service.play()
        dealer_sum = hand_sum(dealer_hand)
        # TODO what happens if both players get 21? for now Im giving it
        # to the player
        if hand_sum(dealer_hand) > 21:
            self._reset()
            return "Dealer has: %s. %s has: %s. Dealer busted. %s wins!" % (
                hand_string(dealer_hand),
                self.user_data["username"],
                hand_string(players_hand),
                self.user_data["username"]
            )
        elif player_sum > dealer_sum:
            self._reset()
            return "Dealer has: %s. %s has: %s. %s wins!" % (
                hand_string(dealer_hand),
                self.user_data["username"],
                hand_string(players_hand),
                self.user_data["username"]
            )
        else:
            self._reset()
            return "Dealer has: %s. %s has: %s. %s loses!" % (
                hand_string(dealer_hand),
                self.user_data["username"],
                hand_string(players_hand),
                self.user_data["username"]
            )
