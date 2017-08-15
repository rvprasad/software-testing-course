George has written a Python function `log(n, b)` that calculates the base b logarithm of n when both b and n are valid; otherwise, it raises ValueError exception.  Your task is to use property-based testing to help George test his `log` function.

Since George does not trust any exponentiation and logarithm support in Python (including any exponentiation and logarithm support you can implement as part of your tests), your tests cannot use any sort of exponentiation or logarithm support in Python to (directly or indirectly) construct the expected outcome.  So, solutions such as `assert b ** log(n, b) == n` or `assert log(n, b) == math.log(n, b)` are not allowed.  However, George is fine if you want to use exponentiation to transform/generate test data.  Also, George wants the tests to be based on varying inputs (unlike in example-based tests).

Submit your tests in a single file named *test_impl.py*.

You should assume the UUT is available in *impl.py* file.  So, in your test file, you should use appropriate import statement and name qualification to access the implementation.  Composability of your tests with our implementation is worth 1 point.

To evaluate your tests, we will use PyTest and Hypothesis.  We will execute the command pytest-2.9.x in a folder with your *test_impl.py* file and our *impl.py* files, i.e., one execution of pytest-2.9.x for each variant of our implementation.

You can use features from pytest, hypothesis, and unittest modules.

Please resolve any ambiguities about the problem by discussing them with the users (TA or instructor) via email or in-person.  When you identify ambiguities, try to describe them precisely and pose questions about them that will help remove ambiguities.

**Note: This is an unused question; hence, it may be incomplete.**
