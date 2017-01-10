import pygame
from Game import Game

class TextWindow(object):
    pygame.font.init()
    textFont = pygame.font.SysFont("monospace", 15)
    textColor = (255, 255, 0)

    def __init__(self):
        self.messageList = []
        self.textScreen = pygame.Surface((Game.textWidth, Game.textHeight))

    def writeStrings(self, messages):
        for message in messages:
            self.messageList += [str(message)]
        while len(self.messageList) > 20:
            self.messageList.pop(0)
        self.textScreen = pygame.Surface((Game.textWidth, Game.textHeight))
        for i in range(len(self.messageList)):
            message = TextWindow.textFont.render(self.messageList[i], 1, TextWindow.textColor)
            self.textScreen.blit(message, (Game.textWidth/2 - message.get_width()/2, i*15))