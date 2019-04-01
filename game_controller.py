from global_store import GLOBAL_STORE
from services.dealer_service import DealerService
from services.game_service import GameService
from services.rebrand_service import RebrandService
from services.register_service import RegisterService
from utils.hand_util import hand_sum, hand_string
from services.endgame_service import EndgameService


class GameController:
    def __init__(self, user_id):
        self.user_id = user_id
        # TODO maybe make a different controller for registering?
        if user_id in GLOBAL_STORE:
            self.game_service = GameService(GLOBAL_STORE[user_id])
            self.dealer_service = DealerService(GLOBAL_STORE[user_id])
            self.dealer_service.init_dealer()

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
        elif command.startswith("bet"):
            # check if user exists
            if self.user_id not in GLOBAL_STORE:
                return "You are not registered"
            parse = command.split(" ")
            if len(parse) < 2:
                message = "must supply an amount to bet"
            else:
                try:
                    bet_amount = int(parse[1])
                except ValueError:
                    return "invalid bet amount"
                GLOBAL_STORE[self.user_id]["money"] += bet_amount
                message = "A :spades: J :heart: BlackJack! %s Wins! Total: %s" % (GLOBAL_STORE[self.user_id]["username"], GLOBAL_STORE[self.user_id]["money"])
        elif command.startswith("hit") or command.startswith("play"):
            return self.game_service.play()
        elif command.startswith("stay") or command.startswith("stand"):
            endgame = EndgameService(self.user_id, GLOBAL_STORE[self.user_id])
            return endgame.determine()
            # pass
            # players_hand = GLOBAL_STORE[self.user_id]["hand"]
            # player_sum = hand_sum(players_hand)
            # if not len(players_hand):
            #     return "Can't stand. Must `play` or `hit` first"
            # dealer_hand = self.dealer_service.play()
            # dealer_sum = hand_sum(dealer_hand)
            # # TODO what happens if both players get 21? for now Im giving it
            # # to the player
            # if hand_sum(dealer_hand) > 21:
            #     GLOBAL_STORE[self.user_id]["hand"] = []
            #     GLOBAL_STORE[self.user_id]["dealer_hand"] = []
            #     return "Dealer has: %s. %s has: %s. Dealer busted. %s wins!" % (
            #         hand_string(dealer_hand),
            #         GLOBAL_STORE[self.user_id]["username"],
            #         hand_string(players_hand),
            #         GLOBAL_STORE[self.user_id]["username"]
            #     )
            # elif player_sum > dealer_sum:
            #     GLOBAL_STORE[self.user_id]["hand"] = []
            #     GLOBAL_STORE[self.user_id]["dealer_hand"] = []
            #     return "Dealer has: %s. %s has: %s. %s wins!" % (
            #         hand_string(dealer_hand),
            #         GLOBAL_STORE[self.user_id]["username"],
            #         hand_string(players_hand),
            #         GLOBAL_STORE[self.user_id]["username"]
            #     )
            # else:
            #     GLOBAL_STORE[self.user_id]["hand"] = []
            #     GLOBAL_STORE[self.user_id]["dealer_hand"] = []
            #     return "Dealer has: %s. %s has: %s. %s loses!" % (
            #         hand_string(dealer_hand),
            #         GLOBAL_STORE[self.user_id]["username"],
            #         hand_string(players_hand),
            #         GLOBAL_STORE[self.user_id]["username"]
            #     )
        return message
