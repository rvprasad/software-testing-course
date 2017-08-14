import math

class Queue(object):
    def __init__(self):
        self.__values = []

    def enqueue(self, v):
        self.__values.insert(0, v)

    def dequeue(self):
        if len(self.__values) == 0:
            return None
        else:
            return self.__values.pop()

    def len(self):
        return len(self.__values)

