from utils.hand_util import hand_sum, hand_string


class EndgameService:
    def __init__(self, user_data, dealer_service):
        self.user_data = user_data
        self.dealer_service = dealer_service

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
        dealer_hand = self.dealer_service.play()
        dealer_hand_string = hand_string(dealer_hand)
        dealer_sum = hand_sum(dealer_hand)

        self._reset()
        if dealer_sum > 21:
            return "Dealer has: %s. %s has: %s. Dealer busted. %s wins %s dollars!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name,
                self.user_data["bet"]
            )
        elif player_sum > dealer_sum:
            return "Dealer has: %s. %s has: %s. %s wins %s dollars!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name,
                self.user_data["bet"]
            )
        elif player_sum == dealer_sum:
            return "Dealer has: %s. %s has: %s. %s ties!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name
            )
        else:
            return "Dealer has: %s. %s has: %s. %s loses %s dollars!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name,
                self.user_data["bet"]
            )
