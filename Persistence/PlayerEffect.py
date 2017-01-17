from abc import ABCMeta

class PlayerEffect(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        raise NotImplementedError

    def update(self, player):
        raise NotImplementedError
