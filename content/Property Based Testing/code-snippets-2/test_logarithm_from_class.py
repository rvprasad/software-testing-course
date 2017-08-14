import math
import pytest   
import hypothesis.strategies as st
from hypothesis import given, assume


def log(x, b):
    # if x < 1000:
    #     return math.log(x, b)
    # else:
    #     return 1
    return math.log(x, b)


# log of x to base x is 1
@given(st.floats(allow_nan=False, allow_infinity=False))
def test_p1(x):
    assume(x > 0 and x != 1)
    assert log(x, x) == 1


# log of 1 at any base (except 1) is 0
@given(st.floats(allow_nan=False, allow_infinity=False))
def test_p2(b):
    assume(b > 0 and b != 1)
    assert log(1, b) == 0


# logarithm of negative values is undefined
@given(st.floats(allow_nan=False, allow_infinity=False), 
    st.floats(allow_nan=False, allow_infinity=False))
def test_p3(x, b):
    assume(b > 0 and b != 1)
    assume(x < 0)
    with pytest.raises(ValueError):
        log(x, b)


# # log(x, b) = n implies b ** n = x 
# @given(st.floats(allow_nan=False, allow_infinity=False), 
#   st.floats(allow_nan=False, allow_infinity=False))
# def test_p4(x, b):
#     assume(b > 0 and b != 1)
#     assume(x > 0)
#     assert b ** log(x, b) == x
#     
#     
# log(x * y) = log(x) + log(y)
@given(st.floats(allow_nan=False, allow_infinity=False, max_value=500), 
    st.floats(allow_nan=False, allow_infinity=False, max_value=500), 
    st.floats(allow_nan=False, allow_infinity=False, max_value=500))
def test_p5(x, y, b):
    assume(b > 0 and b != 1)
    assume(x > 0)
    assume(y > 0)
    tmp1 = x * y
    assume(tmp1 > 0)
    assert abs(log(tmp1, b) - (log(x, b) + log(y, b))) < 1e-3
    

# # log(x / y) = log(x) - log(y)
# @given(st.floats(allow_nan=False, allow_infinity=False), 
#   st.floats(allow_nan=False, allow_infinity=False), 
#   st.floats(allow_nan=False, allow_infinity=False))
# def test_p6(x, y, b):
#     assume(b > 0 and b != 1)
#     assume(x > 0)
#     assume(y != 0)
#     tmp1 = x / y
#     assert log(tmp1, b) == (log(x, b) - log(y, b))
#     
# 
# # log(x ** y) = y * log(x)
# @given(st.floats(allow_nan=False, allow_infinity=False), 
#   st.floats(allow_nan=False, allow_infinity=False), 
#   st.floats(allow_nan=False, allow_infinity=False))
# def test_p7(x, y, b):
#     assume(b > 0 and b != 1)
#     assume(x > 0)
#     tmp1 = x ** y
#     assert log(tmp1, b) == y * log(x, b)
#     
