import pytest
import hypothesis.strategies as st
from hypothesis import given, example, settings, assume

def add(x, y):
    return x+y

#@pytest.mark.parametrize("x", [1,3,4])
#@pytest.mark.parametrize("y", [1,5,4])
@given(st.integers(), st.integers())
@settings(max_examples=5)
@example(x=2,y=3)
def test_commutativity(x, y):
    assert add(x,y) == add(y,x)
    
@given(st.integers(), st.integers(), st.integers())
def test_associativity(x, y, z):
    assert add(x,add(y, z)) == add(add(x, y), z)
    
@given(st.integers())
def test_inverse(x):
    assert add(x,-x) == 0
    
@given(st.integers())
def test_identity(x):
    assert add(x,0) == x