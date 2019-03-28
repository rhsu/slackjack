from services.game_service import GameService


def test_play_works_with_no_hand(default_user_data):
    service = GameService(default_user_data)
    response = service.play()
    assert response is not None
    assert len(service.hand()) == 2


def test_busted(default_user_data, some_busted_hand):
    default_user_data["hand"] = some_busted_hand
    service = GameService(default_user_data)
    response = service.play()
    assert "BUSTED!" in response
    assert "Q :spades:" in response
    assert "K :spades:" in response
    assert "J :spades:" in response
    assert "Restarted." in response
