from utils.default_user_util import load_default_users


def test_load_default_users(global_store):
    load_default_users()
    assert global_store is not None
