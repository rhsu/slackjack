from services.roulette_queue_manager_service import RouletteQueueManangerService
from models.user_data import UserData


def test_user_wins_match_by_number(global_store, roulette_queue):
    user = UserData("user")
    user_id = "user"
    user.roulette_bet = "red"
    user.roulette_bet_amount = 10
    global_store[user_id] = user
    roulette_queue.append(user_id)
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine("red", 5)
    assert result == "*user* bet on *red*. *user* won. \n"
    assert user.money == 110


def test_user_wins_match_by_color(global_store, roulette_queue):
    user = UserData("user")
    user_id = "user"
    user.roulette_bet = 5
    user.roulette_bet_amount = 10
    global_store[user_id] = user
    roulette_queue.append(user_id)
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine("red", 5)
    assert result == "*user* bet on *5*. *user* won. \n"
    assert user.money == 110


def test_user_loses(global_store, roulette_queue):
    user = UserData("user")
    user_id = "user"
    user.roulette_bet = "red"
    user.roulette_bet_amount = 10
    global_store[user_id] = user
    roulette_queue.append(user_id)
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine("black", 2)
    assert result == "*user* bet on *red*. *user* lost. \n"
    assert user.money == 90
