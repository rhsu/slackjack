from services.rebrand_service import RebrandService


def test_rebrand_no_username():
    service = RebrandService(5, None)
    assert service.rebrand() == "Must supply a username to rebrand"


def test_rebrand_no_user():
    service = RebrandService(5, "test")
    assert service.rebrand() == "Cannot rebrand. Not registered"


def test_rebrand_successful(default_id, default_user_data):
    service = RebrandService(default_id, "new name")
    assert service.rebrand() == "successfully rebranded to new name"
