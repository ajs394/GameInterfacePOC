import pygame
from Game import Game
from Grid import Grid
from TextWindow import TextWindow
from Player import Player
from Mage import Mage

pygame.init()

done = False

game = Game()
grid = Grid()
textWindow = TextWindow()
game.setBackgroundImage(grid.gridScreen)
game.setTextWindow(textWindow)
player = Mage()
player2 = player
game.addGameObject(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x = y = 0
    pressed = pygame.key.get_pressed()

    # first player movement
    if pressed[pygame.K_RETURN]:
        player2 = Player()
        game.addGameObject(player2)
    if pressed[pygame.K_UP]: 
        y -= 1
    if pressed[pygame.K_DOWN]: 
        y += 1
    if pressed[pygame.K_LEFT]: 
        x -= 1
    if pressed[pygame.K_RIGHT]: 
        x += 1
    if x != 0 or y != 0:
        player.move(x, y)

    # second player movement
    x = y = 0
    if pressed[pygame.K_w]: 
        y -= 1
    if pressed[pygame.K_s]: 
        y += 1
    if pressed[pygame.K_a]: 
        x -= 1
    if pressed[pygame.K_d]: 
        x += 1
    if x != 0 or y != 0:
        player2.move(x, y)

    # abilities and leveling
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_1]:
        player.useAbility(0)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_1]:
        player.levelUp()

    # Add this somewhere after the event pumping and before the display.flip() 
    game.update().draw()
    pygame.display.flip()
    pygame.time.delay(50)