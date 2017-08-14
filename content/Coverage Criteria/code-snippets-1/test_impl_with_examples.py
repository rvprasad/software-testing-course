# py.test --cov-report=term --cov=. --cov-config=coverage.rc --cov-fail-under=100

from impl import PhysicalInfo
import pytest

def test_e1():
    t = PhysicalInfo()
    with pytest.raises(ValueError):
        t.set_height("Michael")
    
def test_e2():
    t = PhysicalInfo()
    with pytest.raises(ValueError):
        t.set_height(100)

def test_e3():
    t = PhysicalInfo()
    t.set_height(50)
