import pytest
from models.deck import Deck
from models.card import Card


@pytest.fixture
def default_user_data():
    user_data = {
        "username": "someone",
        "hand": [],
        "deck": Deck(),
        "dealer_hand": [],
    }
    return user_data


@pytest.fixture
def some_busted_hand():
    return [
        Card("Q", ":spades:"),
        Card("K", ":spades:"),
        Card("J", ":spades:"),
    ]
