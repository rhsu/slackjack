from global_store import GLOBAL_STORE
from utils.hand_util import hand_sum, hand_string
from services.dealer_service import DealerService


class EndgameService:
    def __init__(self, user_id, user_data):
        self.user_data = user_data
        self.user_id = user_id

    def reset(self):
        self.user_data["hand"] = []
        self.user_data["dealer_hand"] = []

    def determine(self):
        players_hand = GLOBAL_STORE[self.user_id]["hand"]
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
            GLOBAL_STORE[self.user_id]["hand"] = []
            GLOBAL_STORE[self.user_id]["dealer_hand"] = []
            return "Dealer has: %s. %s has: %s. Dealer busted. %s wins!" % (
                hand_string(dealer_hand),
                GLOBAL_STORE[self.user_id]["username"],
                hand_string(players_hand),
                GLOBAL_STORE[self.user_id]["username"]
            )
        elif player_sum > dealer_sum:
            GLOBAL_STORE[self.user_id]["hand"] = []
            GLOBAL_STORE[self.user_id]["dealer_hand"] = []
            return "Dealer has: %s. %s has: %s. %s wins!" % (
                hand_string(dealer_hand),
                GLOBAL_STORE[self.user_id]["username"],
                hand_string(players_hand),
                GLOBAL_STORE[self.user_id]["username"]
            )
        else:
            GLOBAL_STORE[self.user_id]["hand"] = []
            GLOBAL_STORE[self.user_id]["dealer_hand"] = []
            return "Dealer has: %s. %s has: %s. %s loses!" % (
                hand_string(dealer_hand),
                GLOBAL_STORE[self.user_id]["username"],
                hand_string(players_hand),
                GLOBAL_STORE[self.user_id]["username"]
            )
