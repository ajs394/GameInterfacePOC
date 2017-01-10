import sys
from Player import Player

def magicMissile(player, level):
    for i in range(level):
        player.messages += ['did ' + str(i + 1) + ' damage']
        
def fireBall(player, level):
    player.messages += ['did ' + str(5*(level)) + ' damage in a 3x3 grid']

class Mage(Player):

    abilities = [magicMissile, fireBall]
    abilityNames = ['Magic Missile', 'Fire Ball']

    def __init__(self):
        super(Mage, self).__init__()
        self.messages = []
        self.levels = [1 for x in xrange(len(Mage.abilities))]

    def update(self, game):
        super(Mage, self).update(game)
        if self.messages != []:
            game.writeMessage(self.messages)
            self.messages = []

    def levelUp(self, i):
        self.messages += ['Leveling Up ' + Mage.abilityNames[i] + '!']
        self.levels[i] += 1

    def useAbility(self, index):
        if index >= len(Mage.abilities):
            self.messages += ['Ability key not bound']
            return
        self.messages += ['Casting ' + Mage.abilityNames[index] + '!']
        Mage.abilities[index](self, self.levels[index])