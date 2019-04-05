class RouletteQueueManangerService:
    def __init__(self, global_store, roulette_queue, number, color):
        self.global_store = global_store
        self.roulette_queue = roulette_queue
        self.number = number
        self.color = color

    def determine(self):
        for user_id in self.roulette_queue:
            bet = self.global_store[user_id]["bet"]
            if bet == self.color:
                pass
            elif bet == self.result:
                pass
            else:
                pass

