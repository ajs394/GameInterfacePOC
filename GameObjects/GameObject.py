from abc import ABCMeta

class GameObject(object):
    __metaclass__ = ABCMeta

    def __init__(self, game):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError
