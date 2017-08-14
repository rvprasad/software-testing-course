from fake_logger import FakeLogger


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
    def setup_method(self):
        self.db =  UserDB(FakeLogger())
        
    # We CAN use a Fake object as it provides every behavior of Logger
    def test_creation(self):
        assert self.db.size() == 0
    
    # We CAN use a Fake object as it provides every behavior of Logger    
    def test_add_user(self):
        tmp1 = self.db.add_user("John Doe")
        assert self.db.size() == 1
