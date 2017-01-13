class Ability(object):
    # anything static and common to all abilities?

    def __init__(self, player):
        self.name = ''
        self.spell_range = 0
        self.max_level = 0
        self.cd_duration = 0
        self.level = 0
        self.current_cd = 0
        self.charges = 0
        self.player = player

    def cast(self):
        if not self.can_cast():
            return self.get_cannot_cast_message()
        self.go_on_cooldown()

    def set_level(self, level):
        self.level = level

    def go_on_cooldown(self):
        self.current_cd = self.cd_duration

    def can_cast(self):
        return self.current_cd <= 0 or self.charges > 0

    def get_cannot_cast_message(self):
        message = []
        message += [self.name + ' is still cooling down!']
        message += [str(self.current_cd) + ' server ticks remaining']
        return message

    # this one might get overwritten for some interesting ability functions,
    # can be used to determine durations of buffs, or delayed abilities maybe?
    # for stuff like that we'll have to implement buffs and callbacks.  TBD
    def update(self):
        # by default just reduce cd by 1 tick
        self.current_cd = max(self.current_cd - 1, 0)

    def level_up(self):
        self.level = min(self.level + 1, self.max_level)
