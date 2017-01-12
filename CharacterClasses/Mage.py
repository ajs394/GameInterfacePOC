import sys
from Player import Player
import MageSpells

class Mage(Player):
    def __init__(self):
        super(Mage, self).__init__()
        self.abilities = [MageSpells.MagicMissile(self), MageSpells.FireBall(self)]