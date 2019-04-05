from services.service import Service
from utils.hand_util import hand_sum, hand_string


class EndgameService(Service):
    def __init__(self, userdata, dealer_service):
        Service.__init__(self, userdata)
        self.dealer_service = dealer_service

    def _reset(self):
        self.userdata["hand"] = []
        self.userdata["dealer_hand"] = []

    def hand_sum(self):
        return hand_sum(self.hand())

    def determine(self):
        player_sum = hand_sum(self.hand())
        player_hand_string = hand_string(self.hand())
        if not len(self.hand()):
            return "Can't stand. Must `bet` first"
        dealer_hand = self.dealer_service.play()
        dealer_hand_string = hand_string(dealer_hand)
        dealer_sum = hand_sum(dealer_hand)

        # storing bet as local variable before setting to 0
        display_bet = self.bet()

        self._reset()
        if player_sum > 21:
            self.userdata["money"] -= self.userdata["bet"]
            self.userdata["bet"] = 0
            return "%s busted: %s and loses %s dollars" % (
                self.username(), player_hand_string, self.bet())
        if dealer_sum > 21:
            self.userdata["money"] += self.userdata["bet"]
            self.userdata["bet"] = 0
            return "Dealer has: %s. %s has: %s. Dealer busted. %s wins "\
                   "%s dollars!" % (
                        dealer_hand_string,
                        self.username(),
                        player_hand_string,
                        self.username(),
                        display_bet,
                    )
        elif player_sum > dealer_sum:
            self.userdata["money"] += self.userdata["bet"]
            self.userdata["bet"] = 0
            return "Dealer has: %s. %s has: %s. %s wins %s dollars!" % (
                dealer_hand_string,
                self.username(),
                player_hand_string,
                self.username(),
                display_bet,
            )
        elif player_sum == dealer_sum:
            self.userdata["bet"] = 0
            return "Dealer has: %s. %s has: %s. %s ties!" % (
                dealer_hand_string,
                self.username(),
                player_hand_string,
                self.username(),
            )
        else:
            self.userdata["money"] -= self.userdata["bet"]
            self.userdata["bet"] = 0
            return "Dealer has: %s. %s has: %s. %s loses %s dollars!" % (
                dealer_hand_string,
                self.username(),
                player_hand_string,
                self.username(),
                display_bet,
            )
