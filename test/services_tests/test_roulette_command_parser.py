from services.roulette_command_parser import RouletteCommandParser


def test_valid_betting_on_black(default_user_data, default_id):
    command = "put 50 on black"
    response = RouletteCommandParser(
        command, default_id, default_user_data).is_valid()
    assert response == (True, "success")


def test_valid_betting_on_red(default_user_data, default_id):
    command = "put 50 on red"
    response = RouletteCommandParser(
        command, default_id, default_user_data).is_valid()
    assert response == (True, "success")


def test_valid_betting_on_number(default_user_data, default_id):
    command = "put 50 on 5"
    response = RouletteCommandParser(
        command, default_id, default_user_data).is_valid()
    assert response == (True, "success")
