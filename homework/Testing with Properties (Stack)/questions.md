George has implemented the stack (LIFO) data structure as *Stack* class in Python. The signature of the class is given below.
```
  class Stack(object):
    def push(self, v):  # pushes v on top of the stack; no return value
      ....
    def pop(self):      # pops and returns the top of the stack
      ....
    def len(self)       # returns the number of elements in the stack
      ....
```

*Stack.push* method will raise *ValueError* exception if the value being pushed is *None, Nan, and Inf*.  *Stack.pop* method will return *None* if the stack is empty.  Stack is a heterogeneous container.

Your task is to use property-based testing to help George test his Stack class.

For this purpose, identify simple properties of the stack data structure and write parameterized unit tests that check Stack class for these properties using random inputs.  Use features from pytest and hypothesis to write the tests.  Each test case should capture one property along with a one line description of the captured property in comments.  [Hint: To identify properties, consider the constraints/specifications associated with various operations/methods both in isolation and in (simple) combination.]

Submit your tests in a single file named *test_impl.py*.

You should assume the UUT is available in *impl.py* file.  So, in your test file, you should use appropriate import statement and name qualification to access the implementation.  Composability of your tests with our implementation is worth 1 point.

To evaluate your tests, we will use PyTest and Hypothesis.  We will execute the command pytest-2.9.x in a folder with your *test_impl.py* file and our *impl.py* files, i.e., one execution of pytest-2.9.x for each variant of our implementation.

Please resolve any ambiguities about the problem (e.g., if the identified properties are simple) by discussing them with the users (TA or instructor) via email or in-person.  When you identify ambiguities, try to describe them precisely and pose questions about them that will help remove ambiguities.
