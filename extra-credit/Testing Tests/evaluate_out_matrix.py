import re

lines = None
with open("out_matrix.txt", "r") as f:
    tmp1 = [l.strip().split(" ") for l in f.readlines()]
    lines = sorted(tmp1, key=lambda l: len(re.findall(r'F', l[0])))

num_of_tests = len(lines[0][0])
triggered_tests = set()
num_of_tests_triggered_by_impls = []
has_correct_implementation = False
for (results, impl) in lines:
    tests_triggered_by_impl = [i for (i, c) in enumerate(results) if c != '.']
    if len(tests_triggered_by_impl) == 0:
        has_correct_implementation |= True
    if set(tests_triggered_by_impl) - triggered_tests:
        print(results, impl)
        num_of_tests_triggered_by_impls.append(len(tests_triggered_by_impl))
        triggered_tests.update(tests_triggered_by_impl)
        if len(triggered_tests) == num_of_tests:
            break

print("# of tests covered by each implementation:", 
    num_of_tests_triggered_by_impls)
print("All test passing (correct) implementation {0}exists.".format(
    "" if has_correct_implementation else "does not "))

num_of_triggered_tests = len(triggered_tests)
if num_of_triggered_tests:
    untriggered_tests = num_of_tests - num_of_triggered_tests
    print("{0} implementations covered {1} test(s). {2} test(s) were not covered.".format(
        len(num_of_tests_triggered_by_impls), num_of_triggered_tests,
        untriggered_tests))
    scores = [num_of_tests - i for i in num_of_tests_triggered_by_impls]
    print("Score: {0} / 10".format(sum(scores) / num_of_triggered_tests + 
        has_correct_implementation - untriggered_tests * .9))
else:
    print("Zero test(s) were covered.")
    scores = [num_of_tests - i for i in num_of_tests_triggered_by_impls]
    print("Score: {0} / 10".format(int(has_correct_implementation)))
