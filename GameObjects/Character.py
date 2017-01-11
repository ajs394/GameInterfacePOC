import pygame
from Game import Game
from Grid import Grid

class Character(object):

    def __init__(self):
        self.messages = []
        self.faction = ''
        self.name = '?'
        self.isIdle = True
        self.updateTick = 0
        self.color = None
        self.pos = (0 , 0)
        self.drawX = self.pos[0]
        self.drawY = self.pos[1]
        self.destinationPos = self.pos
        # each inheriting class should overwrite the bottom two lines of code
        # we might remove these entirely
        
    def draw(self, game):
        game.screen.blit(self.characterScreen, (self.drawX*Game.gridSize, self.drawY*Game.gridSize))

    def move(self, x, y):
        if not self.isIdle:
            return
        newX = self.pos[0] + x
        newY = self.pos[1] + y
        if newX < 0:
            newX = 0
        if newX >= Game.gridMaxX:
            newX = Game.gridMaxX - 1
        if newY < 0:
            newY = 0
        if newY >= Game.gridMaxY:
            newY = Game.gridMaxY - 1
        if newX == self.pos[0] and newY == self.pos[1]:
            return
        self.isIdle = False
        self.destinationPos = (newX, newY)

    def update(self, game):
        if self.isIdle:
            return
        if self.destinationPos[0] != self.pos[0] or self.destinationPos[1] != self.pos[1]:
            game.setDirty()
            self.updateTick += 1
            self.drawX = self.pos[0] + ((self.destinationPos[0] - self.pos[0])*self.updateTick/Game.MAX_TICKS)
            self.drawY = self.pos[1] + ((self.destinationPos[1] - self.pos[1])*self.updateTick/Game.MAX_TICKS)
            if self.updateTick == Game.MAX_TICKS:
                self.updateTick = 0
                self.isIdle = True
                self.pos = self.destinationPos

    def isHostile(self, other):
        return self.faction != other.faction