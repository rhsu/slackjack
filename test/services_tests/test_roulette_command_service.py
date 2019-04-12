from services.roulette_command_service import RouletteCommandService


def test_valid_betting_on_black(default_user_data, default_id):
    command = "put 50 on black"
    response = RouletteCommandService(
        command, default_id, default_user_data).is_valid()
    assert response == (True, "success")


def test_valid_betting_on_red(default_user_data, default_id):
    command = "put 50 on red"
    response = RouletteCommandService(
        command, default_id, default_user_data).is_valid()
    assert response == (True, "success")


def test_valid_betting_on_number(default_user_data, default_id):
    command = "put 50 on 5"
    response = RouletteCommandService(
        command, default_id, default_user_data).is_valid()
    assert response == (True, "success")


def test_not_valid_put_command(default_user_data, default_id):
    command = "put 50 on 5 please"
    response = RouletteCommandService(
        command, default_id, default_user_data).is_valid()
    assert response == (False, "Invalid *put* command")


def test_not_valid_invalid_bet(default_user_data, default_id):
    command = "put donkey on 5"
    response = RouletteCommandService(
        command, default_id, default_user_data).is_valid()
    assert response == (False, "Invalid bet amount")


def test_not_valid_negative_bet(default_user_data, default_id):
    command = "put -5 on 5"
    response = RouletteCommandService(
        command, default_id, default_user_data).is_valid()
    assert response == (False, "Invalid bet amount")


def test_not_valid_missing_on(default_user_data, default_id):
    command = "put 5 in 5"
    response = RouletteCommandService(
        command, default_id, default_user_data).is_valid()
    assert response == (False, "Invalid *put* command: missing *on* keyword")
