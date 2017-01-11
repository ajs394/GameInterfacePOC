import pygame
from Character import Character
from Game import Game
from Grid import Grid

class Enemy(Character):
    enemyColor = (92, 205, 92)

    def __init__(self, pos):
        super(Enemy, self).__init__()
        self.faction = 'bad guys'
        self.color = Enemy.enemyColor
        self.pos = pos
        self.drawX = self.pos[0]
        self.drawY = self.pos[1]
        self.destinationPos = self.pos
        self.characterScreen = pygame.Surface((Game.gridSize, Game.gridSize))
        pygame.draw.rect(self.characterScreen, self.color, pygame.Rect(0, 0, Game.gridSize, Game.gridSize))