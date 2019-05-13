class RouletteQueueManangerService():
    def __init__(self, color, global_store, number, roulette_queue):
        self.color = color
        self.global_store = global_store
        self.number = number
        self.roulette_queue = roulette_queue

    def determine(self):
        for user_id in self.roulette_queue:
            curr_user = self.global_store[user_id]


    # def __init__(self, global_store, roulette_queue, number, color):
    #     self.global_store = global_store
    #     self.roulette_queue = roulette_queue
    #     self.number = number
    #     self.color = color

    # def determine(self):
    #     for user_id in self.roulette_queue:
    #         bet = self.global_store[user_id]["bet"]
    #         if bet == self.color:
    #             pass
    #         elif bet == self.result:
    #             pass
    #         else:
    #             pass

# result, color = self.roulette_service.spin()
#             ret_val = f"the result is *{result}* (*{color}*) \n"
#             for user_id in ROULETE_QUEUE:
#                 curr_user = GLOBAL_STORE[user_id]
#                 if curr_user.roulette_bet == color:
#                     curr_user.money += curr_user.roulette_bet_amount
#                     ret_val += "*%s* bet on *%s*. *%s* won \n" % (
#                         curr_user.username,
#                         curr_user.roulette_bet,
#                         curr_user.username)
#                 elif curr_user.roulette_bet == result:
#                     curr_user.money += curr_user.roulette_bet_amount
#                     ret_val += "*%s* bet on *%s*. *%s* won. \n" % (
#                         curr_user.username,
#                         curr_user.roulette_bet,
#                         curr_user.username)
#                 else:
#                     curr_user.money -= curr_user.roulette_bet_amount
#                     ret_val += "*%s* bet on *%s*. *%s* lost. \n" % (
#                         curr_user.username,
#                         curr_user.roulette_bet,
#                         curr_user.username)
#             del ROULETE_QUEUE[:]
