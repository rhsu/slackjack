from services.service import Service


class RebuyService(Service):
    def __init__(self, userdata):
        Service.__init__(self, userdata)

    def rebuy(self):
        if self.money() == 0:
            self.set_money(100)
            return f"Rebuy successful. *{self.username()}* has 100 dollars"
        else:
            return f"Can't rebuy *{self.username()}* still has money"
