from hypothesis import given
import hypothesis.strategies as st
import pytest
import constructive_impl
import iterative_impl

@given(st.one_of(st.text(), st.integers(), st.floats(), st.booleans(), st.none()))
def test_invalid_input_type_constructive(values):
    with pytest.raises(ValueError):
        constructive_impl.make_power_set(values)


@given(st.one_of(st.text(), st.integers(), st.floats(), st.booleans(), st.none()))
def test_invalid_input_type_iterative(values):
    with pytest.raises(ValueError):
        next(iterative_impl.make_power_set(values))


@given(st.lists(st.integers(), max_size=10))
def test_valid_return_type_constructive(values):
    power_sets = constructive_impl.make_power_set(values)
    assert isinstance(power_sets, set)
    assert all(isinstance(s, frozenset) for s in power_sets)


@given(st.lists(st.integers(), max_size=10))
def test_valid_return_type_iterative(values):
    power_sets = iterative_impl.make_power_set(values)
    tmp1 = []
    for s in power_sets:
        assert isinstance(s, frozenset)
        tmp1.append(s)
    assert len(tmp1) == len(set(tmp1))


@given(st.lists(st.integers(), max_size=10))
def test_valid_return_type_constructive(values):
    power_sets = constructive_impl.make_power_set(values)
    assert len(power_sets) == 2 ** len(set(values))


@given(st.lists(st.integers(), max_size=10))
def test_valid_return_type_iterative(values):
    power_sets = iterative_impl.make_power_set(values)
    assert sum(1 for s in power_sets) == 2 ** len(set(values))


def check_all_subsets_contain_only_given_values(power_sets, values):
    for s in power_sets:
        assert s.issubset(values)


@given(st.lists(st.integers(), max_size=10))
def test_all_subsets_contain_only_given_values_constructive(values):
    power_sets = constructive_impl.make_power_set(values)
    check_all_subsets_contain_only_given_values(power_sets, values)


@given(st.lists(st.integers(), max_size=10))
def test_all_subsets_contain_only_given_values_iterative(values):
    power_sets = iterative_impl.make_power_set(values)
    check_all_subsets_contain_only_given_values(power_sets, values)
    

#def check_every_element_is_in_required_number_of_subsets(power_sets, values):
#    tmp1 = frozenset(values)
#    count = {v:0 for v in tmp1}
#    for s in power_sets:
#        for i in s:
#            count[i] += 1
#    if values:
#        limit = 2 ** (len(tmp1) - 1)
#        assert all(v == limit for v in count.values())
#    else: # when input is an empty list
#        assert len(count) == 0 and len(power_sets) == 1
#    
#
#@given(st.lists(st.integers(), max_size=10))
#def test_every_element_is_in_required_number_of_subsets_constructive(values):
#    power_sets = constructive_impl.make_power_set(values)
#    check_every_element_is_in_required_number_of_subsets(power_sets, values)
#    
#
#@given(st.lists(st.integers(), max_size=10))
#def test_every_element_is_in_required_number_of_subsets_iterative(values):
#    power_sets = list(iterative_impl.make_power_set(values))
#    check_every_element_is_in_required_number_of_subsets(power_sets, values)
