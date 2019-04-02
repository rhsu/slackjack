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
        player_name = self.user_data["username"]
        player_hand_string = hand_string(players_hand)
        if not len(players_hand):
            return "Can't stand. Must `play` or `hit` first"
        # TODO pass this in as a parameter
        dealer_service = DealerService(self.user_data)
        dealer_service.init_dealer()
        dealer_hand = dealer_service.play()
        dealer_hand_string = hand_string(dealer_hand)
        dealer_sum = hand_sum(dealer_hand)
        # TODO what happens if both players get 21? for now Im giving it
        # to the player
        self._reset()
        if dealer_sum > 21:
            return "Dealer has: %s. %s has: %s. Dealer busted. %s wins!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name
            )
        elif player_sum > dealer_sum:
            return "Dealer has: %s. %s has: %s. %s wins!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name
            )
        elif player_sum == dealer_sum:
            return "Dealer has: %s. %s has: %s. %s ties!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name
            )
        else:
            return "Dealer has: %s. %s has: %s. %s loses!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name
            )
