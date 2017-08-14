# install hypothesis, pytest, and pytest-cov
# into python using pip command

# Execute using
#   py.test -v test_stack.py


from hypothesis import given, assume, example
import hypothesis.strategies as st
import pytest
from impl import Stack


def populate_stack(values):
    stack = Stack()
    for v in values:
        stack.push(v)
    return stack


non_none_value_generator = st.one_of(st.integers(),
                                     st.floats(allow_nan=False,
                                               allow_infinity=False),
                                     st.booleans(), st.text())


# p1: after pushing v1, v2, v3 .. vn, popping will return vn, .. v3, v2, v1
@given(st.lists(non_none_value_generator))
def test_p1_lifo(values):
    stack = Stack()
    for v in values:
        stack.push(v)
    for v in reversed(values):
        assert stack.pop() == v


# p2: successful push will increment length by 1
@given(st.lists(non_none_value_generator), non_none_value_generator)
def test_p2_successful_push_increments_len_by_one(values, v):
    stack = populate_stack(values)
    tmp1 = stack.len()
    stack.push(v)
    assert stack.len() == tmp1 + 1


# p3: unsuccessful push will not affect length
@given(st.lists(non_none_value_generator))
def test_p3_unsuccessful_push_will_not_affect_length(values):
    stack = populate_stack(values)
    tmp1 = stack.len()
    with pytest.raises(ValueError):
        stack.push(None)
    with pytest.raises(ValueError):
        stack.push(float('Nan'))
    with pytest.raises(ValueError):
        stack.push(float('Inf'))
    assert stack.len() == tmp1


# p4: unsuccessful push raises ValueError
def test_p4_pushing_None_raises_ValueError():
    s = Stack()
    with pytest.raises(ValueError):
        s.push(None)


# p5: successful pop will decrement length by 1
@given(st.lists(non_none_value_generator))
def test_p5_successful_pop_decrements_len_by_one(values):
    stack = populate_stack(values)
    tmp1 = stack.len()
    if stack.pop() is not None:
        assert stack.len() == tmp1 - 1


# p6: unsuccessful pop will not affect length
@given(st.lists(non_none_value_generator))
def test_p6_unsuccessful_pop_will_not_affect_length(values):
    stack = populate_stack(values)
    tmp1 = stack.len()
    if stack.pop() is None:
        assert stack.len() == tmp1


# p7: length is zero for empty stack
@given(st.lists(non_none_value_generator))
@example([])
def test_p7_length_is_zero_for_empty_stack(values):
    stack = populate_stack(values)
    for i in range(0, len(values)):
        stack.pop()
    assert stack.len() == 0


# p8: pop returns None for empty stack
@given(st.lists(non_none_value_generator))
@example([])
def test_p8_pop_returns_none_for_empty_stack(values):
    stack = populate_stack(values)
    for i in range(0, len(values)):
        stack.pop()
    assert stack.pop() is None


# p9: len is side effect free
@given(st.lists(non_none_value_generator))
def test_p9_len_is_side_effect_free(values):
    stack = Stack()
    for v in values:
        stack.push(v)
    stack.len()
    for v in reversed(values):
        assert stack.pop() == v
    assert stack.pop() is None


# p10: push does not return value
@given(st.lists(non_none_value_generator))
def test_p10_push_does_not_return_value(values):
    stack = Stack()
    for v in values:
        assert stack.push(v) is None
