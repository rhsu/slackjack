from services.dealer_service import DealerService


def test_init_dealer(default_user_data):
    service = DealerService(default_user_data)
    service.init_dealer()
    assert len(default_user_data["dealer_hand"]) == 2
