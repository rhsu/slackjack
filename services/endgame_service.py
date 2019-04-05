from services.service import Service
from utils.hand_util import hand_sum, hand_string


class EndgameService(Service):
    def __init__(self, userdata, dealer_service):
        Service.__init__(self, userdata)
        self.dealer_service = dealer_service

    def _reset(self):
        self.userdata["hand"] = []
        self.userdata["dealer_hand"] = []

    def determine(self):
        players_hand = self.userdata["hand"]
        player_sum = hand_sum(players_hand)
        player_name = self.userdata["username"]
        player_hand_string = hand_string(players_hand)
        if not len(players_hand):
            return "Can't stand. Must `bet` first"
        dealer_hand = self.dealer_service.play()
        dealer_hand_string = hand_string(dealer_hand)
        dealer_sum = hand_sum(dealer_hand)
        bet_amount = self.userdata["bet"]

        self._reset()
        if player_sum > 21:
            self.userdata["money"] -= self.userdata["bet"]
            self.userdata["bet"] = 0
            return "%s busted: %s and loses %s dollars" % (
                player_name, player_hand_string, bet_amount)
        if dealer_sum > 21:
            self.userdata["money"] += self.userdata["bet"]
            self.userdata["bet"] = 0
            return "Dealer has: %s. %s has: %s. Dealer busted. %s wins %s dollars!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name,
                bet_amount
            )
        elif player_sum > dealer_sum:
            self.userdata["money"] += self.userdata["bet"]
            self.userdata["bet"] = 0
            return "Dealer has: %s. %s has: %s. %s wins %s dollars!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name,
                bet_amount
            )
        elif player_sum == dealer_sum:
            self.userdata["bet"] = 0
            return "Dealer has: %s. %s has: %s. %s ties!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name
            )
        else:
            self.userdata["money"] -= self.userdata["bet"]
            self.userdata["bet"] = 0
            return "Dealer has: %s. %s has: %s. %s loses %s dollars!" % (
                dealer_hand_string,
                player_name,
                player_hand_string,
                player_name,
                bet_amount
            )
