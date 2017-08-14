class Stack(object):
    def __init__(self):
        self.__values = []

    def push(self, v):
        if v == None or not (isinstance(v, float) and 
            isinstance(v, int) and isinstance(v, str) and
            isinstance(v, bool)):
            raise ValueError("Unsupported value: {0}".format(v))
        self.__values.append(v)

    def pop(self):
        if len(self.__values) == 0:
            return None
        else:
            return self.__values.pop()

    def len(self):
        return len(self.__values)

