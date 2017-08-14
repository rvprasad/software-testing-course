from spy_logger import SpyLogger


class UserDB(object):
    def __init__(self, logger):
        self.logger = logger
        self.map = {}
    
    def add_user(self, name):
        self.logger.log("add_user {0}".format(name))
        tmp1 = "id{0}".format(len(self.map))
        self.map[tmp1] = name
        return tmp1
    
    def size(self):
        return len(self.map)


class TestUserDB(object):    
    def test_logger_is_used_appropriately(self):
        db.add_user("John Doe")
        db.add_user("Jane Doe")
