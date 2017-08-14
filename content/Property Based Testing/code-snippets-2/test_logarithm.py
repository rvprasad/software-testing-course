import math


def log_incorrect1(x, b):
    return 1
    
    
def log_incorrect2(x, b):
    if b == 1:
        raise ValueError()
    return 1


def log_incorrect3(x, b):
    if b == 1 or x <= 0:
        raise ValueError()
    return 1


def log_incorrect4(x, b):
    if b == 1 or x <= 0:
        raise ValueError()
    if x == 1:
        return 0
    return 1


def log(x, b):
    # return log_incorrect1(x, b)
    # return log_incorrect2(x, b)
    # return log_incorrect3(x, b)
    # return log_incorrect4(x, b)
    return math.log(x, b)


import pytest   
import hypothesis.strategies as st
from hypothesis import given, assume, example, settings

@pytest.mark.parametrize("x,b,o", [(4,2,2), (27,3,3), (81,3,4), (1024,2,10)])
def test_examples(x, b, o):
    assert log(x, b) == o


def assert_almost_equal(v1, v2, accuracy=1e6):
    assert pytest.approx(v1, accuracy) == v2


SMALLEST_FLOAT=1e-6
LARGEST_FLOAT=1e6


with settings(max_examples=500, min_satisfying_examples=500):
    
    # log of x to base x is 1
    @given(st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT))
    def test_p1(x):
        assert log(x, x) == 1
        
        
    # log of 1 at any base (except 1) is 0
    @given(st.floats(min_value=SMALLEST_FLOAT))
    def test_p2(b):
        assume(b != 1)
        assert log(1, b) == 0
    
    
    # logarithm of negative values is undefined
    @given(st.floats(max_value=0), 
        st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT))
    def test_p3(x, b):
        assume(b != 1)
        with pytest.raises(ValueError):
            log(x, b)
    
    
    # log(x, b) = n implies b ** n = x 
    @given(st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT),
        st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT))
    def test_p4(x, b):
        assume(b != 1)
        assert_almost_equal(b ** log(x, b), x)
        
        
    # log(x * y) = log(x) + log(y)
    @given(st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT),
        st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT),
        st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT))
    def test_p5(x, y, b):
        assume(b != 1)
        tmp1 = x * y
        assume(tmp1 > 0)
        tmp2 = log(tmp1, b)
        assert_almost_equal(tmp2, (log(x, b) + log(y, b)))
        
        
    # log(x / y) = log(x) - log(y)
    @given(st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT),
        st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT),   
        st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT))
    def test_p6(x, y, b):
        assume(b != 1)
        tmp1 = x / y
        assume(tmp1 > 0)
        tmp2 = log(tmp1, b)
        assert_almost_equal(tmp2, (log(x, b) - log(y, b)))
        
        
    # log(x ** y) = y * log(x)
    @given(st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT),
        st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT),
        st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT))
    def test_p7(x, y, b):
        assume(b != 1)
        try:
            tmp1 = x ** y
            assume(tmp1 > 0)
            tmp2 = log(tmp1, b)
            assert_almost_equal(tmp2, y * log(x, b))
        except OverflowError:
            print("Over flow")
            pass 
            
           
    # log(x, c) / log(b, c) = log(x, b)
    @given(st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT),
        st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT),
        st.floats(min_value=SMALLEST_FLOAT, max_value=LARGEST_FLOAT))
    def test_p8(x, b, c):
        assume(c != 1)
        tmp1 = (log(x, c) / log(b, c))
        assert_almost_equal(tmp1, log(x, b))
