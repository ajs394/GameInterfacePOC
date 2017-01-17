from abc import ABCMeta

class GameObject(object):
    __metaclass__ = ABCMeta

    def draw(self, game):
        raise NotImplementedError

    def update(self, game):
        raise NotImplementedError
