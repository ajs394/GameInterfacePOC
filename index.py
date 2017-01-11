import pygame
import random
from Game import Game
from Grid import Grid
from TextWindow import TextWindow
from Player import Player
from Mage import Mage
from Enemy import Enemy

pygame.init()

done = False

game = Game()
grid = Grid()
textWindow = TextWindow()
game.setBackgroundImage(grid.gridScreen)
game.setTextWindow(textWindow)
player = Mage()
enemy = player
game.addGameObject(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x = y = 0
    pressed = pygame.key.get_pressed()

    # first player movement
    if pressed[pygame.K_RETURN]:
        enemyXPos = random.randrange(0, game.gridMaxX-1, 1)
        enemyYPos = random.randrange(0, game.gridMaxY-1, 1)
        while game.isGridSpaceOccupied((enemyXPos, enemyYPos)): 
            enemyXPos = random.randrange(0, game.gridMaxX-1, 1)
            enemyYPos = random.randrange(0, game.gridMaxY-1, 1)
        enemy = Enemy((enemyXPos, enemyYPos))
        game.addGameObject(enemy)
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
        enemy.move(x, y)

    # abilities and leveling
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_1]:
        player.useAbility(0)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_1]:
        player.levelUp(0)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_2]:
        player.useAbility(1)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_2]:
        player.levelUp(1)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_3]:
        player.useAbility(2)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_3]:
        player.levelUp(2)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_4]:
        player.useAbility(3)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_4]:
        player.levelUp(3)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_5]:
        player.useAbility(4)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_5]:
        player.levelUp(4)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_6]:
        player.useAbility(5)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_6]:
        player.levelUp(5)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_7]:
        player.useAbility(6)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_7]:
        player.levelUp(6)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_8]:
        player.useAbility(7)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_8]:
        player.levelUp(7)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_9]:
        player.useAbility(8)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_9]:
        player.levelUp(8)

    # tab targeting
    if pressed[pygame.K_TAB]:
        player.tabTarget(game)

    # Add this somewhere after the event pumping and before the display.flip() 
    game.update().draw()
    pygame.display.flip()
    pygame.time.delay(50)