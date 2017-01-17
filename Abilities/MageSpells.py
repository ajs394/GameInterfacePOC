from Ability import Ability
from GameInterfacePOC.GameObjects.Characters.Character import Character

class MagicMissile(Ability):
    def __init__(self, player):
        super(MagicMissile, self).__init__(player)
        self.name = 'Magic Missile'
        self.spell_range = 5
        self.max_level = 9
        self.cd_duration = 0
        self.level = 1

    def cast(self):
        message = super(MagicMissile, self).cast()
        if message != None:
            return message
        message = ['Casting ' + self.name + '!']
        for i in range(self.level):
            message += ['did ' + str(i + 1) + ' damage']
        self.player.set_gcd()
        return message

class FireBall(Ability):
    def __init__(self, player):
        super(FireBall, self).__init__(player)
        self.name = 'Fire Ball'
        self.spell_range = 4
        self.max_level = 9
        self.cd_duration = Character.gcd_duration * 5
        self.level = 1

    def cast(self):
        message = super(FireBall, self).cast()
        if message != None:
            return message
        message = ['Casting ' + self.name + '!']
        message += ['did ' + str(5*(self.level)) + ' damage in a 3x3 grid']
        self.player.set_gcd()
        return message
