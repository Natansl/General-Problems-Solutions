
class Stack(object):
    def __init__(self):
        self.__stack__ = []

    def put(self, val):
        self.__stack__.append(val)

    def take(self):
        return self.__stack__.pop()