import pygame
from Game import Game
from Grid import Grid

class Player():
    newPlayerInitialPos = [(0, 0),(Grid.gridMaxX - 1, 0),(Grid.gridMaxX - 1, Grid.gridMaxY - 1),(0, Grid.gridMaxY - 1)]
    newPlayerInitialPosInc = 0
    newPlayerColors = [(100, 149, 237), (50, 205, 50), (205, 92, 92), (147, 112, 219)]
    newPlayerColorsInc = 0

    def __init__(self):
        self.isIdle = True
        self.updateTick = 0
        self.color = Player.newPlayerColors[Player.newPlayerColorsInc]
        Player.newPlayerColorsInc = (Player.newPlayerColorsInc + 1) % 4
        self.pos = Player.newPlayerInitialPos[Player.newPlayerInitialPosInc]
        self.drawX = self.pos[0]
        self.drawY = self.pos[1]
        self.destinationPos = self.pos
        Player.newPlayerInitialPosInc = (Player.newPlayerInitialPosInc + 1) % 4
        self.playerScreen = pygame.Surface((Game.gridSize, Game.gridSize))
        pygame.draw.rect(self.playerScreen, self.color, pygame.Rect(0, 0, Game.gridSize, Game.gridSize))
        
    def draw(self, game):
        game.screen.blit(self.playerScreen, (self.drawX*Game.gridSize, self.drawY*Game.gridSize))

    def move(self, x, y):
        if not self.isIdle:
            return
        newX = self.pos[0] + x
        newY = self.pos[1] + y
        if newX < 0:
            newX = 0
        if newX >= Grid.gridMaxX:
            newX = Grid.gridMaxX - 1
        if newY < 0:
            newY = 0
        if newY >= Grid.gridMaxY:
            newY = Grid.gridMaxY - 1
        if newX == self.pos[0] and newY == self.pos[1]:
            return
        print 'Moving: x ->',x,'y ->',y
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