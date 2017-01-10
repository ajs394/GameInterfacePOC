import sys
from Player import Player

def magicMissile(level):
    for i in range(level):
        sys.stdout.write(level)
        sys.stdout.flush()

class Mage(Player):

    abilities = []
    abilities += [magicMissile]

    def __init__(self):
        super(Mage, self).__init__()
        self.levels = [1 for x in xrange(len(Mage.abilities))]

    def levelUp(self):
        for i in range(len(self.levels)):
            self.levels[i] += 1

    def useAbility(self, index):
        Mage.abilities[index](self.levels[index])