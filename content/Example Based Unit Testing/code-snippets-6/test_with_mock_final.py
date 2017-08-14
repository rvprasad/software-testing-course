from mock_logger import MockLogger


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
    def test_logger_is_used_as_expected(self):
        logger = MockLogger()
        # set the expected pattern of log message
        logger.set_expected_pattern(r".*add_user.*")
        db = UserDB(logger)
        db.add_user("Jane Doe")
        # final verification is delegated to the mock
        logger.verify()
