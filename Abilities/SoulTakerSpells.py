from Ability import Ability
from GameInterfacePOC.Persistence.PlayerEffect import PlayerEffect
from GameInterfacePOC.GameObjects.Characters.Character import Character

class SoulTakerSpell(Ability):
    def __init__(self, player):
        super(SoulTakerSpell, self).__init__(player)
        self.mana_cost = 0
        self.soul_cost = 0

    def cast(self, target):
        message = super(SoulTakerSpell, self).cast()
        if message != None:
            return message
        for resource in self.player.resources:
            if resource.get_name() == 'Mana':
                resource.modify(-1*self.mana_cost)        
        for resource in self.player.resources:
            if resource.get_name() == 'Soul Energy':
                resource.modify(-1*self.soul_cost)

    def can_cast(self):
        message = super(SoulTakerSpell, self).can_cast()
        if message is None:
            for resource in self.player.resources:
                if resource.get_name() == 'Soul Energy':
                    if not resource.check_can_cast(self.soul_cost):
                        message = ['Not enough Souls!']
                        break
                if resource.get_name() == 'Mana':
                    if not resource.check_can_cast(self.soul_cost):
                        message = ['Not enough Mana!']
                        break
        return message

class LifeTap(SoulTakerSpell):
    def __init__(self, player):
        super(LifeTap, self).__init__(player)
        self.name = 'Life Tap'
        self.mana_cost = 20
        self.soul_cost = 0

    def cast(self, target):
        message = super(LifeTap, self).cast(target)
        if message is not None:
            return message
        message = ['Casting ' + self.name + '!']
        self.player.modify_health(-20)
        message += ['I now have ' + str(self.player.health) + ' health!']
        self.player.add_soul_energy(200)
        return message

class SoulRend(SoulTakerSpell):
    def __init__(self, player):
        super(SoulRend, self).__init__(player)
        self.name = 'Soul Rend'
        self.mana_cost = 0
        self.soul_cost = 10
        self.range = 8

    def cast(self, target):
        message = super(SoulRend, self).cast(target)
        if message is not None:
            return message
        message = ['Casting ' + self.name + '!']
        # do whatever this specific ability does

        # do 10 damage, applying a debuff
        target.modify_health(-10)
        message += ['Target now has ' + str(target.health) + ' health!']
        target.add_effect(SoulRendDot(self.player))
        return message

    def requires_target(self):
        return True

class SoulRendDot(PlayerEffect):
    def __init__(self, caster):
        super(SoulRendDot, self).__init__()
        self.caster = caster
        self.name = 'Soul Rend'
        self.remaining_duration = 100
        self.max_duration = 100
        self.count = 1

    def update(self, player):
        self.remaining_duration -= 1
        # route A: assume that 'player' is a soultaker
        self.caster.add_soul_energy()

        # route B: write a generic method.  Seems unnecessary
