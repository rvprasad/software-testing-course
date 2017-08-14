from logger_interface import LoggerInterface
        

class StubLogger(LoggerInterface):
    def __init__(self):
        self.ret_val = False

    # set the values to be provided as indirect input to SUT
    def set_return_value(self, value):
        self.ret_val = value;
    
    def log(self, msg):
        return self.ret_val