DENOMINATIONS = (25, 10, 5, 1)

def make_change(n):
    if n < 0:
        raise ValueError()
    d_25 = n // DENOMINATIONS[0]
    tmp1 = n - d_25 * DENOMINATIONS[0]
    d_10 = tmp1 // DENOMINATIONS[1]
    tmp2 = tmp1 - d_10 * DENOMINATIONS[1]
    d_5 = tmp2 // DENOMINATIONS[2]
    d_1 = tmp2 - d_5 * DENOMINATIONS[2]
    return (d_25, d_10, d_5, d_1)


import hypothesis.strategies as st
from hypothesis import given, example
import pytest


# invalid values
@given(st.integers(max_value=-1))
def test_p1(n):
    with pytest.raises(ValueError):
        make_change(n)


# made change amounts to the given value n
@given(st.integers(min_value=0))
def test_p2(n):
    r = make_change(n)
    assert r[0] * DENOMINATIONS[0] + r[1] * DENOMINATIONS[1] + \
        r[2] * DENOMINATIONS[2] + r[3] == n


# made change is least
@given(st.integers(min_value=0, max_value=200))
def test_p3(n):
    r = make_change(n)
    assert n - r[0] * DENOMINATIONS[0] < DENOMINATIONS[0]
    assert r[1] < 3
    assert r[2] < 2
    assert r[3] < 5


# output has valid structure -- a quadruple of ints
@given(st.integers(min_value=0))
def test_p4(n):
    r = make_change(n)
    assert isinstance(r, tuple) and len(r) == 4 and \
        all(isinstance(x, int) for x in r) and 
        all(x >= 0 for x in r)
