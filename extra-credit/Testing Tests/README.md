This exercise is intended to explore thinking about how things can go wrong.

Create correct and incorrect implementations of heterogeneous Stack data structure that conforms to the following signature and can be tested using the test suite *test_stack.py*.

```
  class Stack(object):
    def push(self, v):  # pushes v on top of the stack; no return value
      ....
    def pop(self):      # pops and returns the top of the stack
      ....
    def len(self)       # returns the number of elements in the stack
      ....
```

*Stack.push* method will raise *ValueError* exception if the value being pushed is *None, Nan,* and *Inf*.  *Stack.pop* method will return *None* if the stack is empty.

Place your implementations in a folder name impls, create a zip file of impls folder (including the python files in it), and submit this zip file.  The names of files containing correct implementations should have the prefix *impl_pass*.  The names of files containing incorrect implementations should have the prefix *impl_fail*.  The names of files containing incorrect implementation should describe the incorrectness in the implementation, e.g., *impl_fail-rename_user-returns_True_when_delete_succeeds_and_create_fails.py*.

To evaluate your tests, we will use PyTest and Hypothesis.  For each of your implementations, we will copy it as *impl.py* into a folder containing the below given test suite in a file named *test_impl.py* and execute `pytest test_stack.py` in this folder.  So, make sure your implementations work with the below given tests.  The names of test functions may be changed during evaluation.  There should be at least one unique incorrect implementation for each test case.

We will evaluate your implementations based on how they cumulatively trigger every test case with minimal redundancy.  Correct implementations should not fail any tests.  Ideally, each incorrect implementation should fail exactly one unique test case.  However, it is possible that some incorrect implementations may fail multiple tests.  So, the challenge is to keep the number of incorrect implementations as small as possible and keep the number of failing test cases for each incorrect implementation as low as possible.

Please resolve any ambiguities about the problem by discussing them with the TA or the instructor ONLY via email or in-person.  When you identify ambiguities, describe them precisely and pose questions about them that will help you resolve ambiguities.  Examples of bad questions would be "what is missing in my implementation?" and "do you think my implementation is complete?"  Examples of good questions would be "Am I right in assuming sun goes around the moon?" and "when you said celestial bodies, did you mean the sun or the moon or something else?"

As mentioned in the policies of the course, collaboration is not allowed on assignments. So, do not use the discussion board to pose and discuss your questions.
