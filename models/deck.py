from random import shuffle
from models.card import Card


def RANKS():
    return ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def SUITS():
    return [":clubs:", ":diamonds:", ":hearts:", ":spades:"]


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS() for suit in SUITS()]

    def shuffle(self):
        shuffle(self.cards)

    def deal(self):
        self.cards.pop()

    def __str__(self):
        result = ",".join(map(lambda x: str(x), self.cards))
        return result
