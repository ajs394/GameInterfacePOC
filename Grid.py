import pygame
from Game import Game

class Grid():
    gridMaxX = Game.width/Game.gridSize
    gridMaxY = Game.height/Game.gridSize
    gridColor = (255, 255, 255)
    
    grid = [[] for x in xrange(gridMaxX)]
    
    def __init__(self):
        self.gridScreen = pygame.Surface((Game.width, Game.height))
        for i in range(0, Game.width, Game.gridSize):
            for j in range(0, Game.height, Game.gridSize):
                pygame.draw.rect(self.gridScreen, Grid.gridColor, pygame.Rect(i, j, 20, 20), 1)
    