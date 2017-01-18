import pygame
from GameInterfacePOC.GameObjects.Characters.Character import Character
from GameInterfacePOC.Game.Game import Game

class Player(Character):
    target_bracket_color = (255, 50, 50)

    abilities = []
    abilityNames = []

    def __init__(self, game):
        super(Player, self).__init__(game)
        self.target_tick = 0
        self.abilities = []
        self.resources = []
        self.faction = 'good guys'
        self.color = (100, 149, 237)
        self.pos = (0, 0)
        self.draw_x = self.pos[0]
        self.draw_y = self.pos[1]
        self.destination_pos = self.pos
        self.character_screen = pygame.Surface((Game.grid_size, Game.grid_size))
        pygame.draw.rect(self.character_screen, self.color,
                         pygame.Rect(0, 0, Game.grid_size, Game.grid_size))
        self.target = None

    def draw(self):
        self.game.screen.blit(self.character_screen,
                              (self.draw_x*Game.grid_size, self.draw_y*Game.grid_size))
        if self.target != None:
            pixel_offset = -6+(abs(12-self.target_tick))
            target_width = 2
            position_offset = (abs(12-self.target_tick)/2) + 6 + target_width/2
            player_target_screen = pygame.Surface((Game.grid_size + pixel_offset,
                                                   Game.grid_size + pixel_offset))
            pygame.draw.rect(player_target_screen, Player.target_bracket_color,
                             pygame.Rect(player_target_screen.get_width()/2-position_offset,
                                         player_target_screen.get_height()/2-position_offset,
                                         player_target_screen.get_width(),
                                         player_target_screen.get_height()),
                             target_width)
            self.game.screen.blit(player_target_screen,
                                  ((self.target.draw_x + 1.0/2)*Game.grid_size - position_offset,
                                  (self.target.draw_y + 1.0/2)*Game.grid_size - position_offset))
            self.target_tick = (self.target_tick + 1)%24

    def update(self):
        for ability in self.abilities:
            ability.update()
        for resource in self.resources:
            resource.update(self)
        super(Player, self).update()

    def level_up(self, i):
        self.messages += ['Leveling Up ' + self.abilities[i].name + '!']
        self.abilities[i].level_up()

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
        '''
        # code block for checking resource management over multiple resources
        for resource in self.resources:
            self.messages += [resource.get_name() + ' currently at ' +
                              str(resource.get_curr_percentage()) + ' percent']
        '''

    def get_max_range(self):
        max_range = 0
        for spell in self.abilities:
            max_range = max(max_range, spell.range)
        return max_range

    def tab_target(self):
        self.target = self.game.get_closest_enemy(self, self.get_max_range())
        self.target_tick = 0
