import re
from logger_interface import LoggerInterface
        

class MockLogger(LoggerInterface):
    def __init__(self):
        self.num_of_calls = 0
        
    def log(self, msg):
        # verification on indirect output from SUT
        assert re.search(self.expected_pattern, msg), \
            "{0} did not have expected pattern {1}".format(msg, 
            self.expected_pattern) # check if the message had exptected pattern
            
        # record data provided by the SUT (UserDB) for final verification
        self.num_of_calls += 1
        return True
        
    def set_expected_pattern(self, pattern):
        self.expected_pattern = pattern

    # perform final verification 
    def verify(self):
        assert self.num_of_calls == 1
        