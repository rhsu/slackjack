from models.deck import Deck


class GameService:
    def __init__(self, user_data):
        # TODO put deck in user_data
        self.deck = Deck().shuffle()
        self.user_data = user_data

    def play(self):
        if len(self.user_data["hand"]) == 0:
            self.user_data["hand"] = []
            self.user_data["hand"].append(self.deck.deal())
            self.user_data["hand"].append(self.deck.deal())
            return self._hand_to_string()
        else:
            self.user_data["hand"].append(self.deck.deal())
            total_value = 0
            for card in self.user_data["hand"]:
                total_value += card.value()
            if total_value == 21:
                return "Black Jack You Win % s" % (self._hand_to_string())
            elif total_value > 21:
                return "You lose % s" % (self._hand_to_string())
            else:
                return "Your hand is %s" % (self._hand_to_string())

    def _hand_to_string(self):
        return " ".join(map(lambda x: str(x), self.user_data["hand"]))
