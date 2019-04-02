from services.endgame_service import EndgameService
from test.mocks.mock_objects import MockDealerService


# TODO can't really test this unless I stub. dealer_service.play()
def test_dealer_busted(default_user_data, some_busted_hand, winning_hand):
    mock_dealer_service = MockDealerService(some_busted_hand)

    endgame_service = EndgameService(default_user_data, mock_dealer_service)
    # default_user_data["dealer_hand"] = some_busted_hand
    default_user_data["hand"] = winning_hand
    from pdb import set_trace; set_trace()
    result = endgame_service.determine()
    assert result == "Dealer has: Q :spades: K :spades: J :spades:. someone "\
                     "has: 9 :clubs: 2 :clubs: 10 :clubs:. Dealer busted. "\
                     "someone wins!"


# def test_dealer_wins(
#     endgame_service_fixture, default_user_data, losing_hand, winning_hand
# ):
#     default_user_data["dealer_hand"] = winning_hand
#     default_user_data["hand"] = losing_hand
#     result = endgame_service_fixture.determine()  
#     assert result == "Dealer has: 9 :clubs: 2 :clubs: 10 :clubs:. someone "\
#                      "has: 2 :hearts: 2 :spades. someone loses!"


# def test_dealer_loses(
#     endgame_service_fixture, default_user_data, losing_hand, winning_hand
# ):
#     default_user_data["dealer_hand"] = losing_hand
#     default_user_data["hand"] = winning_hand
#     result = endgame_service_fixture.determine()
#     from pdb import set_trace; set_trace()
#     pass


# def test_cant_stand(endgame_service_fixture, default_user_data):
#     default_user_data["hand"] = []
#     result = endgame_service_fixture.determine()
#     assert result == "Can't stand. Must `play` or `hit` first"

# def test_both_have_21():
#     from pdb import set_trace; set_trace()
#     pass
