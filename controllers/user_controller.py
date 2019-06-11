from global_store import GLOBAL_STORE
from services.register_service import RegisterService
from services. rebrand_service import RebrandService


class UserController:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def register(self):
        if not self._check_user_exists():
            return "A user is already registered with this ID"
        return RegisterService(self.user_id, self.username).register()

    def rebrand(self):
        if not self._check_user_exists():
            return "A user is already registered with this ID"
        return RebrandService(self.user_id, self.username).rebrand()

    def _check_user_exists(self):
        return self.user_id in GLOBAL_STORE
