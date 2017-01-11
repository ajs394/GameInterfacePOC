import sys
from Player import Player
import MageSpells

class Mage(Player):

    abilities = [MageSpells.MagicMissile, MageSpells.FireBall]

    def __init__(self):
        super(Mage, self).__init__()
        self.levels = [1 for x in xrange(len(Mage.abilities))]

    def update(self, game):
        super(Mage, self).update(game)
        if self.messages != []:
            game.writeMessage(self.messages)
            self.messages = []