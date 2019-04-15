from global_store import GLOBAL_STORE


class RebrandService:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def rebrand(self):
        if not self.username:
            return "Must supply a username to rebrand"

        if self.user_id not in GLOBAL_STORE:
            return "Cannot rebrand. Not registered"

        user_data = GLOBAL_STORE[self.user_id]
        user_data.username = self.username
        return f"successfully rebranded to {self.username}"
