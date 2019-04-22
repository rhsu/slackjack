from services.service import Service
from utils.hand_util import hand_sum, hand_string


class EndgameService(Service):
    def __init__(self, userdata, dealer_service):
        Service.__init__(self, userdata)
        self.dealer_service = dealer_service

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

        # this is not ideal but I find it acceptable
        self._userdata.reset_hands()
        if player_sum > 21:
            self._decrease_money()
            self.set_bet(0)
            return "%s busted: %s and loses %s dollars" % (
                self.username(), player_hand_string, display_bet)
        if dealer_sum > 21:
            self._increase_money()
            self.set_bet(0)
            return "Dealer has: %s. %s has: %s. Dealer busted. %s wins "\
                   "%s dollars!" % (
                        dealer_hand_string,
                        self.username(),
                        player_hand_string, 
                        self.username(),
                        display_bet,
                    )
        elif player_sum > dealer_sum:
            self._increase_money()
            self.set_bet(0)
            return "Dealer has: %s. %s has: %s. %s wins %s dollars!" % (
                dealer_hand_string,
                self.username(),
                player_hand_string,
                self.username(),
                display_bet,
            )
        elif player_sum == dealer_sum:
            self.set_bet(0)
            return "Dealer has: %s. %s has: %s. %s ties!" % (
                dealer_hand_string,
                self.username(),
                player_hand_string,
                self.username(),
            )
        else:
            self._decrease_money()
            self.set_bet(0)
            return "Dealer has: %s. %s has: %s. %s loses %s dollars!" % (
                dealer_hand_string,
                self.username(),
                player_hand_string,
                self.username(),
                display_bet,
            )

    def _decrease_money(self):
        self._userdata.money -= self.bet()
        return self._userdata.money

    def _increase_money(self):
        self._userdata.money += self.bet()
        return self._userdata.money
