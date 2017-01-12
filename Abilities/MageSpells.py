from Ability import Ability
from Character import Character

class MagicMissile(Ability):
    def __init__(self, player):
        super(MagicMissile, self).__init__(player)
        self.name = 'Magic Missile'
        self.spellRange = 5
        self.maxLevel = 9
        self.CD_DURATION = 0
        self.level = 1

    def cast(self):
        message = super(MagicMissile, self).cast()
        if message != None:
            return message
        message = ['Casting ' + self.name + '!']
        for i in range(self.level):
            message += ['did ' + str(i + 1) + ' damage']
        self.player.setGcd()
        return message

class FireBall(Ability):
    def __init__(self, player):
        super(FireBall, self).__init__(player)
        self.name = 'Fire Ball'
        self.spellRange = 4
        self.maxLevel = 9
        self.CD_DURATION = Character.GCD_DURATION * 5
        self.level = 1

    def cast(self):
        message = super(FireBall, self).cast()
        if message != None:
            return message
        message = ['Casting ' + self.name + '!']
        message += ['did ' + str(5*(self.level)) + ' damage in a 3x3 grid']
        self.player.setGcd()
        return message
