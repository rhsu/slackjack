from services.service import Service
from utils.hand_util import hand_string


class GameService(Service):
    def __init__(self, userdata, endgame_service):
        Service.__init__(self, userdata)
        self.endgame_service = endgame_service

    def play(self):
        if self.money() == 0:
            return f"{self.username()}: Can't play. YOU HAVE NO MONEY"
        if self.bet() == 0:
            return f"{self.username()}: Can't play. Must `bet` first"

        if len(self.hand()) == 0:
            self.hand().append(self.deck().deal())
            self.hand().append(self.deck().deal())

            # TODO need to rethink this logic
            # I think the reset messed this up. Need a better way to reset.
            if len(self.dealer_hand()) == 0:
                self.dealer_hand().append(self.deck().deal())
                self.dealer_hand().append(self.deck().deal())

            return "Dealer's hand is: %s and :question:. %s's hand is %s" % (
                self.dealer_hand()[0],
                self.username(),
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
                    self.dealer_hand()[0],
                    self.username(),
                    hand_string(self.hand())
                )
