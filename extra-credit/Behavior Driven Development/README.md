In this assignment, you will explore some aspects of behavior-driven development in Python.

It is January 14th, 2017, and Mark Gates has asked you to code up a data structure to represent people (as nodes) and relations between people (as edges).  Instead of rushing to code up the data structure in Python (as you did in homework 1), you have decided to use BDD this time.  So, you will specify the features of the data structure desired of any implementation that conforms to the below interface.

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

Your task is to specify the following feature as done in BDD.

  1. Query friends of friends of a person in the network.

You should consider both correct and incorrect uses of the feature and the corresponding expected outcomes when describing (specifying the behavior of) the features. Since BDD is customer friendly/facing, do not consider incorrect uses of features involving arguments of incorrect types. As for other incorrect uses, you will need to capture it in a customer friendly manner in the feature description and handle it appropriately in the step definition. You can use other methods of the data structure assuming they work (correctly) as specified. [10 points]

Place your .feature files in solution/features folder, your steps files in solution/features/steps folder, create a zip file of solution folder (including all .feature and steps files), and submit this zip file.

To evaluate your solution, we will use PyTest and behave.  We will unzip your submission file, copy an implementation as *impl.py* into solution/src folder, and execute `behave` in solution folder.  We will evaluate your features and steps on how best they can flag incorrect implementations and not flag correct implementations.

Please resolve any ambiguities about the problem by discussing them with the TA or the instructor ONLY via email or in-person.  When you identify ambiguities, describe them precisely and pose questions about them that will help you resolve ambiguities.  Examples of bad questions would be "what is missing in my implementation?" and "do you think my implementation is complete?"  Examples of good questions would be "Am I right in assuming sun goes around the moon?" and "when you said celestial bodies, did you mean the sun or the moon or something else?"

As mentioned in the policies of the course, collaboration is not allowed on assignments. So, do not use the discussion board to pose and discuss your questions.
