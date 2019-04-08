import pytest
from global_store import GLOBAL_STORE
from models.card import Card
from models.user_data import UserData


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


def _setup_default_user_data():
    if "fake_id" in GLOBAL_STORE:
        return GLOBAL_STORE["fake_id"]
    user_data = UserData("someone")
    user_data.bet = 100
    user_data.money = 100
    GLOBAL_STORE["fake_id"] = UserData("someone")
    return user_data
