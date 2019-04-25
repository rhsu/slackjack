from services.service import Service

class RebuyService(Service):
    def __init__(self, userdata):
        Service.__init__(self, userdata)

    def rebuy(self):
        from pdb import set_trace; set_trace();
        if self.money() == 0:
            self.money
            return f"{self.username()} successfully rebought"
        else:
            return f"Can't rebuy {self.username()} still has money"
