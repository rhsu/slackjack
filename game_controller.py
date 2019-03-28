from global_store import GLOBAL_STORE
from models.deck import Deck
from services.game_service import GameService


class GameController:
    def __init__(self):
        pass

    def parse_command(self, user_id, command):
        command = command.lower()
        message = None
        if command.startswith("register"):
            parse = command.split(" ")
            if len(parse) < 2:
                message = "must supply a username with register"
            else:
                if user_id in GLOBAL_STORE:
                    message = "A user is already registered with this ID"
                else:
                    GLOBAL_STORE[user_id] = {
                        "username": parse[1],
                        "money": 100,
                        "hand": [],
                        "deck": Deck(),
                    }
                    message = "OK. I registered %s" % parse[1]
        elif command.startswith("bet"):
            # check if user exists
            if user_id not in GLOBAL_STORE:
                return "You are not registered"
            parse = command.split(" ")
            if len(parse) < 2:
                message = "must supply an amount to bet"
            else:
                try:
                    bet_amount = int(parse[1])
                except ValueError:
                    return "invalid bet amount"
                GLOBAL_STORE[user_id]["money"] += bet_amount
                message = "A :spades: J :heart: BlackJack! %s Wins! Total: %s" % (GLOBAL_STORE[user_id]["username"], GLOBAL_STORE[user_id]["money"])
        elif command.startswith("play"):
            game = GameService(GLOBAL_STORE[user_id])
            return game.play()
        elif command.startswith("stay"):
            pass
        return message
