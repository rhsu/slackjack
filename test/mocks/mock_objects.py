class MockDealerService:
    def __init__(self, dealer_hand):
        self.dealer_hand = dealer_hand

    def play(self):
        return self.dealer_hand


class MockGameService:
    def play(self):
        return "MOCK"
