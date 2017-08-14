import math

class Queue(object):
    def __init__(self):
        self.__values = []

    def enqueue(self, v):
        if v == None or (isinstance(v, float) and \
            (math.isnan(v) or math.isinf(v))):
            raise ValueError("Unsupported value: {0}".format(v))
        self.__values.insert(0, v)

    def dequeue(self):
        if len(self.__values) == 0:
            return None
        else:
            return self.__values.pop()

    def len(self):
        self.__values.insert(0, 0)
        return len(self.__values)

