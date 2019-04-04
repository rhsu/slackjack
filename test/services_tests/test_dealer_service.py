from services.dealer_service import DealerService
from utils.hand_util import hand_sum


def dealer_service_deals_a_dealer_hand(default_user_data):
    DealerService(default_user_data)
    assert len(default_user_data["dealer_hand"]) == 2


def test_play(default_user_data):
    service = DealerService(default_user_data)
    result = service.play()
    assert hand_sum(result) > 16
