# install hypothesis, pytest, and pytest-cov
# into python using pip command

# Execute using
#   py.test -p no:django -v test_stack.py

from hypothesis import given, assume, example
import hypothesis.strategies as st 
import pytest
from impl import Stack
#from correct_stack import Stack
#from incorrect_stack_p1 import Stack


def populate_stack(values):
    stack=Stack()
    for v in values:
        stack.push(v)
    return stack

non_none_value_generator = st.one_of(st.integers(), 
    st.floats(allow_nan=False, allow_infinity=False),
    st.booleans(), st.text())


# # p1: length increases by 1 after a successful push 
# @given(st.lists(st.integers() | st.text()), st.integers())
# def test_p1_successful_push_increases_len_by_one(values, v):
#     stack = populate_stack(values)
#     tmp1 = stack.len()
#     stack.push(v)
#     assert stack.len() == (tmp1 + 1)
# 
# 
# # p2: length does not change after an unsuccessful push
# @given(st.lists(st.integers() | st.none()))
# def test_p2_unsuccessful_push_does_not_affect_length(values):
#     assume(None in values)
#     stack = Stack()
#     tmp1 = 0
#     try:
#         for v in values:
#             tmp1 = stack.len()
#             stack.push(v)
#         assert False
#     except ValueError:
#         assert stack.len() == tmp1
# 
# 
# # # p3: length decreases by 1 after a non-None returning pop
# # @given(st.lists(st.integers() | st.text()))
# # def test_p3_non_none_returning_pop_decreases_len_by_one(values):
# #     stack = populate_stack(values)
# #     tmp1 = stack.len()
# #     if stack.pop() != None:
# #         assert stack.len() == (tmp1 - 1)
# # 
# # 
# # # p4: length does not change after a None returning pop
# # @given(st.lists(st.integers() | st.text()), st.integers(1, 100))
# # def test_p4_none_returning_pop_does_not_affect_length(values, n):
# #     stack = populate_stack(values)
# #     for i in range(0, len(values) + n):
# #         tmp1 = stack.len()
# #         if stack.pop() == None:
# #             assert stack.len() == tmp1
# #             break
# #     else:
# #         assert False
# # 
# # 
# # p5: popping an empty stack returns None
# # @given(st.lists(st.integers() | st.text()))
# # @example([])
# # def test_p5_popping_empty_stack_returns_none(values):
# #     stack = populate_stack(values)
# #     for i in range(0, len(values)):
# #         stack.pop()
# #     assert stack.pop() == None
# # 
# # 
# # p6: pop returns the tos
# @given(st.lists(st.integers() | st.text()), st.integers())
# def test_p6_pop_returns_tos(values, v):
#     stack = populate_stack(values)
#     stack.push(v)
#     assert stack.pop() == v
# 
# 
# # p7: pop affects only the tos
# @given(st.lists(st.integers() | st.text()))
# def test_p7_pop_only_changes_tos(values):
#     stack = populate_stack(values)
#     stack.pop()
#     for v in list(reversed(values))[1:]:
#         assert stack.pop() == v
#     assert stack.pop() == None
# 
# 
# # # p8: push affects only the tos
# # @given(st.lists(st.integers() | st.text()), st.integers())
# # def test_p8_push_only_changes_tos(values, v):
# #     stack = populate_stack(values)
# #     stack.push(v)
# #     values.append(v)
# #     for t in reversed(values):
# #         assert stack.pop() == t
# #     assert stack.pop() == None
# # 
# # 
# # # p9: push raises ValueError with None argument
# # @given(st.lists(st.integers() | st.text()))
# # def test_p9_push_does_not_support_None(values):
# #     stack = populate_stack(values)
# #     with pytest.raises(ValueError):
# #         stack.push(None)
# # 
# # 
# # # p10: len is idempotent
# # @given(st.lists(st.integers() | st.text()))
# # def test_p10_len_is_idempotent(values):
# #     stack = Stack()
# #     for v in values:
# #         stack.push(v)
# #     stack.len()
# #     for v in reversed(values):
# #         assert stack.pop() == v
# #     assert stack.pop() == None
# # 
# # 
# # # p11: pop returns None implies length is zero
# # @given(st.lists(st.integers()), st.integers(1, 100))
# # def test_p11_pop_returns_none_implies_len_is_zero(values, n):
# #     stack = populate_stack(values)
# #     for i in range(0, len(values) + n):
# #         tmp1 = stack.pop()
# #         if tmp1 == None:
# #             assert stack.len() == 0
# #             break
# #     else:
# #         assert False
# # 
# # 
# # p12: length is zero implies pop will return None 
# @given(st.lists(st.integers()), st.integers(1, 100))
# def test_p12_len_is_zero_implies_pop_returns_none(values, n):
#     stack = populate_stack(values)
#     for i in range(0, len(values) + n):
#         stack.pop()
#         if stack.len() == 0:
#             assert stack.pop() == None
#             break
#     else:
#         assert False
# 
# 
# # # p13: length returns 0 or positive number
# # @given(st.lists(st.integers()), st.integers(0, 100))
# # def test_p13_len_returns_zero_or_pos_num(values, n):
# #     stack = populate_stack(values)
# #     for i in range(0, n):
# #         stack.pop()
# #     assert stack.len() >= 0
# #     


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
@given(non_none_value_generator)
def test_p4_pushing_None_raises_ValueError(v):
    stack = Stack()
    if v == None:
        with pytest.raises(ValueError):
            s.push(v)


# p5: successful pop will decrement length by 1
@given(st.lists(non_none_value_generator))
def test_p5_successful_pop_decrements_len_by_one(values):
    stack = populate_stack(values)
    tmp1 = stack.len()
    if stack.pop() != None:
        assert stack.len() == tmp1 - 1

# p6: unsuccessful pop will not affect length
@given(st.lists(non_none_value_generator))
def test_p6_unsuccessful_pop_will_not_affect_length(values):
    stack = populate_stack(values)
    tmp1 = stack.len()
    if stack.pop() == None:
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
    assert stack.pop() == None
    
# p9: len is side effect free
@given(st.lists(non_none_value_generator))
def test_p9_len_is_side_effect_free(values):
    stack = Stack()
    for v in values:
        stack.push(v)
    stack.len()
    for v in reversed(values):
        assert stack.pop() == v
    assert stack.pop() == None


# p10: push does not return value
@given(st.lists(non_none_value_generator))
def test_p10_push_does_not_return_value(values):
    stack = Stack()
    for v in values:
        assert stack.push(v) == None
