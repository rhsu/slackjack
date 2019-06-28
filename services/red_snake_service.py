from services.service import Service

RED_SNAKE_NUMBERS = [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]

class RedSnakeService(Service):

    def __init__(self, userdata, roulette_service):
        Service.__init__(self, userdata)
        self.roulette_service = roulette_service

    def play(self):
        number, color = self.roulette_service.spin()
        if color != "red":
            return f"you lost"
        elif number in RED_SNAKE_NUMBERS:
            return f"you won"

