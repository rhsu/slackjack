class HelpService:
    def __init__(self):
        pass

    def help(self):
        help_text = [
            "*bet* <amount>: _bets <amount> of money for blackjack_",
            "*hit*: or *play*: _starts blackjack after money is bet_",
            "*put* <amount>: _puts <amount> of money for roulette_",
            "*rebrand* <username>: _renames to <username>_",
            "*register* <username>: _registers <username>_",
            "*start*: _starts the roulette game_",
            "*status*: _checks the total money_",
            "*stay*: or *stand*: _stay commmand in blackjack after game is played_",
            "*rebuy*: _refills back to 100 dollars. (Kenny is that you? Did you run out of money already?)_"
        ]

        return "\n".join(help_text)
