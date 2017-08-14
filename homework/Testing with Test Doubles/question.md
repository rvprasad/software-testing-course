This homework is intended to explore the use of test doubles for unit testing (in Python).

Sheryl Ellison contracted developers to implement an authentication component with the below interface.  She plans to use this component in her online marketplace.

She expects the authentication component to use the data store provided by her to store and retrieve user information.  The user name should be stored as is in the data store.  Also, the component to use the data store efficiently:
 - use it to only store user information and
 - use as fewer data store interactions as possible to realize each of the offered services (methods) (without saving any data in the component).

She wants you to write a test suite to test *AuthenticationComponent*.  Since the implementation of the data store is not available, she expects your tests to rely on test doubles.  Also, since the developers are still implementing the component, your tests should be based on the specification of the component (and the data store).

```
class AuthenticationComponent(object):
  def __init__(self, data_store):
    # create the component that uses the given data store to store user info
    assert isinstance(data_store, DataStore)
    self.data_store = data_store
    pass

  # DO NOT TEST THIS METHOD
  # Implementations can modify this function to plug in an apt transformation
  def transform_password(self, input):
      assert isinstance(input, str)
      return input
      # assert isinstance(ret_val, str)

  def create_user(self, user_name, password):
    # create a user with user_name and password
    # return True if the user was created; False, otherwise
    # user names are unique
    assert isinstance(user_name, str)
    assert isinstance(password, str)
    return self.data_store.create(user_name, self.transform_password(password))
    # assert isinstance(ret_val, bool)

  def login_user(self, user_name, password):
    # check if user_name and password represent an existing user
    # return True if user_name and password represent an existing user; False, otherwise
    assert isinstance(user_name, str)
    assert isinstance(password, str)
    pass
    # assert isinstance(ret_val, bool)

  def change_password(self, user_name, new_password):
    # change the password of user with user_name to new_password
    # return True if password was changed to new_password; False, otherwise
    assert isinstance(user_name, str)
    assert isinstance(new_password, str)
    pass
    # assert isinstance(ret_val, bool)

  def rename_user(self, user_name, new_user_name):
    # rename the user named user_name as new_user_name
    # return True if user was renamed; False, otherwise
    assert isinstance(user_name, str)
    assert isinstance(new_user_name, str)
    pass
    # assert isinstance(ret_val, bool)


class DataStore(object):
  def create(self, name, value):
    # create a new entry that records the given name and value
    # return True if the entry was created; False, otherwise
    # each entry is unique in terms of the associated name
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
```

Submit your test suite along with the test double(s) in a single file named *test_impl.py*.

We will place your tests in a folder along with *authentication_component_impl.py *and *data_store_interface.py*, and execute `pytest test_impl.py`.  So, add the following import statements to your *test_impl.py* and use the imported identifiers to test the provided implementation.
```
from data_store_interface import DataStore
from authentication_component_impl import AuthenticationComponent
```

To expedite grading of the homework, please ensure the name of the test case function/method that tests method X has the prefix *test_X*, e.g., a test case function/method that tests a specification of create_user should have the prefix *test_create_user*.

Please resolve any ambiguities about the problem by discussing them with the TA or the instructor ONLY via email or in-person.  When you identify ambiguities, describe them precisely and pose questions about them that will help you resolve ambiguities.  Examples of bad questions would be "what is missing in my implementation?" and "do you think my implementation is complete?"  Examples of good questions would be "Am I right in assuming sun goes around the moon?" and "when you said celestial bodies, did you mean the sun or the moon or something else?"

As mentioned in the policies of the course, collaboration is not allowed on assignments. So, do not use the discussion board to pose and discuss your questions.
