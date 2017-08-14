The questions used in quizzes.  They were intended to reinforce the contents discussed in class via quiz administered the week following the class.  Each quiz consists of 1-7 questions totaling up to 8 points.  The quiz was administered online.  Students have 60 minutes to finish the quiz once they start the quiz.  Students can take the quiz at anytime during a 24 hour time window.

1. In Python, what is the result of the expression 3 < 5 > 2?
    - [ ] True
    - [ ] False

2. Given a Python function max to identify the maximum of two given numbers, which of the following tests will help confirm the function is correct?  Select all that apply.
    - [ ] Check max fails with two numbers
    - [ ] Check max fails with two non-numbers
    - [ ] Check max succeeds with two numbers
    - [ ] Check max succeeds with a number and a non-number

3. Which of the following statements about Python are false?  Select all that apply.
    - [ ] Python is an object-oriented language.
    - [ ] Python is a dynamically typed language.
    - [ ] Python is a statically typed language.
    - [ ] Python is a weakly typed language.
    - [ ] Python is a domain-specific language.

4. Given a string "I like python", write a python expression to extract the sub-string "like".

5. Given a string "I like python", write python expression to transform the string into "ekil".

6. Most often, testing proves the absence of bugs.
    - [ ] True
    - [ ] False

7. Identify the bugs in the following Python snippet:
```
    i = "5"
    if (i == 5)
         print(i * 3)
         print(i + 3)
```

8. Testing ensures requirements are met.
    - [ ] True
    - [ ] False

9. In comparison with dynamically typed languages, does the use of a statically typed language lower the number of validity checks performed on function parameters within the function?  Justify your answer.

10. Match the terms to their definintions.

    - *Terms*
        1. Fault
        2. Error
        3. Failure

    - *Definitions*
        1. System does not function as expected
        2. Mistake made by programmer
        3. State of the program that results due to fault

11. *checkSSN(x)* returns *True* if string x is a valid SSN and *False* otherwise.  While implementing this function in Python, what validity checks should be performed on x?  You may describe the checks in English or in Python..

12. Assume the program has one fault, which of the following statements are false about faults, errors, and failures?  Select all that apply.
    - [ ] Failure occurs when the fault is sensitized.
    - [ ] An error occurs when a fault is desensitized.
    - [ ] Failure occurs when an error propagates out of the program.
    - [ ] Since failure was not observed, no faults exist in the program.
    - [ ] Since an error occurred, the program will fail.

13. Given a library of functions (units), we should write one unit test to test the functionality of all functions.
    - [ ] True
    - [ ] False

14. Given a function _max(x, y)_ where x and y are limited to values from 1 to 25 (both inclusive), how many minimum tests do you need to prove max will always provide the right answer when given valid inputs?
    - [ ] 1250
    - [ ] 625
    - [ ] 50
    - [ ] 25

15. In homework 2 "Developer Another Python Program", what was your submission?
    - [ ] UUT
    - [ ] Test cases

16. With _assertXXX_ functions, we can perform checks that aren't possible with assert statement.
    - [ ] True
    - [ ] False

17. A function _divide_ accepts two integers arguments x and y and returns the result of x divided by y or raises _ZeroDivisionError_ if y is 0.  Using _assert_ statement, write a test case _test_divide_raises_zerodivisionerror_ that tests _divide_ raises _ZeroDivisionError_ when it should.


18. What is the common code pattern to test for absence of exceptional behavior/outcome?

19. What is the common code pattern to test for absence of exceptional behavior/outcome?

20. Of the constraints (specifications) on the parameter x to a function convert_temperature, which of them are redundant?  Select all that apply.
    - [ ] x <= 212
    - [ ] x >= 32
    - [ ] x is positive
    - [ ] (x - 30) * 5 / 9 > 0

21. In general, how does a test runner work?

22. Given a positive number of cents N, function _make_change(N)_ will return a tuple of four non-negative integers describing how to make N with the least number of coins of specific denominations; otherwise, the function raises _ValueError_ exception.  Positions 0, 1, 2, and 3 in the returned tuple correspond to 25 cents, 10 cents, 5 cents, and 1 cent denominations, respectively.  For example, _make_change(27)_ will return _(1,0,0,2)_.  Similarly, _make_change(19)_ will return _(0,1,1,4)_.

