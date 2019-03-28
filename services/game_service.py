class GameService:
    def __init__(self, user_data):
        self.user_data = user_data
        self.deck = user_data["deck"]
        self.hand = user_data["hand"]

    def play(self):
        if len(self.hand) == 0:
            self.hand.append(self.deck.deal())
            self.hand.append(self.deck.deal())
            return self._hand_to_string()
        else:
            self.hand.append(self.deck.deal())
            total_value = 0
            for card in self.hand:
                total_value += card.value()
            if total_value == 21:
                return "Black Jack You Win % s" % (self._hand_to_string())
            elif total_value > 21:
                hand_string = self._hand_to_string()
                self.user_data["hand"] = []
                return "BUSTED!: % s. Restarted." % (hand_string)
            else:
                return "Your hand is %s" % (self._hand_to_string())

    def _hand_to_string(self):
        return " ".join(map(lambda x: str(x), self.hand))
