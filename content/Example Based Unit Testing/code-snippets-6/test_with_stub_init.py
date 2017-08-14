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
    def test_when_logger_succeeds(self):
        try:
            self.db.add_user("John Doe")
        except RuntimeError:
            assert False
            
    def test_when_logger_fails(self):
        try:
            self.db.add_user("John Doe")
            assert False
        except RuntimeError:
            assert True