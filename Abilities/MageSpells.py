from GameInterfacePOC.Abilities.Ability import Ability
from GameInterfacePOC.GameObjects.Characters.Character import Character

class MagicMissile(Ability):
    def __init__(self, player):
        super(MagicMissile, self).__init__(player)
        self.name = 'Magic Missile'
        self.range = 5
        self.max_level = 9
        self.cd_duration = 0
        self.level = 1
        self.mana_cost = 3

    def cast(self, target: Character):
        message = super(MagicMissile, self).cast()
        if message != None:
            return message
        message = ['Casting ' + self.name + '!']
        for i in range(self.level):
            message += ['did ' + str(i + 1) + ' damage']
            target.modify_health(-1*(i + 1))
        message += ['Target now has ' + str(target.health) + ' health!']
        for resource in self.player.resources:
            if resource.get_name() == 'Mana':
                resource.modify(-1*self.mana_cost)
        return message

    def can_cast(self):
        message = super(MagicMissile, self).can_cast()
        if message is None:
            for resource in self.player.resources:
                if resource.get_name() == 'Mana':
                    if not resource.check_can_cast(self.mana_cost):
                        message = ['Not enough Mana!']
                        break
        return message

    def requires_target(self):
        return True

class FireBall(Ability):
    def __init__(self, player):
        super(FireBall, self).__init__(player)
        self.name = 'Fire Ball'
        self.range = 4
        self.max_level = 9
        self.cd_duration = Character.gcd_duration * 5
        self.level = 1
        self.mana_cost = 5 + (self.level - 3)

    def cast(self, target: Character):
        message = super(FireBall, self).cast()
        if message != None:
            return message
        message = ['Casting ' + self.name + '!']
        message += ['did ' + str(5*(self.level)) + ' damage in a 3x3 grid']
        target.modify_health(-5*(self.level))
        message += ['Target now has ' + str(target.health) + ' health!']
        for resource in self.player.resources:
            if resource.get_name() == 'Mana':
                resource.modify(-1*self.mana_cost)
        return message

    def can_cast(self):
        message = super(FireBall, self).can_cast()
        if message is None:
            for resource in self.player.resources:
                if resource.get_name() == 'Mana':
                    if not resource.check_can_cast(self.mana_cost):
                        message = ['Not enough Mana!']
                        break
        return message

    def level_up(self):
        super(FireBall, self).level_up()
        self.mana_cost = 5 + (self.level - 3)

    def requires_target(self):
        return True
