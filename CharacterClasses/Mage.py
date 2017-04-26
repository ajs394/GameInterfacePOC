from GameInterfacePOC.Game import Game
from GameInterfacePOC.GameObjects.Characters.Player import Player
from GameInterfacePOC.Abilities import MageSpells
from GameInterfacePOC.Resources.Mana import Mana

class Mage(Player):
    def __init__(self, game: Game):
        super(Mage, self).__init__(game)
        self.name = 'Mage'
        self.abilities = [MageSpells.MagicMissile(self), MageSpells.FireBall(self)]
        self.resources = [Mana()]

    def use_ability(self, index):
        if self.gcd_tick > 0:
            self.messages += ['GCD not cleared']
            return
        if index >= len(self.abilities):
            self.messages += ['Ability key not bound']
            return
        if not self.resources[0].check_can_cast(self.abilities[index].mana_cost):
            self.messages += ['Not enough Mana']
            return
        cast_return = self.game.cast(lambda: self.abilities[index].cast(self.target),
                                     self.abilities[index], self, self.target)
        if cast_return != None:
            for message in cast_return:
                self.messages += [message]
