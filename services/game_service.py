from utils.hand_util import hand_string


class GameService:
    def __init__(self, user_data, endgame_service):
        self.user_data = user_data
        self.endgame_service = endgame_service

    def deck(self):
        return self.user_data["deck"]

    def hand(self):
        return self.user_data["hand"]

    def username(self):
        return self.user_data["username"]

    def money(self):
        return self.user_data["money"]

    def play(self):
        if self.user_data["money"] == 0:
            return "%s: Can't play. YOU HAVE NO MONEY" % self.username()
        if self.user_data["bet"] == 0:
            return "%s: Can't play. Must `bet` first" % self.username()

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
            if total_value > 21:
                return self.endgame_service.determine()
            else:
                return "Dealer's hand is: %s and :question:. %s's hand is %s" % (
                        self.user_data["dealer_hand"][0],
                        self.user_data["username"],
                        hand_string(self.hand())
                    )
