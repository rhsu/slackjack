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

            # TODO need to rethink this logic
            # I think the reset messed this up. Need a better way to reset.
            if len(self.user_data["dealer_hand"]) == 0:
                self.user_data["dealer_hand"].append(self.deck().deal())
                self.user_data["dealer_hand"].append(self.deck().deal())

            return "Dealer's hand is: %s and :question:. %s's hand is %s" % (
                    self.user_data["dealer_hand"][0],
                    self.user_data["username"],
                    hand_string(self.hand())
                )
        else:
            self.hand().append(self.deck().deal())
            total_value = 0
            for card in self.hand():
                total_value += card.value()
            if total_value == 21:
                result = hand_string(self.hand())
                # resetting
                self.user_data["hand"] = []
                self.user_data["dealer_hand"] = []
                return "21: %s Wins %s dollars! % s" % (
                    self.user_data["username"], self.user_data["bet"], result)
            elif total_value > 21:
                result = hand_string(self.hand())
                self.user_data["hand"] = []
                self.user_data["dealer_hand"] = []
                return "BUSTED! %s. %s Loses %s dollars!" % (
                    result, self.user_data["username"], self.user_data["bet"])
            else:
                return "Dealer's hand is: %s and :question:. %s's hand is %s" % (
                        self.user_data["dealer_hand"][0],
                        self.user_data["username"],
                        hand_string(self.hand())
                    )
