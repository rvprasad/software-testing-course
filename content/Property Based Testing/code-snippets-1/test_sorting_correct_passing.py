# py.test -p no:django -v 

def sort(list_of_ints, descending):
    assert isinstance(list_of_ints, list)
    assert all(isinstance(x, int) for x in list_of_ints)
    result = sorted(list_of_ints, reverse=descending)
    return result


from hypothesis import given
import hypothesis.strategies as st
import collections


@given(st.lists(st.integers()), st.booleans())
def test_ordering(values, descending):
    result = sort(values, descending)
    for i in range(0, len(result) - 1):
        if descending:
            assert result[i] >= result[i + 1]
        else:
            assert result[i] <= result[i + 1]


@given(st.lists(st.integers()), st.booleans())
def test_presence_with_freq(values, descending):
    result = sort(values, descending)
    tmp1 = collections.Counter(values)
    tmp2 = collections.Counter(result)
    assert tmp1 == tmp2
