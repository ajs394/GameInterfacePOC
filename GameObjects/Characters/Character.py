from GameInterfacePOC.GameObjects.GameObject import GameObject
from GameInterfacePOC.Game.Game import Game

class Character(GameObject):
    # in server ticks
    gcd_duration = 10.0
    MOVEMENT_DURATION = 10.0

    def __init__(self, game):
        self.game = game
        self.is_alive = True
        self.health = 100.0
        self.max_health = 100
        self.health_regen = .1
        self.gcd_tick = 0
        self.messages = []
        self.faction = ''
        self.name = 'No Name Set'
        self.can_move = True
        self.update_tick = 0
        self.color = None
        self.pos = (0, 0)
        self.draw_x = self.pos[0]
        self.draw_y = self.pos[1]
        self.destination_pos = self.pos
        self.character_screen = None

    def draw(self):
        self.game.screen.blit(self.character_screen, (self.draw_x*Game.grid_size,
                                                      self.draw_y*Game.grid_size))

    def move(self, x, y):
        if not self.can_move:
            return
        new_x = self.pos[0] + x
        new_y = self.pos[1] + y
        if new_x < 0:
            new_x = 0
        if new_x >= Game.grid_max_x:
            new_x = Game.grid_max_x - 1
        if new_y < 0:
            new_y = 0
        if new_y >= Game.grid_max_y:
            new_y = Game.grid_max_y - 1
        if new_x == self.pos[0] and new_y == self.pos[1]:
            return
        self.can_move = False
        self.destination_pos = (new_x, new_y)

    def update(self):
        if self.destination_pos[0] != self.pos[0] or self.destination_pos[1] != self.pos[1]:
            self.game.set_dirty()
            self.update_tick += 1
            self.draw_x = self.pos[0] + ((self.destination_pos[0] - self.pos[0])*
                                         self.update_tick/Character.MOVEMENT_DURATION)
            self.draw_y = self.pos[1] + ((self.destination_pos[1] - self.pos[1])*
                                         self.update_tick/Character.MOVEMENT_DURATION)
            if self.update_tick == Character.MOVEMENT_DURATION:
                self.update_tick = 0
                self.can_move = True
                self.pos = self.destination_pos
        if self.gcd_tick > 0:
            self.gcd_tick -= 1
        if self.is_dying():
            self.die()
        if not self.is_alive:
            self.messages += ['I unfortunately appear to have died :(']
        if self.messages != []:
            for message in self.messages:
                self.game.write_message([self.name + ': ' + message])
            self.messages = []
        if not self.is_alive:
            self.game.remove_game_object(self)
        self.modify_health(self.health_regen)

    def set_gcd(self):
        self.gcd_tick = Character.gcd_duration

    def is_hostile(self, other):
        return self.faction != other.faction

    def modify_health(self, change):
        self.health += change
        self.health = min(self.max_health, max(self.health, 0))

    def is_dying(self):
        if self.health <= 0:
            return True
        return False

    def die(self):
        self.is_alive = False
