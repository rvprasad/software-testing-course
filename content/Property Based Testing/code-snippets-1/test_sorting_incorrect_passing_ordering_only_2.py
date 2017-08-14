# py.test -p no:django -v

def sort(list_of_ints, descending):
    assert isinstance(list_of_ints, list)
    assert all(isinstance(x, int) for x in list_of_ints)
    if descending:
        return list(range(len(list_of_ints), 0, -1))
    else:
        return list(range(0, len(list_of_ints)))


from hypothesis import given
import hypothesis.strategies as st


@given(st.lists(st.integers()), st.booleans())
def test_ordering(values, descending):
    result = sort(values, descending)
    for i in range(0, len(result) - 1):
        if descending:
            assert result[i] >= result[i + 1]
        else:
            assert result[i] <= result[i + 1]
