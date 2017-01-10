import pygame
from Game import Game

class Grid(object):
    gridMaxX = Game.gridWidth/Game.gridSize
    gridMaxY = Game.gridHeight/Game.gridSize
    gridColor = (255, 255, 255)
    
    grid = [[] for x in xrange(gridMaxX)]
    
    def __init__(self):
        self.gridScreen = pygame.Surface((Game.gridWidth, Game.gridHeight))
        for i in range(0, Game.gridWidth, Game.gridSize):
            for j in range(0, Game.gridHeight, Game.gridSize):
                pygame.draw.rect(self.gridScreen, Grid.gridColor, pygame.Rect(i, j, 20, 20), 1)
    