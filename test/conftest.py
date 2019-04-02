from global_store import GLOBAL_STORE
from services.endgame_service import EndgameService
from models.card import Card
from models.deck import Deck
import pytest


@pytest.fixture(autouse=True)
def run_around_test():
    yield
    GLOBAL_STORE.clear()


@pytest.fixture
def default_user_data():
    return _setup_default_user_data()


@pytest.fixture
def some_busted_hand():
    return [
        Card("Q", ":spades:"),
        Card("K", ":spades:"),
        Card("J", ":spades:"),
    ]


@pytest.fixture
def losing_hand():
    return [
        Card("2", ":hearts:"),
        Card("2", ":spades"),
    ]


@pytest.fixture
def winning_hand():
    return [
        Card("9", ":clubs:"),
        Card("2", ":clubs:"),
        Card("10", ":clubs:"),
    ]


@pytest.fixture
def global_store():
    return GLOBAL_STORE


@pytest.fixture
def endgame_service_fixture():
    _setup_default_user_data()
    return EndgameService("fake_id")


def _setup_default_user_data():
    if "fake_id" in GLOBAL_STORE:
        return GLOBAL_STORE["fake_id"]
    user_data = {
        "username": "someone",
        "hand": [],
        "deck": Deck(),
        "dealer_hand": [],
    }
    GLOBAL_STORE["fake_id"] = user_data
    return user_data


# @pytest.fixture
# def mock_dealer_service():
#     class MockDealerService:
#         def __init__(self, dealer_hand):
#             self.dealer_hand = dealer_hand

#         def play(self):
#             pass
#     return MockDealerService()
