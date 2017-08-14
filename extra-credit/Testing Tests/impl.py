import math

class Stack(object):
    def __init__(self):
        self.__values = []

    def push(self, v):
        if v == None or (isinstance(v, float) and (math.isnan(v) or math.isinf(v))):
            raise ValueError("Unsupported value: {0}".format(v))
        self.__values.append(v)

    def pop(self):
        if len(self.__values) == 0:
            return None
        else:
            return self.__values.pop()

    def len(self):
        return float(len(self.__values))

