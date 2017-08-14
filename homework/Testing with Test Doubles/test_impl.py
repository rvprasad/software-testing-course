from data_store_interface import DataStore
from authentication_component_impl import AuthenticationComponent
import pytest


user_name_param = ["Hamilton"] #, "1234"]
password_param = ["234230987"] #, "!@!#$!)(*&"]
new_user_name_param = ["Jackson"] #, "Jane"]
new_password_param = ["ASDFADFA"] #, "?><|}':"]


def test_authentication_component_creation_succeeds():
    class DummyDataStore(DataStore):
        pass

    tmp1 = AuthenticationComponent(DummyDataStore())


class TestCreateUser(object):
    class SpyingStubDataStore(DataStore):
        def __init__(self):
            self.create_call_count = 0
            self.create_retval = None

        def create(self, name, value):
            self.create_call_count += 1
            self.user_name = name
            return self.create_retval
        
        def read(self, name):
            pytest.fail("read is not implemented")

        def update(self, name, value):
            pytest.fail("update is not implemented")

        def delete(self, name):
            pytest.fail("delete is not implemented")

    def setup_method(self):
        self.ds = TestCreateUser.SpyingStubDataStore()
        self.ac = AuthenticationComponent(self.ds)

    def teardown_method(self):
        self.ds = None

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    def test_returns_true_when_user_was_created(
            self, user_name, password):
        self.ds.create_retval = True
        assert self.ac.create_user(user_name, password), \
            "create_user returned false when user was created in data store"
        assert self.ds.user_name == user_name, \
            "create_user did not store the user name in the data store"
        assert self.ds.create_call_count == 1, \
            "create_user performed more than one operation on data store"

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    def test_returns_false_when_user_cannot_be_created(
            self, user_name, password):
        self.ds.create_retval = False
        assert not self.ac.create_user(user_name, password), \
            "create_user returned false when user could not \
be created in data store"
        assert self.ds.create_call_count == 1, \
            "create_user performed more than one operation on data store"


class TestLoginUser(object):
    class SpyingFakeDataStore(DataStore):
        def __init__(self):
            self.call_count = 0
            self.data = {}

        def create(self, name, value):
            self.call_count += 1
            self.data[name] = value
            return True

        def read(self, name):
            self.call_count += 1
            if name in self.data:
                return self.data[name]
            else:
                raise RuntimeError("Name not in data store")
        
        def update(self, name, value):
            pytest.fail("update is not implemented")

        def delete(self, name):
            pytest.fail("delete is not implemented")

    def setup_method(self):
        self.ds = TestLoginUser.SpyingFakeDataStore()
        self.ac = AuthenticationComponent(self.ds)

    def teardown_method(self):
        self.ac = None
        self.ds = None

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    def test_returns_true_when_user_exists(self, user_name, password):
        self.ac.create_user(user_name, password)
        self.ds.call_count = 0
        assert self.ac.login_user(user_name, password), \
            "login_user returned false for an existing user"
        assert self.ds.call_count == 1, \
            "login_user performed more than one operation on data store"

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    def test_returns_false_when_user_does_not_exist(
            self, user_name, password):
        assert not self.ac.login_user(user_name, password), \
            "login_user returned true for a non-existent user name"
        assert self.ds.call_count == 1, \
            "login_user performed more than one operation on data store"

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    def test_returns_false_when_password_does_not_match(
            self, user_name, password):
        self.ac.create_user(user_name, password)
        self.ds.call_count = 0
        assert not self.ac.login_user(user_name, "x" + password), \
            "login_user returned true when password did not match"
        assert self.ds.call_count == 1, \
            "login_user performed more than one operation on data store"


class TestChangePassword(object):
    class SpyingFakeDataStore(DataStore):
        def __init__(self):
            self.call_count = 0
            self.data = {}

        def create(self, name, value):
            self.call_count += 1
            self.data[name] = value
            return True

        def read(self, name):
            self.call_count += 1
            if name in self.data:
                return self.data[name]
            else:
                raise RuntimeError("Name not in store")

        def update(self, name, value):
            self.call_count += 1
            if name in self.data:
                self.data[name] = value
                return True
            else:
                return False
        
        def delete(self, name):
            pytest.fail("delete is not implemented")

    def setup_method(self):
        self.ds = TestChangePassword.SpyingFakeDataStore()
        self.ac = AuthenticationComponent(self.ds)

    def teardown_method(self):
        self.ac = None
        self.ds = None

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    @pytest.mark.parametrize("new_password", new_password_param)
    def test_returns_true_when_user_exists(
            self, user_name, password, new_password):
        self.ac.create_user(user_name, password)
        self.ds.call_count = 0
        assert self.ac.change_password(user_name, new_password), \
            "change_password returned false for existing user"
        assert self.ds.call_count == 1, \
            "change_password performed excess operations on the data store"
        assert self.ac.login_user(user_name, new_password), \
            "change_password did not change the password"

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    def test_returns_false_when_user_does_not_exists(
            self, user_name, password):
        self.ds.call_count = 0
        assert not self.ac.change_password(user_name, password), \
            "change_password returned true for non-existent user"
        assert self.ds.call_count == 1, \
            "change_password performed excess operations on the data store"
        assert not self.ac.login_user(user_name, password), \
            "change_password changed the password"


