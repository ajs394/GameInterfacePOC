import random
import pygame
from GameInterfacePOC.GameObjects.Characters.Character import Character
from GameInterfacePOC.Game.Game import Game

class Enemy(Character):
    enemy_color = (92, 205, 92)
    enemy_names = ['Ralph', 'Jim Bob', 'Suzy Q', 'Loretta', 'Hanz', 'Franz', 'Potato',
                   'Potahto', 'Felicienne', 'Sonya Blyat']

    def __init__(self, game, pos):
        super(Enemy, self).__init__(game)
        self.faction = 'bad guys'
        self.color = Enemy.enemy_color
        self.pos = pos
        self.draw_x = self.pos[0]
        self.draw_y = self.pos[1]
        self.destination_pos = self.pos
        self.name = Enemy.enemy_names[random.randint(0, len(Enemy.enemy_names))]
        self.character_screen = pygame.Surface((Game.grid_size, Game.grid_size))
        pygame.draw.rect(self.character_screen, self.color,
                         pygame.Rect(0, 0, Game.grid_size, Game.grid_size))
