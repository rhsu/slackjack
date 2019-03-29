from global_store import GLOBAL_STORE
from models.card import Card
from models.deck import Deck
import pytest


@pytest.fixture
def default_user_data():
    user_data = {
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


@pytest.fixture
def global_store():
    return GLOBAL_STORE
