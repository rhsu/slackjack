from services.roulette_command_parser import RouletteCommandParser


def test_valid_betting_on_black():
    command = "put 50 on black"
    response = RouletteCommandParser(command).is_valid()
    assert response == (True, "success")


def test_valid_betting_on_red():
    command = "put 50 on red"
    assert RouletteCommandParser(command).is_valid()


def test_valid_betting_on_number():
    command = "put 50 on 5"
    assert RouletteCommandParser(command).is_valid()
