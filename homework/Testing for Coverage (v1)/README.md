Jane has implemented a binary search tree (BST), and she'd like your help to write testcases to test this implementation.  Specifically, she wants the tests to test for correctness and achieve 100% line coverage of the implementation.

For this purpose, she has provided you with her BST implementation in [impl.py](impl.py).

Jane plans to modify her BST implementation.  So, she wants your tests to catch bugs that she may accidentally introduce into the implementation while tweaking it.  However, she is fine if the tests do not achieve 100% line coverage of the implementation after she has modified it.

Your task is to write tests to help Jane test her BST implementation.

Submit your tests in a single file named *test_impl.py*.

Assume the UUT is available in impl.py file.  In your test file, use appropriate import statement and name qualification to access the implementation.  Composability of your tests with our implementation is worth 1 point.

To evaluate your tests, we will use PyTest (2.9.x), Coverage (4.0.3), and Pytest-Cov (2.2.1).  We will execute the command pytest-2.9.x in a folder with your _*est_impl.py* file and our _impl.py_ files, i.e., one execution of pytest-2.9.x for each variant of our implementation.
You are not required to use Hypothesis for this assignment.

Please resolve any ambiguities about the problem (e.g., if the identified properties are simple) by discussing them with the users (TA or instructor) via email or in-person.  When you identify ambiguities, try to describe them precisely and pose questions about them that will help remove ambiguities.
