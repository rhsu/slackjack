from services.service import Service


def test_username(default_user_data):
    assert Service(
        default_user_data).username() == default_user_data.username


def hand(default_user_data):
    assert Service(
        default_user_data).hand() == default_user_data.hand


def deck(default_user_data):
    assert Service(
        default_user_data).deck() == default_user_data.deck


def dealer_hand(default_user_data):
    assert Service(
        default_user_data).dealer_hand() == default_user_data.dealer_hand


def bet(default_user_data):
    assert Service(
        default_user_data).bet() == default_user_data.bet


def money(default_user_data):
    assert Service(
        default_user_data).money() == default_user_data.money
