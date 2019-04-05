from global_store import GLOBAL_STORE, ROULETE_QUEUE
from services.betting_service import BettingService
from services.dealer_service import DealerService
from services.endgame_service import EndgameService
from services.game_service import GameService
from services.rebrand_service import RebrandService
from services.register_service import RegisterService
from services.roulette_service import RouletteService


class GameController:
    def __init__(self, user_id):
        self.user_id = user_id
        self.roulette_service = RouletteService()
        # TODO maybe make a different controller for registering?
        if user_id in GLOBAL_STORE:
            self.dealer_service = DealerService(GLOBAL_STORE[user_id])
            self.endgame_service = EndgameService(
                GLOBAL_STORE[user_id], self.dealer_service)
            self.game_service = GameService(
                GLOBAL_STORE[user_id], self.endgame_service)
            self.betting_service = BettingService(
                GLOBAL_STORE[user_id], self.game_service)

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
            # TODO need to check if user is registered
            # TODO maybe be able to check other people's statuses
            return "%s has %s dollars" % (
                GLOBAL_STORE[self.user_id]["username"],
                GLOBAL_STORE[self.user_id]["money"])
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
        elif command.startswith("join"):
            parse = command.split(" ")
            if len(parse) < 2:
                return "must supply an amount to bet"
            GLOBAL_STORE[self.user_id]["bet"] = parse[1]
            ROULETE_QUEUE.append(self.user_id)
            return "%s has joined" % GLOBAL_STORE[self.user_id]["username"]
        elif command.startswith("start"):
            result, color = self.roulette_service.spin()
            ret_val = "the result is %s (%s)" % (result, color)
            for user_id in ROULETE_QUEUE:
                if GLOBAL_STORE[user_id]["bet"] == color:
                    ret_val += "%s bet on %s. %s won" % (GLOBAL_STORE[user_id]["username"], color, GLOBAL_STORE[user_id]["username"])
                elif GLOBAL_STORE[user_id]["bet"] == result:
                    ret_val += "%s bet on (%s) %s won. " % (
                        GLOBAL_STORE[user_id]["username"], GLOBAL_STORE[user_id]["bet"], color, GLOBAL_STORE[user_id]["username"])
                else:
                    ret_val += "%s bet on %s (%s). %s lost. " % (
                        GLOBAL_STORE[user_id]["username"], GLOBAL_STORE[user_id]["bet"], color, GLOBAL_STORE[user_id]["username"])
            del ROULETE_QUEUE[:]
            return ret_val
        elif command.startswith("rebuy"):
            if GLOBAL_STORE[self.user_id]["money"] == 0:
                GLOBAL_STORE[self.user_id]["money"] = 100
                return "rebought"
            else:
                return "you still have money"
        return message
