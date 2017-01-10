import pygame

class Game(object):
    MAX_TICKS = 10.0
    gridWidth = 400
    gridHeight = 300
    textWidth = 400
    textHeight = 300
    gridSize = 20

    def __init__(self):
        self.screenDirty = True
        self.gameObjects = []
        self.bcg = None
        self.tw = None
        self.screen = pygame.display.set_mode((max(Game.gridWidth, Game.textWidth), Game.gridHeight + Game.textHeight))
    
    def addGameObject(self, obj):
        self.gameObjects += [obj]

    def setBackgroundImage(self, bcg):
        self.bcg = bcg

    def setTextWindow(self, tw):
        self.tw = tw

    def setDirty(self):
        self.isDirty = True
    
    def writeMessage(self, message):
        self.tw.writeStrings(message)

    def update(self):
        for obj in self.gameObjects:
            obj.update(self)
        return self

    def draw(self):
        if not self.screenDirty:
            return        
        self.screen.blit(self.bcg, (0, 0))
        self.screen.blit(self.tw.textScreen, (0, Game.gridHeight))
        for obj in self.gameObjects:
            obj.draw(self)
        self.isDirty = False
        return self