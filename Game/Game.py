import pygame
import math

class Game(object):
    server_tick_length = 50
    max_ticks = 10.0
    grid_width = 400
    grid_height = 300
    text_width = 400
    text_height = 300
    grid_size = 20
    grid_max_x = grid_width/grid_size
    grid_max_y = grid_height/grid_size

    def __init__(self):
        self.grid = [[None for _ in xrange(Game.grid_max_y)] for _ in xrange(Game.grid_max_x)]
        self.screen_dirty = True
        self.game_objects = []
        self.bcg = None
        self.text_writer = None
        self.screen = pygame.display.set_mode((max(Game.grid_width, Game.text_width),
                                               Game.grid_height + Game.text_height))

    def add_game_object(self, obj):
        pos = obj.pos
        if self.is_grid_space_occupied(pos):
            return
        self.game_objects += [obj]
        self.grid[pos[0]][pos[1]] = obj

    def is_grid_space_occupied(self, pos):
        if self.grid[pos[0]][pos[1]] != None:
            return True
        return False

    def get_closest_enemy(self, char, max_range):
        target_range = max_range + 1
        target = None
        for game_char in self.game_objects:
            if char.is_hostile(game_char):
                curr_range = self.get_distance(char.pos, game_char.pos)
                if curr_range < target_range:
                    target_range = curr_range
                    target = game_char
        return target

    def get_distance(self, pos1, pos2):
        return int(math.ceil(math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)))

    def check_object_move_is_safe(self, pos1, pos2):
        # this method can get cleaned significantly.  I'll get around to it
        if pos1 == pos2:
            return True
        hit_positions = []
        x_right = 1 if (pos2[0] >= pos1[0]) else -1
        y_down = 1 if (pos2[1] >= pos1[1]) else -1
        diff_x = abs(pos1[0] - pos2[0])
        diff_y = abs(pos1[1] - pos2[1])
        slope = float(diff_y)/diff_x
        if diff_x > diff_y:
            ypos = pos1[1]
            count = 0
            x_to_move = 1/slope
            while ypos != pos2[1]:
                xpos = pos1[0] + count*int(math.floor(x_to_move))
                for i in range(int(math.ceil(x_to_move + 1))):
                    hit_positions += [(xpos + i*x_right, ypos)]
                    hit_positions += [(xpos + i*x_right, ypos + y_down)]
                ypos += y_down
                count += 1
        else:
            xpos = pos1[0]
            y_to_move = slope
            count = 0
            while xpos != pos2[0]:
                ypos = pos1[1] + count*int(math.floor(y_to_move))
                for i in range(int(math.ceil(y_to_move + 1))):
                    hit_positions += [(xpos, ypos + i*y_down)]
                    hit_positions += [(xpos + x_right, ypos + i*y_down)]
                xpos += x_right
                count += 1
        # remove the self reference at the beginning of list
        hit_positions.pop(0)
        for pos in hit_positions:
            if pos[0] >= Game.grid_max_x or pos[1] >= Game.grid_max_y:
                return False
            if pos[0] < 0 or pos[1] < 0:
                return False
            if self.is_grid_space_occupied(pos):
                return False
        return True

    def set_background_image(self, bcg):
        self.bcg = bcg

    def set_text_window(self, tw):
        self.text_writer = tw

    def set_dirty(self):
        self.screen_dirty = True

    def write_message(self, message):
        self.text_writer.write_strings(message)

    def update(self):
        for obj in self.game_objects:
            obj.update(self)
        return self

    def draw(self):
        # unsure whether or not we need to be cautious with redraws.  Pygame might
        # handle a lot of keeping that efficient on it's own.  Commenting out for 
        # now
        #if not self.screen_dirty:
        #    return
        self.screen.blit(self.bcg, (0, 0))
        self.screen.blit(self.text_writer.text_screen, (0, Game.grid_height))
        for obj in self.game_objects:
            obj.draw(self)
        self.screen_dirty = False
        return self
