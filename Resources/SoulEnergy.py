from Resource import Resource

class SoulEnergy(Resource):

    def __init__(self):
        self.name = 'Soul Energy'
        self.energy = 0.0
        self.max = 100.0
        self.delay = 15
        self.last_update = 0

    def check_can_cast(self, cost):
        return cost <= self.energy

    def modify(self, change):
        self.energy += change
        self.energy = min(self.max, max(self.energy, 0))
        self.last_update = 0

    def update(self, character):
        #do nothing
        return

    def get_name(self):
        return self.name

    def get_curr_percentage(self):
        return self.energy
