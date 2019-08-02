from services.roulette_queue_manager_service import RouletteQueueManangerService
from models.user_data import UserData


def test_user_wins_match_by_number(global_store, roulette_queue):
    # build a user
    user = UserData("user")
    user_id = "user"
    user.roulette_bet = [(5, 10)]

    # put user into data structures
    global_store[user_id] = user
    roulette_queue.add(user_id)

    # run test
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine(5, "red")
    assert result == "The result is 5 :red_circle:. \n *user* bet on *5*. *user* won. \n"
    assert user.money == 450
    assert len(roulette_queue) == 0


def test_user_wins_match_by_color(global_store, roulette_queue):
    # build a user
    user = UserData("user")
    user_id = "user"
    # TODO: for consistency. I would like the thing to be (string, int)
    user.roulette_bet = [("red", 10)]

    global_store[user_id] = user
    roulette_queue.add(user_id)

    # run test
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine(5, "red")
    assert result == "The result is 5 :red_circle:. \n *user* bet on *:red_circle:*. *user* won. \n"
    assert user.money == 110
    assert len(roulette_queue) == 0


def test_user_loses(global_store, roulette_queue):
    # build a user
    user = UserData("user")
    user_id = "user"
    user.roulette_bet = [("red", 10)]

    # put user into data structures
    global_store[user_id] = user
    roulette_queue.add(user_id)

    # run test
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine(2, "black")
    assert result == "The result is 2 :black_circle:. \n *user* bet on *:red_circle:*. *user* lost. \n"
    assert user.money == 90
    assert len(roulette_queue) == 0


def test_two_users_winer_and_loser(global_store, roulette_queue):
    # build a winner
    winner = UserData("winner")
    winner_id = "winner"
    winner.roulette_bet = [("red", 10)]

    # build a loser
    loser = UserData("loser")
    loser_id = "loser"
    loser.roulette_bet = [("black", 10)]

    # put user into data structures
    global_store[winner_id] = winner
    global_store[loser_id] = loser
    roulette_queue.add(winner_id)
    roulette_queue.add(loser_id)

    # run test
    service = RouletteQueueManangerService(global_store, roulette_queue)
    result = service.determine(2, "red")
    assert "The result is 2 :red_circle:. \n" in result
    assert "*loser* bet on *:black_circle:*. *loser* lost. \n" in result
    assert "*winner* bet on *:red_circle:*. *winner* won. \n" in result
    assert winner.money == 110
    assert loser.money == 90
    assert len(roulette_queue) == 0

# TODO test 3d betting
