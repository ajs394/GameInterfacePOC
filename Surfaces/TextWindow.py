import pygame
from GameInterfacePOC.Game.Game import Game

class TextWindow(object):
    pygame.font.init()
    textFont = pygame.font.SysFont("monospace", 15)
    textColor = (255, 255, 0)

    def __init__(self):
        self.message_list = []
        self.text_screen = pygame.Surface((Game.text_width, Game.text_height))

    def write_strings(self, messages):
        for message in messages:
            self.message_list += [str(message)]
        while len(self.message_list) > 20:
            self.message_list.pop(0)
        self.text_screen = pygame.Surface((Game.text_width, Game.text_height))
        for i in range(len(self.message_list)):
            message = TextWindow.textFont.render(self.message_list[i], 1, TextWindow.textColor)
            self.text_screen.blit(message, (Game.text_width/2 - message.get_width()/2, i*15))
