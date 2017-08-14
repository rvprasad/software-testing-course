from logger_interface import LoggerInterface
        

# A logger that prints the message to the console
class FakeLogger(LoggerInterface):
    def log(self, msg):
        print("Log: {0}".format(msg))
        return True
