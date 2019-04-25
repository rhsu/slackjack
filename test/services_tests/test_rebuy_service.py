from services.rebuy_service import RebuyService

def test_sucessfully_rebought(default_user_data):
    default_user_data.money = 0
    # from pdb import set_trace; set_trace()
    service = RebuyService(default_user_data)
    assert service.rebuy() == "someone successfully rebought"
    # from pdb import set_trace; set_trace()
    assert default_user_data.money == 100
