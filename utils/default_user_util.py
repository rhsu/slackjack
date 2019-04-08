from dotenv import load_dotenv
import os
from global_store import GLOBAL_STORE
from models.user_data import UserData


# TODO I think this should be a service
def load_default_users():
    load_dotenv()
    default_users = os.environ.get('DEFAULT_USERS')
    for user in default_users.split(','):
        user_id, username = user.split(':')
        GLOBAL_STORE[user_id.strip()] = UserData(username)
        # GLOBAL_STORE[user_id.strip()] = {
        #     # TODO this should be defineed in one place
        #     "username": username.strip(),
        #     "money": 100,
        #     "hand": [],
        #     "deck": Deck(),
        #     "dealer_hand": [],
        #     "bet": 0
        # }
