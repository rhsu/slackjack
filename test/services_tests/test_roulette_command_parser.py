from services.roulette_command_parser import RouletteCommandParser


def test_valid_betting_on_black():
    command = "put 50 on black"
    # from pdb import set_trace; set_trace()
    response = RouletteCommandParser(command).is_valid()
    # from pdb import set_trace; set_trace()
    assert response == (True, "success")
    pass


# def test_valid_betting_on_red():
#     command = "put 50 on red"
#     assert RouletteCommandParser(command).is_valid()
#     pass


# def test_valid_betting_on_number():
#     command = "put 50 on 5"
#     assert RouletteCommandParser(command).is_valid()
#     pass
