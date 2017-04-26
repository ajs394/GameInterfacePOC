from GameInterfacePOC.GameObjects.Characters.Player import Player
from GameInterfacePOC.Resources.Mana import Mana
from GameInterfacePOC.Resources.SoulEnergy import SoulEnergy

class SoulTaker(Player):
    def __init__(self, game):
        super(SoulTaker, self).__init__(game)
        from GameInterfacePOC.Abilities import SoulTakerSpells
        self.name = 'Soul Taker'
        self.abilities = [SoulTakerSpells.SoulRend(self), SoulTakerSpells.LifeTap(self)]
        self.resources = [Mana(), SoulEnergy()]

    def use_ability(self, index):
        if self.gcd_tick > 0:
            self.messages += ['GCD not cleared']
            return
        if index >= len(self.abilities):
            self.messages += ['Ability key not bound']
            return
        cast_return = self.game.cast(lambda: self.abilities[index].cast(self.target),
                                     self.abilities[index], self, self.target)
        if cast_return != None:
            for message in cast_return:
                self.messages += [message]

    def add_soul_energy(self, amount=.1):
        self.resources[1].modify(amount)
