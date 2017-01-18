class PlayerEffect(object):

    def __init__(self):
        self.name = ''
        self.remaining_duration = 0
        self.max_duration = 0
        self.count = 0

    def update(self, player):
        raise NotImplementedError

    #indicates that the duration of the effect refreshes on new instance
    def can_refresh(self):
        return False

    #indicates that the effect can have an increasing counter
    def can_stack(self):
        return False

    #indicates that the effect stacks uniquely
    def is_unique(self):
        return False
