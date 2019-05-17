from services.roulette_queue_manager_service import RouletteQueueManangerService
from models.user_data import UserData


def test_user_wins_match_by_number(global_store, roulette_queue):
    # build a user
    user = UserData("user")
    user_id = "user"
    user.roulette_bet = "red"
    user.roulette_bet_amount = 10

    # put user into data structures
    global_store[user_id] = user
    roulette_queue.append(user_id)

    # run test
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine("red", 5)
    assert result == "*user* bet on *red*. *user* won. \n"
    assert user.money == 110
    assert len(roulette_queue) == 0


def test_user_wins_match_by_color(global_store, roulette_queue):
    # build a user
    user = UserData("user")
    user_id = "user"
    user.roulette_bet = 5
    user.roulette_bet_amount = 10

    # put user into data structures
    global_store[user_id] = user
    roulette_queue.append(user_id)

    # run test
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine("red", 5)
    assert result == "*user* bet on *5*. *user* won. \n"
    assert user.money == 110
    assert len(roulette_queue) == 0


def test_user_loses(global_store, roulette_queue):
    # build a user
    user = UserData("user")
    user_id = "user"
    user.roulette_bet = "red"
    user.roulette_bet_amount = 10

    # put user into data structures
    global_store[user_id] = user
    roulette_queue.append(user_id)

    # run test
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine("black", 2)
    assert result == "*user* bet on *red*. *user* lost. \n"
    assert user.money == 90
    assert len(roulette_queue) == 0


def test_two_users_winer_and_loser(global_store, roulette_queue):
    # build a winner
    winner = UserData("winner")
    winner_id = "winner"
    winner.roulette_bet = "red"
    winner.roulette_bet_amount = 10

    # build a loser
    loser = UserData("loser")
    loser_id = "loser"
    loser.roulette_bet = "black"
    loser.roulette_bet_amount = 10

    # put user into data structures
    global_store[winner_id] = winner
    global_store[loser_id] = loser
    roulette_queue.append(winner_id)
    roulette_queue.append(loser_id)

    # run test
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine("red", 2)
    assert result == "*winner* bet on *red*. *winner* won. \n *loser* bet on *black*. *loser* lost. \n"
    assert winner.money == 110
    assert loser.money == 90
    assert len(roulette_queue) == 0
