from global_store import GLOBAL_STORE
from models.deck import Deck


class RegisterService:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def register(self):
        if self.user_id in GLOBAL_STORE:
            return "A user is already registered with this ID"
        else:
            # TODO refactor this
            GLOBAL_STORE[self.user_id] = {
                "username": self.user_name,
                "money": 100,
                "hand": [],
                "deck": Deck(),
                "dealer_hand": [],
                "bet": 0,
            }
            return "OK. I registered %s" % self.user_name
