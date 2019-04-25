from services.rebuy_service import RebuyService

def test_sucessfully_rebought(default_user_data):
    default_user_data.money = 0
    service = RebuyService(default_user_data)
    assert service.rebuy() == "Rebuy successful. *someone* has 100 dollars"
    assert default_user_data.money == 100


def test_unsuccessfully_rebought(default_user_data):
    service = RebuyService(default_user_data)
    assert service.rebuy() == "Can't rebuy *someone* still has money"
    assert default_user_data.money > 0
