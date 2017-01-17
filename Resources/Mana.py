from Resource import Resource

class Mana(Resource):

    def __init__(self):
        self.name = 'Mana'
        self.mana = 100.0
        self.max = 100
        self.recharge = .1

    def check_can_cast(self, cost):
        return cost <= self.mana

    def modify(self, change):
        self.mana += change
        self.mana = min(self.max, max(self.mana, 0))

    def update(self, character):
        self.modify(self.recharge)

    def get_name(self):
        return self.name

    def get_curr_percentage(self):
        return self.mana
