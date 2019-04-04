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
            return "Can't stand. Must `bet` first"
        dealer_hand = self.dealer_service.play()
        dealer_hand_string = hand_string(dealer_hand)
        dealer_sum = hand_sum(dealer_hand)
        bet_amount = self.user_data["bet"]

        self._reset()
        if player_sum > 21:
            self.user_data["money"] -= self.user_data["bet"]
            self.user_data["bet"] = 0
            return "%s busted: %s and loses %s dollars" % (
                player_name, player_hand_string, bet_amount)
        if dealer_sum > 21:
            self.user_data["money"] += self.user_data["bet"]
            self.user_data["bet"] = 0
            return "Dealer has: %s. %s has: %s. Dealer busted. %s wins %s dollars!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name,
                bet_amount
            )
        elif player_sum > dealer_sum:
            self.user_data["money"] += self.user_data["bet"]
            self.user_data["bet"] = 0
            return "Dealer has: %s. %s has: %s. %s wins %s dollars!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name,
                bet_amount
            )
        elif player_sum == dealer_sum:
            self.user_data["bet"] = 0
            return "Dealer has: %s. %s has: %s. %s ties!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name
            )
        else:
            self.user_data["money"] -= self.user_data["bet"]
            self.user_data["bet"] = 0
            return "Dealer has: %s. %s has: %s. %s loses %s dollars!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name,
                bet_amount
            )
