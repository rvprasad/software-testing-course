A hotel can have N guest rooms.  Upon arrival at the front desk of the hotel, each new guest is allocated an unoccupied room and given a keycard to the room.

Each room is equipped with a keycard operated lock to enter the room.  Each keycard contains two keys.  Likewise, each lock has two keys.  When a key is used to open a lock, if the first key on the card matches the first key in the lock and the second key on the card matches the second key in the lock, then the lock opens.  When the first key on the card matches the second key in the lock, the lock opens, but the lock is rekeyed with its first and second keys matching the first and second keys of the card, respectively.

The front desk maintains a record of the guest in each room.  It also maintains the set of keys that have been issued for each room.  When a new keycard is issued for a room, its first key is the last key issued for that room and its second key is a newly generated key.

For proper functioning of a hotel, some relations/interactions between guests, rooms, keycards, locks, and keys should be allowed while others should be disallowed.  For example, two guests should not be allocated the same room.  These constraints are similar to those in most hotels.

Federal Hotel Administration (FHA) has modelled the above hotel system for purposes of simulations.  FHA has created a skeletal implementation (just the interface) in Python and is available in *skeletal_impl.py*.

Lucky for you, FHA has hired you to help them with this model. Specifically, FHA wants you to do the following two tasks.

 - Implement the system.  You should implement the methods of the system such that others can use your implementation of the interface to simulate various scenarios in the above hotel system.  In other words, you should assume users will use your implementation only via the interface described in skeletal_impl.py.
 - Test the system.  You should write tests that test any implementation of the provided interface of the above system for correctness.  In other words, your tests should rely only the interface described in skeletal_impl.py.

With regards to the requirements for proper functioning of a hotel, they should be identified/elicited from FHA and then both enforced in your implementation and checked for in your tests.  It is possible that you may identify a requirement that the FHA agrees as valid but cannot be satisfied with the existing interface of the system.


## Submission Instructions

Place your implementation in a file named impl.py.  Place your tests in a file named *test_impl.py*.  If you'd like, place the requirements for proper functioning of a hotel in a file named *requirements.txt*.  If there are any details about running your tests (i.e., installation of specific pytest plugin, command line options for test execution, etc.), then describe them in detail in a file named *testing.txt*.  Submit a zip file named *submission.zip* containing the above three files.

Late submissions are not allowed in this assignment.


## Evaluation Details

To evaluate your implementation, we will use our tests with PyTest 2.9.x.

To evaluate your tests, we will use PyTest.  We will execute the command pytest-2.9.x in a folder with your *test_impl.py* file and our *impl.py* files, i.e., one execution of pytest-2.9.x for each variant of our implementation.   We will test it with an installation of PyTest that includes hypothesis and pytest-cov.

We will follow any testing related instructions in testing.txt.  If the execution fails after following your instructions, then we will evaluate the observed results.  So, keep it simple :)

The points for your implementation will be based on how well it fares with our tests.  The points for your tests will be based on how well they fare with our correct and incorrect implementations.

Please resolve any ambiguities about the problem (e.g., if the identified properties are simple) by discussing them with the users (TA or instructor) via email or in-person.  When you identify ambiguities, try to describe them precisely and pose questions about them that will help remove ambiguities.
