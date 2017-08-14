import pytest
import hypothesis.strategies as st
from hypothesis import given, example, settings, assume

def add(x, y):
    return x+y

#@pytest.mark.parametrize("x", [1,3,4])
#@pytest.mark.parametrize("y", [1,5,4])
@given(st.floats(allow_nan=False, allow_infinity=False), 
    st.floats(allow_nan=False, allow_infinity=False))
@settings(max_examples=5)
@example(x=2,y=3)
def test_commutativity(x, y):
    assert add(x,y) == add(y,x)

@given(st.floats(min_value=-1e6, max_value=1e6), 
    st.floats(min_value=-1e6, max_value=1e6), 
    st.floats(min_value=-1e6, max_value=1e6))
def test_associativity(x, y, z):
    assert pytest.approx(add(x,add(y, z)), 1e-6) == add(add(x, y), z)
    #assert add(x,add(y, z)) == add(add(x, y), z)
    
@given(st.floats(allow_nan=False, allow_infinity=False))
def test_inverse(x):
    assert add(x,-x) == 0
    
@given(st.floats(allow_nan=False, allow_infinity=False))
def test_identity(x):
    assert abs(add(x,0) - x) <= 1e-6