from services.game_service import GameService
from test.mocks.mock_objects import MockEndgameService


def test_play_works_with_no_hand(default_user_data):
    service = GameService(default_user_data, MockEndgameService())
    response = service.play()
    assert response is not None
    assert len(service.hand()) == 2


def test_busted(default_user_data, some_busted_hand):
    default_user_data.hand = some_busted_hand
    service = GameService(default_user_data, MockEndgameService())
    response = service.play()
    assert response == "EndGameService"