class TestRenameUser(object):
    class MockDataStore(DataStore):
        def __init__(self):
            self.call_count = 0
            self.create_retval = True
            self.delete_retval = True
            self.read_retval = True
            self.read_throw = False
            self.new_name = None
            self.old_name = None
            self.new_password = None
            self.new_password_was_set = False
            self.create_called = False

        def reset_call_count(self):
            self.call_count = 0

        def create(self, name, value):
            self.call_count += 1
            self.create_called = True
            assert (not self.new_name) or name == self.new_name, \
                "rename_user did not pass the new name to the data store"
            self.new_password_was_set = True
            self.new_password = value
            return self.create_retval

        def read(self, name):
            self.call_count += 1
            self.read_called = True
            if self.read_throw:
                raise RuntimeError("Name not in store")
            else:
                return self.read_retval

        def update(self, name, value):
            pytest.fail("update is not implemented")

        def delete(self, name):
            self.call_count += 1
            self.delete_called = True
            assert (not self.old_name) or name == self.old_name, \
                "rename_user did not remove the old name from the data store"
            return self.delete_retval

        def being_renamed(self, old_name, new_name):
            self.old_name = old_name
            self.new_name = new_name

        def verify(self):
            assert self.call_count <= 3, \
                "rename_user performed excess operations on the data store"
            assert (not self.new_password_was_set) or \
                self.new_password == self.read_retval, \
                "rename_user did not copy password"

    def setup_method(self):
        self.ds = TestRenameUser.MockDataStore()
        self.ac = AuthenticationComponent(self.ds)

    def teardown_method(self):
        self.ac = None
        self.ds = None

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    @pytest.mark.parametrize("new_name", new_user_name_param)
    def test_returns_true_when_user_exists(
            self, user_name, password, new_name):
        self.ds.read_retval = password
        self.ds.being_renamed(user_name, new_name)
        assert self.ac.rename_user(user_name, new_name), \
            "rename_user returned false for existing user"
        self.ds.verify()

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    def test_returns_true_when_user_exists_and_renames_to_same_name(
            self, user_name, password):
        self.ds.read_retval = password
        self.ds.being_renamed(user_name, user_name)
        assert self.ac.rename_user(user_name, user_name), \
            "rename_user returned false for existing user"
        self.ds.verify()

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    @pytest.mark.parametrize("new_name", new_user_name_param)
    def test_returns_false_when_user_does_not_exists(
            self, user_name, password, new_name):
        self.ds.read_throws = True
        self.ds.create_retval = True
        self.ds.delete_retval = False
        self.ds.being_renamed(user_name, new_name)
        assert not self.ac.rename_user(user_name, new_name), \
            "rename_user returned true for non-existent user"
        self.ds.verify()

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    @pytest.mark.parametrize("new_name", new_user_name_param)
    def test_returns_false_when_user_cannot_be_created(
            self, user_name, password, new_name):
        self.ds.create_retval = False
        self.ds.read_retval = password
        self.ds.being_renamed(user_name, new_name)
        assert not self.ac.rename_user(user_name, new_name), \
            "rename_user returned true when user cannot be created"
        self.ds.verify()

    @pytest.mark.parametrize("user_name", user_name_param)
    @pytest.mark.parametrize("password", password_param)
    @pytest.mark.parametrize("new_name", new_user_name_param)
    def test_returns_false_when_user_cannot_be_deleted(
            self, user_name, password, new_name):
        self.ds.delete_retval = False
        self.ds.read_retval = password
        self.ds.being_renamed(user_name, new_name)
        assert not self.ac.rename_user(user_name, new_name), \
            "rename_user returned true when user cannot be deleted"
        self.ds.verify()

