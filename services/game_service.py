from utils.hand_util import hand_string


class GameService:
    def __init__(self, user_data):
        self.user_data = user_data

    def deck(self):
        return self.user_data["deck"]

    def hand(self):
        return self.user_data["hand"]

    def play(self):
        if len(self.hand()) == 0:
            self.hand().append(self.deck().deal())
            self.hand().append(self.deck().deal())
            return "Dealer's hand is: %s. Your hand is %s" % (
                    hand_string(self.user_data["dealer_hand"]),
                    hand_string(self.hand())
                )
        else:
            self.hand().append(self.deck().deal())
            total_value = 0
            for card in self.hand():
                total_value += card.value()
            if total_value == 21:
                result = hand_string(self.hand())
                self.user_data["hand"] = []
                self.user_data["dealer_hand"] = []
                return "21: You Win % s" % (result)
            elif total_value > 21:
                result = hand_string(self.hand())
                self.user_data["hand"] = []
                self.user_data["dealer_hand"] = []
                return "BUSTED!: % s. Restarted." % result
            else:
                return "Dealer's hand is: %s. Your hand is %s" % (
                    hand_string(self.user_data["dealer_hand"]),
                    hand_string(self.hand())
                )
