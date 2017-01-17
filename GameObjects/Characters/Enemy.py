import pygame
from GameInterfacePOC.GameObjects.Characters.Character import Character
from GameInterfacePOC.Game.Game import Game

class Enemy(Character):
    enemyColor = (92, 205, 92)

    def __init__(self, pos):
        super(Enemy, self).__init__()
        self.faction = 'bad guys'
        self.color = Enemy.enemyColor
        self.pos = pos
        self.draw_x = self.pos[0]
        self.draw_y = self.pos[1]
        self.destination_pos = self.pos
        self.character_screen = pygame.Surface((Game.grid_size, Game.grid_size))
        pygame.draw.rect(self.character_screen, self.color,
                         pygame.Rect(0, 0, Game.grid_size, Game.grid_size))
