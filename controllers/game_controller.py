from global_store import GLOBAL_STORE
from services.dealer_service import DealerService
from services.endgame_service import EndgameService
from services.game_service import GameService
from services.rebrand_service import RebrandService
from services.register_service import RegisterService
from services.betting_service import BettingService


class GameController:
    def __init__(self, user_id):
        self.user_id = user_id
        # TODO maybe make a different controller for registering?
        if user_id in GLOBAL_STORE:
            self.game_service = GameService(GLOBAL_STORE[user_id])
            self.dealer_service = DealerService(GLOBAL_STORE[user_id])
            self.endgame_service = EndgameService(
                GLOBAL_STORE[user_id], self.dealer_service)
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

            # TODO move this to service later
            if GLOBAL_STORE[self.user_id]["bet"] != 0:
                return "%s has already placed a bet. try `hit` or `stay`" % (
                    GLOBAL_STORE[self.user_id]["username"]
                )
            parse = command.split(" ")
            if len(parse) < 2:
                message = "must supply an amount to bet"
            else:
                try:
                    bet_amount = int(parse[1])
                except ValueError:
                    return "invalid bet amount"
                if bet_amount <= 0:
                    return "invalid bet amount"
                return self.betting_service.bet(bet_amount)
        elif command.startswith("hit") or command.startswith("play"):
            return self.game_service.play()
        elif command.startswith("stay") or command.startswith("stand"):
            return self.endgame_service.determine()
        elif command.startswith("rebuy"):
            if GLOBAL_STORE[self.user_id]["money"] == 0:
                GLOBAL_STORE[self.user_id]["money"] = 100
                return "rebought"
            else:
                return "you still have money"
        return message
