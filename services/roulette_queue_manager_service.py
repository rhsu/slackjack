class RouletteQueueManangerService():
    def __init__(self, global_store, roulette_queue):
        self.global_store = global_store
        self.roulette_queue = roulette_queue

    def determine(self, number, color):
        ret_val = [f"The result is {number} {color}. \n"]
        for user_id in self.roulette_queue:
            curr_user = self.global_store[user_id]
            if curr_user.roulette_bet == color:
                curr_user.money += curr_user.roulette_bet_amount
                ret_val.append("*%s* bet on *%s*. *%s* won. \n" % (
                    curr_user.username,
                    curr_user.roulette_bet,
                    curr_user.username
                ))
            elif curr_user.roulette_bet == number:
                curr_user.money += curr_user.roulette_bet_amount
                ret_val.append("*%s* bet on *%s*. *%s* won. \n" % (
                    curr_user.username,
                    curr_user.roulette_bet,
                    curr_user.username
                ))
            else:
                curr_user.money -= curr_user.roulette_bet_amount
                ret_val.append("*%s* bet on *%s*. *%s* lost. \n" % (
                    curr_user.username,
                    curr_user.roulette_bet,
                    curr_user.username
                ))
        del self.roulette_queue[:]
        return " ".join(ret_val)
