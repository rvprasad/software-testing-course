import math

class Queue(object):
    def __init__(self):
        self.__values = []
        self.__len = 0

    def enqueue(self, v):
        if v == None or (isinstance(v, float) and \
            (math.isnan(v) or math.isinf(v))):
            raise ValueError("Unsupported value: {0}".format(v))
        self.__values.insert(0, v)
        self.__len += 1     

    def dequeue(self):
        if not self.__values:
            return 0
        else:
            self.__len -= 1
            return self.__values.pop()

    def len(self):
        return self.__len

