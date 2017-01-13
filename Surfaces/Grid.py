import pygame
from GameInterfacePOC.Game.Game import Game

class Grid(object):
    gridColor = (255, 255, 255)

    def __init__(self):
        self.grid_screen = pygame.Surface((Game.grid_width, Game.grid_height))
        for i in range(0, Game.grid_width, Game.grid_size):
            for j in range(0, Game.grid_height, Game.grid_size):
                pygame.draw.rect(self.grid_screen, Grid.gridColor, pygame.Rect(i, j, 20, 20), 1)
    