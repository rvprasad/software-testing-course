class Stack(object):
    def __init__(self):
        self.__values = []
        self.__len = 1

    def push(self, v):
        if v == None:
            raise ValueError("Unsupported value: {0}".format(v))
        self.__values.append(v)
        self.__len += 1

    def pop(self):
        if len(self.__values) == 0:
            return None
        else:
            self.__len -= 2
            return self.__values.pop()

    def len(self):
        return self.__len

