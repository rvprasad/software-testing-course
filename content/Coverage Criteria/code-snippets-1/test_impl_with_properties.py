# py.test --cov-report=term --cov=. --cov-config=coverage.rc --cov-fail-under=100

from impl import PhysicalInfo
import pytest
import hypothesis.strategies as st
from hypothesis import given, assume

@given(st.floats() | st.text() | st.booleans())
def test_p1(v):
    t = PhysicalInfo()
    with pytest.raises(ValueError):
        t.set_height(v)

@given(st.integers())
def test_p2(v):
    assume(v < 17 or v > 84)
    t = PhysicalInfo()
    with pytest.raises(ValueError):
        t.set_height(v)

@given(st.integers())
def test_p3(v):
    assume(v >= 17 and v <= 84)
    t = PhysicalInfo()
    t.set_height(v)