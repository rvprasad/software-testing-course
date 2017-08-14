import hypothesis.strategies as st
from hypothesis import given, assume, example

def is_jolly_jumper(nums):
    if len(nums) == 1:
        return True
    tmp1 = [abs(nums[i-1] - nums[i]) for i in range(1, len(nums))]
    print(sorted(tmp1), list(range(1, len(nums))))
    return sorted(tmp1) == list(range(1, len(nums)))

@given(st.lists(st.integers(), min_size=1, max_size=1))
def test_one_element_sequence_is_a_jolly_jumper(values):
    assert is_jolly_jumper(values)
    
@given(st.lists(st.integers(), min_size=2, max_size=15))
@example([101, 104, 102, 103])
@example([1,4,8,6,5])
def test_jolly_jumper(values):
    tmp1 = sorted([abs(values[i-1] - values[i]) for i in range(1, len(values))])
    assert (tmp1 == list(range(1, len(values)))) == is_jolly_jumper(values)
