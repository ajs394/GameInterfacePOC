import pygame
from Character import Character
from Game import Game
from Grid import Grid

class Player(Character):
    newPlayerInitialPos = [(0, 0),(Game.gridMaxX - 1, 0),(Game.gridMaxX - 1, Game.gridMaxY - 1),(0, Game.gridMaxY - 1)]
    newPlayerInitialPosInc = 0
    newPlayerColors = [(100, 149, 237), (50, 205, 50), (205, 92, 92), (147, 112, 219)]
    newPlayerColorsInc = 0
    targetBracketColor = (255, 50, 50)
    
    abilities = []
    abilityNames = []

    def __init__(self):
        self.targetTick = 0
        self.messages = []
        self.levels = []
        self.faction = 'good guys'
        self.isIdle = True
        self.updateTick = 0
        self.color = Player.newPlayerColors[Player.newPlayerColorsInc]
        Player.newPlayerColorsInc = (Player.newPlayerColorsInc + 1) % 4
        self.pos = Player.newPlayerInitialPos[Player.newPlayerInitialPosInc]
        self.drawX = self.pos[0]
        self.drawY = self.pos[1]
        self.destinationPos = self.pos
        Player.newPlayerInitialPosInc = (Player.newPlayerInitialPosInc + 1) % 4
        self.characterScreen = pygame.Surface((Game.gridSize, Game.gridSize))
        pygame.draw.rect(self.characterScreen, self.color, pygame.Rect(0, 0, Game.gridSize, Game.gridSize))
        self.target = None
        
    def draw(self, game):
        game.screen.blit(self.characterScreen, (self.drawX*Game.gridSize, self.drawY*Game.gridSize))
        if self.target != None:
            pixelOffset = -6+(abs(12-self.targetTick))
            targetWidth = 2
            positionOffset = (abs(12-self.targetTick)/2) + 6 + targetWidth/2
            playerTargetScreen = pygame.Surface((Game.gridSize + pixelOffset, Game.gridSize + pixelOffset))
            pygame.draw.rect(playerTargetScreen, Player.targetBracketColor, pygame.Rect(playerTargetScreen.get_width()/2-positionOffset, playerTargetScreen.get_height()/2-positionOffset, playerTargetScreen.get_width(), playerTargetScreen.get_height()), targetWidth)
            game.screen.blit(playerTargetScreen, ((self.target.drawX + 1.0/2)*Game.gridSize - positionOffset, (self.target.drawY + 1.0/2)*Game.gridSize - positionOffset))
            self.targetTick = (self.targetTick + 1)%24

    def levelUp(self, i):
        self.messages += ['Leveling Up ' + self.__class__.abilities[i].name + '!']
        self.levels[i] += 1

    def useAbility(self, index):
        if index >= len(self.__class__.abilities):
            self.messages += ['Ability key not bound']
            return
        self.messages += ['Casting ' + self.__class__.abilities[index].name + '!']
        self.__class__.abilities[index].cast(self, self.levels[index])

    def getMaxRange(self):
        maxRange = 0
        for spell in self.__class__.abilities:
            maxRange = max(maxRange, spell.spellRange)
        return maxRange

    def tabTarget(self, game):
        self.target = game.getClosestEnemy(self, self.getMaxRange())
        self.targetTick = 0
