class HelpService:
    def __init__(self):
        pass

    def help(self):
        help_text = [
            "*register* <username>: _registers <username>_",
            "*rebrand* <username>: _renames to <username>_",
            "*status*: _checks the total money_",
            "*bet* <amount>: _bets <amount> of money for blackjack_",
            "*hit*: or *play*: _starts blackjack after money is *bet*",
            "*stay*: or *stand*: _stay commmand in blackjack after game is played_",
            "*put* <amount>: _puts <amount> of money for roulette_",
            "*start*: _starts the roulette game_",
            "*rebuy*: _refills back to 100 dollars. (Kenny is that you? Did you run out of money already?)_"
        ]

        return "\n".join(help_text)
