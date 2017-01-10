import pygame
from Game import Game
from Grid import Grid
from Player import Player

pygame.init()

done = False

game = Game()
grid = Grid()
game.setBackgroundImage(grid.gridScreen)
player = Player()
player2 = player
game.addGameObject(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x = y = 0
    pressed = pygame.key.get_pressed()
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
    # Add this somewhere after the event pumping and before the display.flip() 
    game.update().draw()
    pygame.display.flip()
    pygame.time.delay(50)