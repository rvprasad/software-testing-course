import pytest
from impl import type_of_triangle

@pytest.mark.parametrize("x", range(1, 10))
def test_equilateral(x):
    ret = type_of_triangle(x, x, x)
    assert ret == "equilateral"

@pytest.mark.parametrize("x", range(1, 10))
@pytest.mark.parametrize("y", range(1, 10))
def test_isoceles(x, y):
    if y >= x + x or y == x:
        pytest.skip("Invalid test input")
    assert type_of_triangle(x, x, y) == "isoceles"
    assert type_of_triangle(x, y, x) == "isoceles"
    assert type_of_triangle(y, x, x) == "isoceles"

@pytest.mark.parametrize("x", range(1, 10))
@pytest.mark.parametrize("y", range(1, 10))
@pytest.mark.parametrize("z", range(1, 10))
def test_scalene(x, y, z):
    if x + y <= z or x + z <= y or y + z <= x or \
        x == y or y == z or x == z:
        pytest.skip("Invalid test input")
    ret = type_of_triangle(x, y, z)
    assert ret == "scalene"
    
@pytest.mark.parametrize("x", range(1, 10))
@pytest.mark.parametrize("y", range(1, 10))
@pytest.mark.parametrize("z", range(1, 10))
def test_not_a_triangle(x, y, z):
    if not (x + y <= z or x + z <= y or y + z <= x):
        pytest.skip("Invalid test input")
    ret = type_of_triangle(x, y, z)
    assert ret == "Not a triangle"
    

# parameterize this test as practice
def test_sides_greater_than_zero():
    with pytest.raises(RuntimeError):
        type_of_triangle(0, 1, 1)


# parameterize this test as practice
def test_sum_of_sides():
    ret = type_of_triangle(1, 1, 2)
    assert ret == "Not a triangle"

