from global_store import GLOBAL_STORE
from models.deck import Deck
from services.game_service import GameService
from services.dealer_service import DealerService
from utils.hand_util import hand_sum


class GameController:
    def __init__(self, user_id):
        self.user_id = user_id
        # TODO maybe make a different controller for registering?
        if user_id in GLOBAL_STORE:
            self.game_service = GameService(GLOBAL_STORE[user_id])
            self.dealer_service = DealerService(GLOBAL_STORE[user_id])
            self.dealer_service.init_dealer()

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
                    # TODO refactor this
                    GLOBAL_STORE[user_id] = {
                        "username": parse[1],
                        "money": 100,
                        "hand": [],
                        "deck": Deck(),
                        "dealer_hand": []
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
        elif command.startswith("hit"):
            return self.game_service.play()
        elif command.startswith("stay"):
            dealer_hand = self.dealer_service.play()
            dealer_sum = hand_sum(dealer_hand)
            players_hand = GLOBAL_STORE[user_id]["hand"]
            player_sum = hand_sum(players_hand)
            # TODO what happens if both players get 21? for now Im giving it 
            # to the player
            if hand_sum(dealer_hand) > 21:
                return "Dealer busted. You win!"
            elif player_sum > dealer_sum:
                return "You win"
            else:
                return "You lose"
        return message
