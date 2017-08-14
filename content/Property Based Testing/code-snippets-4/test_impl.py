# py.test -k "p2"
# py.test --timeout=10 --timeout_method=thread -k "v2"

import hypothesis.strategies as st
from hypothesis import given
from impl import Stack
import pytest


strategy = st.lists(elements=(st.floats(allow_nan=False) | st.text() | 
    st.integers()))


@given(strategy)
@pytest.mark.timeout(2, 'thread')
def test_p1_v1(a):
    s = Stack()
    for x in a:
        s.push(x)
    while s.len()>0:
        s.pop()
    assert s.pop() == None
    assert s.len() == 0


@given(strategy)
def test_p1_v2(a):
    s = Stack()
    for x in a:
        s.push(x)
    for x in a:
        s.pop()
    assert s.pop() == None
    assert s.len() == 0
