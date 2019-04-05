from services.endgame_service import EndgameService
from test.mocks.mock_objects import MockDealerService


def test_dealer_busted(default_user_data, some_busted_hand, winning_hand):
    mock_dealer_service = MockDealerService(some_busted_hand)
    default_user_data["hand"] = winning_hand
    endgame_service = EndgameService(default_user_data, mock_dealer_service)
    result = endgame_service.determine()
    assert result == "Dealer has: Q :spades: K :spades: J :spades:. someone "\
                     "has: 9 :clubs: 2 :clubs: 10 :clubs:. Dealer busted. "\
                     "someone wins 100 dollars!"


def test_dealer_wins(default_user_data, losing_hand, winning_hand):
    mock_dealer_service = MockDealerService(winning_hand)
    default_user_data["hand"] = losing_hand
    endgame_service = EndgameService(default_user_data, mock_dealer_service)
    result = endgame_service.determine()
    assert result == "Dealer has: 9 :clubs: 2 :clubs: 10 :clubs:. someone "\
                     "has: 2 :hearts: 2 :spades. someone loses 100 dollars!"


def test_dealer_loses(default_user_data, losing_hand, winning_hand):
    mock_dealer_service = MockDealerService(losing_hand)
    default_user_data["hand"] = winning_hand
    endgame_service = EndgameService(default_user_data, mock_dealer_service)
    result = endgame_service.determine()
    assert result == "Dealer has: 2 :hearts: 2 :spades. someone has: 9 "\
                     ":clubs: 2 :clubs: 10 :clubs:. someone wins 100 dollars!"


def test_cant_stand(default_user_data, winning_hand):
    mock_dealer_service = MockDealerService(winning_hand)
    default_user_data["hand"] = []
    endgame_service = EndgameService(default_user_data, mock_dealer_service)
    result = endgame_service.determine()
    assert result == "Can't stand. Must `bet` first"


def test_both_have_21(default_user_data, winning_hand):
    mock_dealer_service = MockDealerService(winning_hand)
    default_user_data["hand"] = winning_hand
    endgame_service = EndgameService(default_user_data, mock_dealer_service)
    result = endgame_service.determine()
    assert result == "Dealer has: 9 :clubs: 2 :clubs: 10 :clubs:. someone "\
                     "has: 9 :clubs: 2 :clubs: 10 :clubs:. someone ties!"
