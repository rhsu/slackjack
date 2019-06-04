from utils.color_util import determine_icon


class RouletteQueueManangerService():
    def __init__(self, global_store, roulette_queue):
        self.global_store = global_store
        self.roulette_queue = roulette_queue

    def determine(self, number, color):
        ret_val = [f"The result is {number} {determine_icon(color)}. \n"]
        for user_id in self.roulette_queue:
            curr_user = self.global_store[user_id]
            ret_val += self.determine_if_user_won(curr_user, number, color)
            # if curr_user.roulette_bet == color:
            #     curr_user.money += curr_user.roulette_bet_amount
            #     ret_val.append("*%s* bet on *%s*. *%s* won. \n" % (
            #         curr_user.username,
            #         determine_icon(curr_user.roulette_bet),
            #         curr_user.username
            #     ))
            # elif curr_user.roulette_bet == number:
            #     curr_user.money += curr_user.roulette_bet_amount
            #     ret_val.append("*%s* bet on *%s*. *%s* won. \n" % (
            #         curr_user.username,
            #         determine_icon(curr_user.roulette_bet),
            #         curr_user.username
            #     ))
            # else:
            #     curr_user.money -= curr_user.roulette_bet_amount
            #     ret_val.append("*%s* bet on *%s*. *%s* lost. \n" % (
            #         curr_user.username,
            #         determine_icon(curr_user.roulette_bet),
            #         curr_user.username
            #     ))
        del self.roulette_queue[:]
        return " ".join(ret_val)

    def determine_if_user_won(self, curr_user, number, color):
        # from pdb import set_trace; set_trace()
        ret_val = []
        for bet, bet_amount in curr_user.roulette_bet_v2:
            # from pdb import set_trace; set_trace()
            if (bet == number or bet == color):
                curr_user.money += bet_amount
                # TODO clear roulette_bet_v2
                ret_val.append("*%s* bet on *%s*. *%s* won. \n" % (
                    curr_user.username,
                    determine_icon(bet),
                    curr_user.username
                ))
            else:
                curr_user.money -= bet_amount
                # TODO clear roulette_bet_v2
                ret_val.append("*%s* bet on *%s*. *%s* lost. \n" % (
                    curr_user.username,
                    determine_icon(curr_user.roulette_bet),
                    curr_user.username
                ))
        return ret_val
