from stub_logger import StubLogger


class UserDB(object):
    def __init__(self, logger):
        self.logger = logger
        self.map = {}
    
    def add_user(self, name):
        if not self.logger.log("add_user {0}".format(name)):
            raise RuntimeError("Unable to Log")
        tmp1 = "id{0}".format(len(self.map))
        self.map[tmp1] = name
    
    def size(self):
        return len(self.map)


class TestUserDB(object):    
    def setup_method(self):
        self.logger = StubLogger()
        self.db =  UserDB(self.logger)
    
    def test_when_logger_succeeds(self):
        # we set the value to be returned by log() method of stub object
        self.logger.set_return_value(True)
        try:
            self.db.add_user("John Doe")
        except RuntimeError:
            assert False
            
    def test_when_logger_fails(self):
        # we set the value to be returned by log() method of stub object
        self.logger.set_return_value(False)
        try:
            self.db.add_user("John Doe")
            assert False
        except RuntimeError:
            assert True