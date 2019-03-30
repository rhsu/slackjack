from services.rebrand_service import RebrandService


def test_rebrand_no_username():
    service = RebrandService(5, None)
    assert service.rebrand() == "Must supply a username to rebrand"


def test_rebrand_no_user():
    service = RebrandService(5, "test")
    assert service.rebrand() == "Cannot rebrand. Not registered"


def test_rebrand_successful(global_store):
    global_store[5] = {
        "username": "test"
    }
    service = RebrandService(5, "new name")
    # TODO state bleed. investigate later
    assert service.rebrand() == "successfully rebranded to new name"
