import math


def log(x, b):
    return math.log(x, b)

    
import pytest


@pytest.mark.parametrize("x,b,o", [(4,2,2), (27,3,3), (81,3,4), (1024,2,10)])
def test_examples(x, b, o):
    assert log(x, b) == o
