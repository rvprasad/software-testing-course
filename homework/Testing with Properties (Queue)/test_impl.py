# install hypothesis, pytest, and pytest-cov
# into python using pip command

# Execute using
#   py.test -v test_queue.py


from hypothesis import given, assume, example
import hypothesis.strategies as st
import pytest
import math
from impl import Queue


def populate_queue(values):
    queue = Queue()
    for v in values:
        queue.enqueue(v)
    return queue

non_none_value_generator = st.one_of(st.integers(),
    st.floats(allow_nan=False, allow_infinity=False),
    st.booleans(), st.text(), st.lists(st.booleans()), 
    st.tuples(st.integers(), st.booleans()),
    st.sets(st.integers()), st.dictionaries(st.integers(), st.text()))


# p1: after successfully enqueueing v1, v2, v3 .. vn, 
#     successful dequeuing will return vn, ... v3, v2, v1
@given(st.lists(non_none_value_generator), st.lists(non_none_value_generator))
@example([], st.lists(non_none_value_generator).example())
def test_p1_lifo(init_values, values):
    queue = populate_queue(init_values)
    for v in values:
        queue.enqueue(v)
    for v in init_values:
        queue.dequeue()
    for v in values:
        assert queue.dequeue() == v


# p2: successful enqueue will increment length by 1
@given(st.lists(non_none_value_generator), non_none_value_generator)
def test_p2_successful_enqueue_increments_len_by_one(values, v):
    queue = populate_queue(values)
    tmp1 = queue.len()
    queue.enqueue(v)
    assert queue.len() == tmp1 + 1


# p3: unsuccessful enqueue will not affect length
@given(st.lists(non_none_value_generator))
def test_p3_unsuccessful_enqueue_will_not_affect_length(values):
    queue = populate_queue(values)
    tmp1 = queue.len()
    with pytest.raises(ValueError):
        queue.enqueue(None)
    with pytest.raises(ValueError):
        queue.enqueue(float('Nan'))
    with pytest.raises(ValueError):
        queue.enqueue(float('Inf'))
    assert queue.len() == tmp1


# p4: unsuccessful enqueue raises ValueError
def test_p4_enqueueing_None_raises_ValueError():
    queue = Queue()
    with pytest.raises(ValueError):
        queue.enqueue(None)


# p5: successful dequeue will decrement length by 1
@given(st.lists(non_none_value_generator))
def test_p5_successful_dequeue_decrements_len_by_one(values):
    queue = populate_queue(values)
    tmp1 = queue.len()
    if queue.dequeue() is not None:
        assert queue.len() == tmp1 - 1


# p6: unsuccessful dequeue will not affect length
@given(st.lists(non_none_value_generator))
def test_p6_unsuccessful_dequeue_will_not_affect_length(values):
    queue = populate_queue(values)
    tmp1 = queue.len()
    if queue.dequeue() is None:
        assert queue.len() == tmp1


# p7: length is zero for empty queue
@given(st.lists(non_none_value_generator))
@example([])
def test_p7_length_is_zero_for_empty_queue(values):
    queue = populate_queue(values)
    for i in range(0, len(values)):
        queue.dequeue()
    assert queue.len() == 0


# p8: dequeue returns None for empty queue
@given(st.lists(non_none_value_generator))
@example([])
def test_p8_dequeue_returns_none_for_empty_queue(values):
    queue = populate_queue(values)
    for i in range(0, len(values)):
        queue.dequeue()
    assert queue.dequeue() is None


# p9: len is side effect free
@given(st.lists(non_none_value_generator))
def test_p9_len_is_side_effect_free(values):
    queue = Queue()
    for v in values:
        queue.enqueue(v)
    queue.len()
    for v in values:
        assert queue.dequeue() == v
    assert queue.dequeue() is None


# p10: enqueue does not return value
@given(st.lists(non_none_value_generator))
def test_p10_enqueue_does_not_return_value(values):
    queue = Queue()
    for v in values:
        assert queue.enqueue(v) is None


# p11: enqueue should exhibit abnormal behavior for invalid inputs
@pytest.mark.parametrize('values', [[None], [math.inf], [-math.inf], 
    [math.nan]])
def test_p11_enqueue_exhibits_abnormal_behavior_for_invalid_inputs(values):
    queue = Queue()
    with pytest.raises(ValueError):
        populate_queue(values)
