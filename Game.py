import pygame

class Game():
    MAX_TICKS = 10.0
    width = 400
    height = 300
    gridSize = 20

    def __init__(self):
        self.screenDirty = True
        self.gameObjects = []
        self.bcg = None
        self.screen = pygame.display.set_mode((Game.width, Game.height))
    
    def addGameObject(self, obj):
        self.gameObjects += [obj]

    def setBackgroundImage(self, bcg):
        self.bcg = bcg

    def setDirty(self):
        self.isDirty = True

    def update(self):
        for obj in self.gameObjects:
            obj.update(self)
        return self

    def draw(self):
        if not self.screenDirty:
            return        
        self.screen.blit(self.bcg, (0, 0))
        for obj in self.gameObjects:
            obj.draw(self)
        self.isDirty = False
        return self