from Player import Player
class Ability(object):
    # anything static and common to all abilities?

    def __init__(self, player):
        self.name = ''
        self.spellRange = 0
        self.maxLevel = 0
        self.CD_DURATION = 0
        self.level = 0
        self.currentCd = 0
        self.charges = 0
        self.player = player

    def cast(self):
        if not self.canCast():
            return self.getCannotCastMessage()
        self.currentCd = self.CD_DURATION

    def setLevel(self, level):
        self.level = level

    def goOnCooldown(self):
        self.currentCd = self.CD_DURATION

    def canCast(self):
        return self.currentCd <= 0 or self.charges > 0

    def getCannotCastMessage(self):        
        message = []
        message += [self.name + ' is still cooling down!']
        message += [str(self.currentCd) + ' server ticks remaining']
        return message

    # this one might get overwritten for some interesting ability functions,
    # can be used to determine durations of buffs, or delayed abilities maybe?
    # for stuff like that we'll have to implement buffs and callbacks.  TBD
    def update(self):
        # by default just reduce cd by 1 tick
        self.currentCd = max(self.currentCd - 1, 0)

    def levelUp(self):
        self.level = min(self.level + 1, self.maxLevel)