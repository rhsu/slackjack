from global_store import GLOBAL_STORE, ROULETE_QUEUE
from services.betting_service import BettingService
from services.dealer_service import DealerService
from services.endgame_service import EndgameService
from services.game_service import GameService
from services.rebrand_service import RebrandService
from services.rebuy_service import RebuyService
from services.register_service import RegisterService
from services.roulette_command_service import RouletteCommandService
from services.roulette_service import RouletteService
from services.help_service import HelpService


class GameController:
    def __init__(self, user_id):
        self.user_id = user_id
        self.roulette_service = RouletteService()
        self.help_service = HelpService()
        # TODO maybe make a different controller for registering?
        if user_id in GLOBAL_STORE:
            self.user_data = GLOBAL_STORE[user_id]
            self.rebuy_service = RebuyService(self.user_data)
            self.dealer_service = DealerService(self.user_data)
            self.endgame_service = EndgameService(
                self.user_data, self.dealer_service)
            self.game_service = GameService(
                self.user_data, self.endgame_service)
            self.betting_service = BettingService(
                self.user_data, self.game_service)

    def parse_command(self, command):
        command = command.lower()
        message = None
        if command.startswith("register"):
            parse = command.split(" ")
            if len(parse) < 2:
                return "must supply a username with register"
            else:
                message = RegisterService(self.user_id, parse[1]).register()
                return message
        elif command.startswith("rebrand"):
            # TODO maybe put parse = command.split(" ") at the top
            parse = command.split(" ")
            if len(parse) < 2:
                return "must supply a username with rebrand"
            return RebrandService(self.user_id, parse[1]).rebrand()
        elif command.startswith("status"):
            return f"{self.user_data.username} has {self.user_data.money}"
        elif command.startswith("bet"):
            # check if user exists
            if self.user_id not in GLOBAL_STORE:
                return "You are not registered"

            # check if the user supplied a bet amount
            parse = command.split(" ")
            if len(parse) < 2:
                return "must supply an amount to bet"

            # check if that amount is valid
            try:
                bet_amount = int(parse[1])
            except ValueError:
                return "invalid bet amount"
            if bet_amount <= 0:
                return "invalid bet amount"

            return self.betting_service.place_bet(bet_amount)
        elif command.startswith("hit") or command.startswith("play"):
            return self.game_service.play()
        elif command.startswith("stay") or command.startswith("stand"):
            return self.endgame_service.determine()
        elif command.startswith("put"):
            parsed = RouletteCommandService(
                command, self.user_id, self.user_data).is_valid()
            if parsed[0]:
                return "%s has joined" % self.user_data.username
            else:
                return "error: %s" % (parsed[1])
        elif command.startswith("start"):
            result, color = self.roulette_service.spin()
            ret_val = f"the result is *{result}* (*{color}*) \n"
            for user_id in ROULETE_QUEUE:
                curr_user = GLOBAL_STORE[user_id]
                if curr_user.roulette_bet == color:
                    curr_user.money += curr_user.roulette_bet_amount
                    ret_val += "*%s* bet on *%s*. *%s* won \n" % (
                        curr_user.username,
                        curr_user.roulette_bet,
                        curr_user.username)
                elif curr_user.roulette_bet == result:
                    curr_user.money += curr_user.roulette_bet_amount
                    ret_val += "*%s* bet on *%s*. *%s* won. \n" % (
                        curr_user.username,
                        curr_user.roulette_bet,
                        curr_user.username)
                else:
                    curr_user.money -= curr_user.roulette_bet_amount
                    ret_val += "*%s* bet on *%s*. *%s* lost. \n" % (
                        curr_user.username,
                        curr_user.roulette_bet,
                        curr_user.username)
            del ROULETE_QUEUE[:]
            return ret_val
        elif command.startswith("rebuy"):
            return self.rebuy_service.rebuy()
        elif command.startswith("help"):
            return self.help_service.help()
        return message
