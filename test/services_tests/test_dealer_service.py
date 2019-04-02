from services.dealer_service import DealerService
from utils.hand_util import hand_sum


# def test_init_dealer(default_user_data):
#     service = DealerService(default_user_data)
#     service.init_dealer()
#     assert len(default_user_data["dealer_hand"]) == 2


# def test_play(default_user_data):
#     service = DealerService(default_user_data)
#     service.init_dealer()
#     result = service.play()
#     assert hand_sum(result) > 16
