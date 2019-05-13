class MockDealerService:
    def __init__(self, dealer_hand):
        self.dealer_hand = dealer_hand

    def play(self):
        return self.dealer_hand


class MockGameService:
    def play(self):
        return "MOCK"


class MockEndgameService:
    def determine(self):
        return "EndGameService"


class MockSimulationService:
    def __init__(self):
        pass

    def simulate(self):
        return "simulate"

    def flip(self):
        return "flip"
