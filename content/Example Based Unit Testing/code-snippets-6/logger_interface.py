from abc import ABCMeta, abstractmethod

class LoggerInterface(object):
    # log the message
    # return True if the message was logged
    # return False if the message was not logged
    def log(self, msg):
        raise NotImplementedError()
