import pygame
import math

class Game(object):
    SERVER_TICK_LENGTH = 50
    MAX_TICKS = 10.0
    gridWidth = 400
    gridHeight = 300
    textWidth = 400
    textHeight = 300
    gridSize = 20
    gridMaxX = gridWidth/gridSize
    gridMaxY = gridHeight/gridSize

    def __init__(self):    
        self.grid = [[None for y in xrange(Game.gridMaxY)] for x in xrange(Game.gridMaxX)]
        self.screenDirty = True
        self.gameObjects = []
        self.bcg = None
        self.tw = None
        self.screen = pygame.display.set_mode((max(Game.gridWidth, Game.textWidth), Game.gridHeight + Game.textHeight))
    
    def addGameObject(self, obj):
        pos = obj.pos
        if self.isGridSpaceOccupied(pos):
            return
        self.gameObjects += [obj]
        self.grid[pos[0]][pos[1]] = obj
        obj._GRID_LOC = pos

    def isGridSpaceOccupied(self, pos):
        if self.grid[pos[0]][pos[1]] != None:
            return True
        return False

    def getClosestEnemy(self, char, maxRange):
        targetRange = maxRange + 1
        target = None
        for gChar in self.gameObjects:
            if char.isHostile(gChar):
                currRange = self.getDistance(char.pos, gChar.pos)
                if currRange < targetRange:
                    targetRange = currRange
                    target = gChar
        return target

    def getDistance(self, pos1, pos2):
        return int(math.ceil(math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)))
        
    def checkObjectMoveIsSafe(self, pos1, pos2):
        if pos1 == pos2:
            return True
        hitPositions = []
        xRight = 1 if (pos2[0] >= pos1[0]) else -1
        yDown = 1 if (pos2[1] >= pos1[1]) else -1
        diffX = abs(pos1[0] - pos2[0])
        diffY = abs(pos1[1] - pos2[1])
        slope = float(diffY)/diffX
        if diffX > diffY:
            ypos = pos1[1]
            count = 0
            xToMove = 1/slope
            while ypos != pos2[1]:
                xpos = pos1[0] + count*int(math.floor(xToMove))
                for i in range(int(math.ceil(xToMove + 1))):
                    hitPositions += [(xpos + i*xRight, ypos)]
                    hitPositions += [(xpos + i*xRight, ypos + yDown)]
                ypos += yDown
                count += 1
        else:
            xpos = pos1[0]
            yToMove = slope
            count = 0
            while xpos != pos2[0]:
                ypos = pos1[1] + count*int(math.floor(yToMove))
                for i in range(int(math.ceil(yToMove + 1))):
                    hitPositions += [(xpos, ypos + i*yDown)]
                    hitPositions += [(xpos + xRight, ypos + i*yDown)]
                xpos += xRight
                count += 1
        # remove the self reference at the beginning of list
        hitPositions.pop(0)
        for pos in hitPositions:
            if pos[0] >= Game.gridMaxX or pos[1] >= Game.gridMaxY:
                return False
            if pos[0] < 0 or pos[1] < 0:
                return False
            if self.isGridSpaceOccupied(pos):
                return False
        return True

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