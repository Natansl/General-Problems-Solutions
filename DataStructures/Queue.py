
class Queue(object):
    def __init__(self):
        self.__queue__ = []

    def put(self, val):
        self.__queue__.append(val)

    def take(self):
        out = self.__queue__[0]
        del self.__queue__[0]
        return out 