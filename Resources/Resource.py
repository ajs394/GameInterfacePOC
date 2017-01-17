from abc import ABCMeta

class Resource(object):
    __metaclass__ = ABCMeta

    def check_can_cast(self, cost):
        raise NotImplementedError

    def modify(self, change):
        raise NotImplementedError

    def update(self, character):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    def get_curr_percentage(self):
        raise NotImplementedError