Describe four (distinct) properties of _make_change_ that we can use to test it.  To simplify your description, assume the return value of _make_change_ is stored in a variable named _ret_, i.e., `ret = make_change(N)`.


23. You are given a Python function _type_of_triangle(x, y, z)_ that detects the type of triangle based on the lengths of its sides.  The function accepts the lengths of the sides of a triangle as three  integers x, y, and z and returns either "equilateral", "isosceles", "scalene", or "not a triangle" depending on the type of triangle formed by the input.  The function assumes the input parameters are positive integers (>=0).  Further, the function guarantees to return only one of the above four strings.

Identify concrete inputs (like in example-based testing) to test this function.  Mention the expected output for each input.

24. Which of the following testing techniques is not best suited to test UUT sensitive to the structure/shape of string (input) data?
    - [ ] Equivalence Class Testing
    - [ ] Boundary Value Testing

25. 100% branch coverage implies 100% edge coverage.
    - [ ] True
    - [ ] False

26. In Python, what is the result of the expression not []?
    - [ ] False
    - [ ] True
    - [ ] Error
    - [ ] No answer text provided.

27. Given a Python function sort to sort an array of integers, which of the following tests must be performed?
    - [ ] Check if sort fails with an array containing only integers.
    - [ ] Check if sort fails with an array containing integers.
    - [ ] Check if sort does not fail with an array containing only integers.
    - [ ] Check if sort does not fail with an array containing integers

28. What is the output of executing the following code snippet?
```
    [x.upper for x in set('ham')]
```
29. Specification describes what is to be accomplished / needs to be done.
    - [ ] True
    - [ ] False

30. When testing (or as a tester), which of the following are you trying uncover?
    - [ ] Failure
    - [ ] Error
    - [ ] Fault

31. Most often, testing proves the absence of bugs.
    - [ ] True
    - [ ] False

32. System testing is development team-centric, i.e., intended to uncover as many faults before releasing the software to the user.
    - [ ] True
    - [ ] False

33. Black-box testing can deal with all exhibited behaviors.
    - [ ] True
    - [ ] False

34. Which form of testing is best suited to check if any expected behaviors are not supported?
    - [ ] Specification-based testing (Black box)
    - [ ] Code-based testing (White box)

35. Name any three aspects (properties) of software that we test.

36. What are the three necessary elements (i.e. information, abilities) required to to realize any kind of testing?
move/copy question to another bank

37. What is the expansion of UUT?

38. In homework 2 "Testing with examples", what did you submit?
    - [ ] UUT
    - [ ] Test cases

39. How will you implement _assert <expr>_ statement in Python?

40. How does test runner work?

41. How do most XUnit testing framework determine test verdict?

42. Mention one upside and one downside of using assertions in programs.

43. What is the common code pattern to test for presence of specific exceptional behavior/outcome, i.e., raises exception X?

44. PUTs are test cases.
    - [ ] True
    - [ ] False

45. Test cases are ______ of PUTs with specific ______.  (Fill in the blanks.)

46. What is a test double?

47. List three situations (reasons) that warrant the use of test doubles.

48. What is the difference between Test Stub and Test Spy?

49. Describe single-fault assumption.

50. In _______ Equivalence Class Testing, we cover all valid equivalence classes of each variable.  (Fill in the blanks.)

51. Mention a limitation of Equivalence Class Testing.

52. Which of the following testing techniques is best suited to tests involving string data?
    - [ ] Equivalence Class Testing
    - [ ] Boundary Value Testing

53. Branch coverage implies edge coverage.
    - [ ] True
    - [ ] False

54. Edge coverage implies branch coverage.
    - [ ] True
    - [ ] False

55. 100% branch coverage implies 100% node coverage.
    - [ ] True
    - [ ] False

56. 100% edge coverage implies 100% data flow coverage.
    - [ ] True
    - [ ] False

57. Identify inputs to achieve 100% edge coverage of the function below.
```
def foo(x, y, z):
    if x > y:
        print("here")
    elif y < z:
        print("there")
    if x < z:
        print("where")
    else:
        print("anywhere")
```
