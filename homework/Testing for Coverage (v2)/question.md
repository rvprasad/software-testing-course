This homework is intended to explore code coverage and correctness in Python.

Xi has implemented a homogeneous binary search tree (BST), and she'd like your help to write test cases to test this implementation.  Specifically, she wants the tests to achieve 100% line coverage on her [current implementation](impl.py).

Xi plans to change this implementation (not the interface).  As she may accidentally introduce bugs while tweaking the implementation, she wants your tests to test for properties of any correct implementations of BST.  She is fine with your tests not achieving 100% line coverage of modified implementations.

Your task is to use property-based testing to help Xi test her implementation(s) of BST. Use features from pytest and hypothesis to implement tests.  Each test case should try to capture one property along with a one line description of the captured property in comments.  [Hint: To identify properties, consider the constraints/specifications associated with different operations/methods both in isolation and in (simple) combination.]

Submit your tests in a single file named *test_impl.py*.

To evaluate your tests, we will use PyTest with the plugins Hypothesis, Pytest-timeout, and Pytest-cov.  We will place your submission with an implementation of BST _impl.py_ in a folder and execute the following commands in the folder.
1. `pytest --cov-fail-under=100 --cov=. --cov-report=term-missing -s --cov-config=coverage.rc --timeout=180
    --timeout_method=thread test_impl.py` to evaluate your tests against the posted implementation and
2. `pytest test_impl.py` to evaluate your tests against other correct/incorrect implementations.
Make sure your test suite tests the UUT by importing it (via `import impl`) and using it appropriately (e.g., via _impl._ prefix).  Also, decorate your tests with appropriate _pytest.mark.timeout_ decorators to handle runaway behavior of implementations.  We will evaluate your tests based on their ability to identify/flag correct and incorrect BST implementations.

To expedite grading of the homework, please ensure the name of the test case function/method that tests method X has the prefix *test_X*, e.g., a test case function/method that tests a specification of BST.insert should have the prefix *test_insert*.

Please resolve any ambiguities about the problem by discussing them with the TA or the instructor ONLY via email or in-person.  When you identify ambiguities, describe them precisely and pose questions about them that will help you resolve ambiguities.  Examples of bad questions would be "what is missing in my implementation?" and "do you think my implementation is complete?"  Examples of good questions would be "Am I right in assuming sun goes around the moon?" and "when you said celestial bodies, did you mean the sun or the moon or something else?"

As mentioned in the policies of the course, collaboration is not allowed on assignments. So, do not use the discussion board to pose and discuss your questions.
