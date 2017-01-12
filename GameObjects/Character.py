import pygame
from Game import Game
from Grid import Grid

class Character(object):
    # in server ticks
    GCD_DURATION = 10.0
    MOVEMENT_DURATION = 10.0

    def __init__(self):
        self.gcdTick = 0
        self.messages = []
        self.faction = ''
        self.name = '?'
        self.canMove = True
        self.updateTick = 0
        self.color = None
        self.pos = (0 , 0)
        self.drawX = self.pos[0]
        self.drawY = self.pos[1]
        self.destinationPos = self.pos
        self.characterScreen = None
        
    def draw(self, game):
        game.screen.blit(self.characterScreen, (self.drawX*Game.gridSize, self.drawY*Game.gridSize))

    def move(self, x, y):
        if not self.canMove:
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
        self.canMove = False
        self.destinationPos = (newX, newY)

    def update(self, game):
        if self.destinationPos[0] != self.pos[0] or self.destinationPos[1] != self.pos[1]:
            game.setDirty()
            self.updateTick += 1
            self.drawX = self.pos[0] + ((self.destinationPos[0] - self.pos[0])*self.updateTick/Character.MOVEMENT_DURATION)
            self.drawY = self.pos[1] + ((self.destinationPos[1] - self.pos[1])*self.updateTick/Character.MOVEMENT_DURATION)
            if self.updateTick == Character.MOVEMENT_DURATION:
                self.updateTick = 0
                self.canMove = True
                self.pos = self.destinationPos
        if self.gcdTick > 0:
            self.gcdTick -= 1

    def setGcd(self):
        self.gcdTick = Character.GCD_DURATION

    def isHostile(self, other):
        return self.faction != other.faction