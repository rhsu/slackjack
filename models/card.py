class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "%s %s" % (self.rank, self.suit)

    def value(self):
        try:
            return int(self.rank)
        except ValueError:
            if self.rank == "A":
                return 1
            return 10
