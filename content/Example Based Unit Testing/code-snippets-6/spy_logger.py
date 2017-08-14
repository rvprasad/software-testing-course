from logger_interface import LoggerInterface
        

class SpyLogger(LoggerInterface):
    def __init__(self):
        self.num_of_calls = 0
        
    def get_num_of_calls(self):
        return self.num_of_calls
        
    def log(self, msg):
        # record data provided by the SUT (UserDB)
        self.num_of_calls += 1
        return True
