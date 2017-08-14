# py.test -p no:django -v

def sort(list_of_ints, descending):
    assert isinstance(list_of_ints, list)
    assert all(isinstance(x, int) for x in list_of_ints)
    if descending:
        return list_of_ints
    else:
        return [4, 2, 3]


from hypothesis import given
import hypothesis.strategies as st
import collections

@given(st.lists(st.integers()))
def test_presence_with_freq(values):
    result = sort(values, True)
    tmp1 = collections.Counter(values)
    tmp2 = collections.Counter(result)
    assert tmp1 == tmp2
    
    
