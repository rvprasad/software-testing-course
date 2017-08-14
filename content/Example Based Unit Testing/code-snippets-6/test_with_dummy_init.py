from dummy_logger import DummyLogger    


class UserDB(object):
    def __init__(self, logger):
        self.logger = logger
        self.map = {}
    
    def add_user(self, name):
        self.logger.log("add_user {0}".format(name))
        tmp1 = "id{0}".format(len(self.map))
        self.map[tmp1] = name
    
    def size(self):
        return len(self.map)


class TestUserDB(object):
    def test_creation(self):
        assert self.db.size() == 0
