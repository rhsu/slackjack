from services.betting_service import BettingService
from test.mocks.mock_objects import MockGameService


def test_place_bet_when_no_money(default_user_data):
    game_service = MockGameService()
    default_user_data["money"] = 0
    service = BettingService(default_user_data, game_service)
    result = service.place_bet(5)
    assert result == "someone: Can't play. Not enough money."


def test_place_bet_when_not_enough_money(default_user_data):
    game_service = MockGameService()
    service = BettingService(default_user_data, game_service)
    result = service.place_bet(5000)
    assert result == "someone: Not enough money. Can't bet 5000"


def test_place_bet_when_bet_exists(default_user_data):
    game_service = MockGameService()
    service = BettingService(default_user_data, game_service)
    result = service.place_bet(1)
    assert result == "someone has already placed a bet. try `hit` or `stay`"


def test_place_bet_when_successful(default_user_data):
    game_service = MockGameService()
    default_user_data["bet"] = 0
    service = BettingService(default_user_data, game_service)
    result = service.place_bet(1)
    assert result == "someone: has bet 1. MOCK"
