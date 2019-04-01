from services.endgame_service import EndgameService


def test_dealer_busted(
    endgame_service_fixture, default_user_data, some_busted_hand, winning_hand
):
    default_user_data["dealer_hand"] = some_busted_hand
    default_user_data["hand"] = winning_hand
    result = endgame_service_fixture.determine()
    assert result == "Dealer has: Q :spades: K :spades: J :spades:. someone "\
                     "has: 9 :clubs: 2 :clubs: 10 :clubs:. Dealer busted. "\
                     "someone wins!"


def test_dealer_wins(
    endgame_service_fixture, default_user_data, losing_hand, winning_hand
):
    default_user_data["dealer_hand"] = winning_hand
    default_user_data["hand"] = losing_hand
    result = endgame_service_fixture.determine()
    assert result == "Dealer has: 9 :clubs: 2 :clubs: 10 :clubs:. someone "\
                     "has: 2 :hearts: 2 :spades. someone loses!"


# def test_dealer_loses(endgame_service_fixture):
#     # EndgameService(fake_user_id)
#     from pdb import set_trace; set_trace()
#     pass


# def test_cant_stand():
#     from pdb import set_trace; set_trace()
#     pass
