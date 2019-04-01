from dotenv import load_dotenv
import os
from global_store import GLOBAL_STORE
from models.deck import Deck


def load_default_users():
    load_dotenv()
    default_users = os.environ.get('DEFAULT_USERS')
    for user in default_users.split(','):
        user_id, username = user.split(':')
        GLOBAL_STORE[user_id.strip()] = {
            "username": username.strip(),
            "money": 100,
            "hand": [],
            "deck": Deck(),
            "dealer_hand": []
        }