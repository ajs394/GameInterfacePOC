# pylint: disable=C0103
import random
import pygame
from GameInterfacePOC.Game.Game import Game
from GameInterfacePOC.Surfaces.Grid import Grid
from GameInterfacePOC.Surfaces.TextWindow import TextWindow
from GameInterfacePOC.GameObjects.Characters.Enemy import Enemy
from GameInterfacePOC.CharacterClasses.Mage import Mage

pygame.init()

done = False

game = Game()
grid = Grid()
text_window = TextWindow()
game.set_background_image(grid.grid_screen)
game.set_text_window(text_window)
player = Mage(game)
enemy = player
game.add_game_object(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x = y = 0
    pressed = pygame.key.get_pressed()

    # first player movement
    if pressed[pygame.K_RETURN]:
        enemy_x_pos = random.randrange(0, game.grid_max_x-1, 1)
        enemy_y_pos = random.randrange(0, game.grid_max_y-1, 1)
        while game.is_grid_space_occupied((enemy_x_pos, enemy_y_pos)):
            enemy_x_pos = random.randrange(0, game.grid_max_x-1, 1)
            enemy_y_pos = random.randrange(0, game.grid_max_y-1, 1)
        enemy = Enemy(game, (enemy_x_pos, enemy_y_pos))
        game.add_game_object(enemy)
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
        player.use_ability(0)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_1]:
        player.level_up(0)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_2]:
        player.use_ability(1)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_2]:
        player.level_up(1)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_3]:
        player.use_ability(2)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_3]:
        player.level_up(2)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_4]:
        player.use_ability(3)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_4]:
        player.level_up(3)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_5]:
        player.use_ability(4)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_5]:
        player.level_up(4)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_6]:
        player.use_ability(5)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_6]:
        player.level_up(5)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_7]:
        player.use_ability(6)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_7]:
        player.level_up(6)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_8]:
        player.use_ability(7)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_8]:
        player.level_up(7)
    if not pressed[pygame.K_LSHIFT] and pressed[pygame.K_9]:
        player.use_ability(8)
    if pressed[pygame.K_LSHIFT] and pressed[pygame.K_9]:
        player.level_up(8)

    # tab targeting
    if pressed[pygame.K_TAB]:
        player.tab_target()

    # Add this somewhere after the event pumping and before the display.flip()
    game.update().draw()
    pygame.display.flip()
    pygame.time.delay(Game.server_tick_length)
