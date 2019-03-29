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

        GLOBAL_STORE[self.user_id]["username"] = self.username
        return "successfully rebranded to %s" % self.username
