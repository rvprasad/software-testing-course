This homework is intended to explore example-based unit testing in Python.

This is the dual of 'Develop A Python Program' homework

Mark Jobs had a brilliant idea of constructing a network of people in which nodes represent people and edges between nodes represent relationships between people.  In this network, he wanted to capture various properties about people and relationships.  Also, he wanted to query the network

- for persons using their names and
- for all current friends of current friends of a person.

A slew of developers created different implementations of the network that conform to the following signature/interface.  Now, to select one of these implementations to use, Mark needs your help to identify which of these implementations are correct.  For this purpose, he wants you to write unit tests to test implementations of this signature/interface. [19 points]

```
class Network(object):
  def __init__(self):
    # constructor
    pass
  def create_person(self):
    # create a person in the network and return the person
    pass
  def add_person_property(self, person, prop, value):
    # add property to a person
    pass
  def add_relation(self, person1, person2):
    # add a relation
    pass
  def add_relation_property(self, person1, person2, prop, value):
    # add property to the relation between person1 and person2
    pass
  def get_person(self, name):
    # get the person with given name
    pass
  def friends_of_friends(self, name):
    # get a list of current friends of current friends of the person with given name
    pass
  ```

Submit your implementation in a single file named *test_impl.py*.

We will place your submission in a folder with an implementation *impl.py* and execute `pytest test_impl.py`.  Naming your file appropriately to enable this composability is worth 1 point.  We will evaluate your tests on their ability to correctly identify/flag valid and invalid implementations of the signature/interface.

To expedite grading of the homework, please ensure the name of the test case function/method that tests method X has the prefix `test_X`, e.g., a test case function/method that tests a specification of `add_person_property` should have the prefix `test_add_person_property`.

Please resolve any ambiguities about the problem by discussing them with the TA or the instructor ONLY via email or in-person.  When you identify ambiguities, describe them precisely and pose questions about them that will help you resolve ambiguities.  Examples of bad questions would be "what is missing in my implementation?" and "do you think my implementation is complete?"  Examples of good questions would be "Am I right in assuming sun goes around the moon?" and "when you said celestial bodies, did you mean the sun or the moon or something else?"

As mentioned in the policies of the course, collaboration is not allowed on assignments.  So, do not use the discussion board to pose and discuss your questions.
