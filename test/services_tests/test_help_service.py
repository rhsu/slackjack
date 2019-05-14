from services.help_service import HelpService


def test_works():
    service = HelpService()
    expected_result = "*bet* <amount>: _bets <amount> of money for blackjack_\n"\
                      "*hit*: or *play*: _starts blackjack after money is bet_\n"\
                      "*put* <amount>: _puts <amount> of money for roulette_\n*"\
                      "rebrand* <username>: _renames to <username>_\n"\
                      "*register* <username>: _registers <username>_\n"\
                      "*start*: _starts the roulette game_\n"\
                      "*status*: _checks the total money_\n"\
                      "*stay*: or *stand*: _stay commmand in blackjack after game is played_\n"\
                      "*rebuy*: _refills back to 100 dollars. (Kenny is that you? Did you run out of money already?)_"
    assert service.help() == expected_result
