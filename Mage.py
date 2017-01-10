import sys
from Player import Player

def magicMissile(player, level):
    for i in range(level):
        player.messages += [i]

class Mage(Player):

    abilities = []
    abilities += [magicMissile]

    def __init__(self):
        super(Mage, self).__init__()
        self.messages = []
        self.levels = [1 for x in xrange(len(Mage.abilities))]

    def update(self, game):
        super(Mage, self).update(game)
        if self.messages != []:
            game.writeMessage(self.messages)
            self.messages = []

    def levelUp(self):
        for i in range(len(self.levels)):
            self.levels[i] += 1

    def useAbility(self, index):
        Mage.abilities[index](self, self.levels[index])