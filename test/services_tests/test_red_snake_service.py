from services.red_snake_service import RedSnakeService


def test_play(default_user_data):
    service = RedSnakeService(default_user_data)
    # default_user_data.money = 0
    # service = RebuyService(default_user_data)
    # assert service.rebuy() == "Rebuy successful. *someone* has 100 dollars"
    # assert default_user_data.money == 100
