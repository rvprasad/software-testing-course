class Stack(object):
    def __init__(self):
        self.__value = None
        self.__len = 0

    def push(self, v):
        if v == None:
            raise ValueError("Unsupported value: {0}".format(v))
        self.__value = v
        self.__len += 1

    def pop(self):
        if self.__len == 0:
            return None
        else:
            self.__len -= 1
            return self.__value

    def len(self):
        return self.__len

