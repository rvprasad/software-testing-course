This homework is intended to explore property-based testing in Python.

George has implemented a heterogeneous queue (FIFO) data structure as `Queue` class in Python. The signature of the class is given below.
```
  class Queue(object):
    def enqueue(self, v): # adds v to the back of the queue; no return value
      ....
    def dequeue(self):    # removes and returns the element at the front of the queue
      ....
    def len(self):        # returns the number of elements in the queue
      ....
      #assert isinstance(ret, int)
```

`Queue.enqueue` method will raise `ValueError` exception if the value being added is `None, Nan, Inf,` and `-Inf*`(as it does not support storing of these values).  `Queue.dequeue` method will return `None*`if the queue is empty.

Your task is to use property-based testing to help George test implementations of Queue that conform to this signature.  You don't have to test for assumptions/guarantees (denoted with assert statements in the signature).  Likewise, you can assume the values placed in the queue are comparable.

For this purpose, identify simple properties of the queue data structure and write parameterized unit tests that check Queue class for these properties using random inputs.  Use features from pytest and hypothesis to write the tests.  Each test case should capture one property along with a one line description of the captured property in comments.  [Hint: To identify properties, consider the constraints/specifications associated with various operations/methods both in isolation and in (simple) combination.]

Submit your tests in a single file named *test_impl.py*.

To evaluate your tests, we will use PyTest and Hypothesis.  We will place your submission in a folder with an implementation *impl.py* and execute `pytest test_impl.py`.  So, make sure your test suite tests the provided implementation by importing it (via `import impl`) and using it appropriately (e.g., via _impl._ prefix).   We will evaluate your tests on their ability to correctly identify/flag valid and invalid implementations of the signature/interface.

To expedite grading of the homework, please ensure the name of the test case function/method that tests method X has the prefix `test_X`, e.g., a test case function/method that tests a specification of `Queue.enqueue` should have the prefix `test_enqueue`.

Please resolve any ambiguities about the problem by discussing them with the TA or the instructor ONLY via email or in-person.  When you identify ambiguities, describe them precisely and pose questions about them that will help you resolve ambiguities.  Examples of bad questions would be "what is missing in my implementation?" and "do you think my implementation is complete?"  Examples of good questions would be "Am I right in assuming sun goes around the moon?" and "when you said celestial bodies, did you mean the sun or the moon or something else?"

As mentioned in the policies of the course, collaboration is not allowed on assignments. So, do not use the discussion board to pose and discuss your questions.
