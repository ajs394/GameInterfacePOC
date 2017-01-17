from Resource import Resource

class Rage(Resource):

    def __init__(self):
        self.name = 'Rage'
        self.rage = 0
        self.max = 100
        self.degen = -.5
        self.delay = 15
        self.last_update = 0

    def check_can_cast(self, cost):
        return cost <= self.rage

    def modify(self, change):
        self.rage += change
        self.rage = min(self.max, max(self.rage, 0))
        self.last_update = 0

    def update(self, character):
        self.last_update += 1
        if self.last_update > self.delay:
            self.modify(self.degen)

    def get_name(self):
        return self.name

    def get_curr_percentage(self):
        return self.rage
