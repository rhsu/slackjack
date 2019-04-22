from global_store import GLOBAL_STORE
from models.user_data import UserData


class RegisterService:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def register(self):
        if self.user_id in GLOBAL_STORE:
            return "A user is already registered with this ID"
        else:
            GLOBAL_STORE[self.user_id] = UserData(self.user_name)
            return f"OK. I registered {self.user_name}"
