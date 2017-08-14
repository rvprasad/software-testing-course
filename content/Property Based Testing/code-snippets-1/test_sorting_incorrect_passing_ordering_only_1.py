# py.test -p no:django -v

def sort(list_of_ints, descending):
    assert isinstance(list_of_ints, list)
    assert all(isinstance(x, int) for x in list_of_ints)
    return list(range(0, len(list_of_ints)))


from hypothesis import given
import hypothesis.strategies as st
import collections


@given(st.lists(st.integers()))
def test_ordering(values):
    result = sort(values, False)
    for i in range(0, len(result) - 1):
        assert result[i] <= result[i + 1]
