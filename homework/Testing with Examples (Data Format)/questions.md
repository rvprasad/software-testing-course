Upon Neo's request, Trinity has implemented a _PhysicalInfo_ class (in Python) to store the following information from physical examination of patients.

  - Date of examination
  - Patient's Name
  - Patient's Gender
  - Patient's Height
  - Patient's Temperature

This class provides the following setter methods.

  - set_date(string)
  - set_name(string)
  - set_gender(string)
  - set_height(int)
  - set_temperature(float)

If the values are invalid, then these setter methods will raise a _ValueError_ exception.  If not, then they will merely return. [20 points]

Your task is to help Neo by writing unit tests to test Trinity's implementation.

Submit your unit tests in a single file named *test_impl.py*.

You should assume the implementation being testing (Unit Under Test) is available in *impl.py* file.  So, in your test file, you should use appropriate import statement (e.g., `import impl`) and name qualification (e.g., `impl.PhysicalInfo)`` to access the implementation.  The composability of your tests with our implementation is worth 1 point.

To evaluate your tests, we will execute nosetests-3.4 in a folder with your *test_impl.py* file and various of our *impl.py* files, i.e., one execution of nosetests-3.4 for each variant of our implementation.

You can use either assert statements or *assertXXX* functions from nose library or unittest module in Python standard library.

Please resolve any ambiguities about the problem by discussing them with the users (TA or instructor) via email or in-person.  When you identify ambiguities, try to describe them precisely and pose questions about them that will help you remove ambiguities.
