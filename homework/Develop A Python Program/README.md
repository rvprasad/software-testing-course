This homework is intended to test your skill/knowledge to understand the problem, devise a solution, and program the solution in Python.

Mark Gates got this brilliant idea of constructing a network of people in which nodes represent people and edges between nodes represent relationships between people.  In this network, he wants to capture various properties about people and relationships.  Also, he wants to query the network 1) for persons using their names and 2) for all friends of friends of a person.

Your task is to develop a data structure to help Mark create a network of people.  Your implementation of the data structure should conform to/have the following signature/interface. [19 points]
```
  class Network(object):
    def __init__(self):
      # constructor
      pass
    def create_person(self):
      # create a person in the network
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
      # get a list of friends of friends of the person with given name
      pass
```
Submit your implementation in a single file named _impl.py_.

We will place your submission in a folder with our evaluation tests.  Our tests will import your module via `import impl` and access the implementation using the above signature.  Naming your files and implementation appropriately to enable this composability is worth 1 point.

Please resolve any ambiguities about the problem by discussing them with the TA or the instructor ONLY via email or in-person.  When you identify ambiguities, describe them precisely and pose questions about them that will help you resolve ambiguities.  Examples of bad questions would be "what is missing in my implementation?" and "do you think my implementation is complete?"  Examples of good questions would be "Am I right in assuming sun goes around the moon?" and "when you said celestial bodies, did you mean the sun or the moon or something else?"

As mentioned in the policies of the course, collaboration is not allowed on assignments.  So, do not use the discussion board to pose and discuss your questions.
