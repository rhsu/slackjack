from services.register_service import RegisterService


def test_register_already_exists(global_store):
    global_store[5] = {}
    result = RegisterService(5, "somename").register()
    assert result == "A user is already registered with this ID"


def test_register_works(global_store):
    result = RegisterService(5, "somename").register()
    assert result == "OK. I registered somename"
    assert global_store[5].username == "somename"
