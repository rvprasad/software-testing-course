class DataStore(object):
    def create(self, name, value):
        # create a new entry that records the given name and value
        # return True if the entry was created; False, otherwise
        # each entry is unique in terms the associated name
        assert isinstance(name, str)
        assert isinstance(value, str)
        pass
        # assert isinstance(ret_val, bool)

    def read(self, name):
        # return the value of the existing entry corresponding to the name
        # raise RuntimeError exception if there is no entry with the name
        assert isinstance(name, str)
        pass
        # assert isinstance(ret_val, str)

    def update(self, name, value):
        # update the value of the existing entry corresponding to the name
        # return True if the entry was updated; false, otherwise
        assert isinstance(name, str)
        assert isinstance(value, str)
        pass
        # assert isinstance(ret_val, bool)

    def delete(self, name):
        # delete the existing entry corresponding to the name
        # return True if the entry was deleted; false, otherwise
        assert isinstance(name, str)
        pass
        # assert isinstance(ret_val, bool)

