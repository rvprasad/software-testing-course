This homework will be composed of writing two questions.

1. Implement a function `anagram_check` that accepts two strings and checks if the second string is an anagram of the first string.  All whitespace characters in the strings should be ignored.  You can assume 1) the inputs will be based only on the words in words.txt and 2) the file will exist in the same folder as your submission file.  This question is an opportunity to explore complex data types and related libraries in Python. [6 points]

2. Implement a `ShopInfo` class whose instances can store the following information about shops in US.

    - Name: string
    - Phone: int
    - Email: string
    - URL: string

    Your implementation should provide a 4-parameter constructor (parameters correspond to the above information in order) along with following getter methods for the above information.
    - get_name
    - get_phone
    - get_email
    - get_website

    Getter methods should return only valid (well-formed) values or raise `ValueError` exception.  This question is an opportunity to explore classes in Python and test-related thinking. [7 points]

Submit your implementations in a single file named *impl.py*.

Our evaluation tests will import the submitted module and access the implementations based on the above specified names.  So, the composability of your implementation with our tests is worth 2 points.

Please resolve any ambiguities about the problem by discussing them with the users (TA or instructor) via email or in-person.  When you identify ambiguities, try to describe them precisely and pose questions about them that will help remove ambiguities.
