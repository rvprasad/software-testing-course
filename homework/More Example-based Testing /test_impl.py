from helpers import *
import impl
#import correct_impl as impl

import hypothesis.strategies as st
from hypothesis import given, assume, example, settings
import pytest


@given(st.integers(min_value=1, max_value=10).flatmap(
    lambda n: st.lists(
        st.tuples(
            st.integers(min_value=0, max_value=n), 
            st.integers(min_value=0, max_value=n), 
            st.integers(min_value=1, max_value=50)), 
        min_size=n, max_size=n)))
def test_disonnected(edges):
    assume(not has_multiple_edges_between_nodes(edges) and 
        is_disconnected(edges) and 
        not has_loops(edges))
    with pytest.raises(ValueError) as t:
        impl.all_pairs_shortest_paths(edges)


@given(st.integers(min_value=1, max_value=10).flatmap(
    lambda n: st.lists(
        st.tuples(
            st.integers(min_value=0, max_value=n), 
            st.integers(min_value=0, max_value=n), 
            st.integers(min_value=-1, max_value=50)), 
        min_size=n, max_size=n)))
def test_non_positive_weights(edges):
    assume(not has_multiple_edges_between_nodes(edges) and 
        not is_disconnected(edges) and 
        not has_loops(edges) and 
        any(e[2] < 1 for e in edges))
    with pytest.raises(ValueError):
        impl.all_pairs_shortest_paths(edges)

        
@given(st.integers(min_value=1, max_value=10).flatmap(
    lambda n: st.lists(
        st.tuples(
            st.integers(min_value=0, max_value=n//2), 
            st.integers(min_value=0, max_value=n//2), 
            st.integers(min_value=1, max_value=50)), 
        min_size=n, max_size=n)))
def test_multiple_edges_between_nodes(edges):
    assume(has_multiple_edges_between_nodes(edges) and 
        not is_disconnected(edges) and 
        not has_loops(edges))
    with pytest.raises(ValueError):
        impl.all_pairs_shortest_paths(edges)
        

@given(st.integers(min_value=1, max_value=10).flatmap(
    lambda n: st.lists(
        st.tuples(
            st.integers(min_value=0, max_value=n*n), 
            st.integers(min_value=0, max_value=n*n), 
            st.integers(min_value=1, max_value=50)), 
        min_size=n, max_size=n)).map(
    lambda edges: edges + [(edges[0][0], edges[0][0], edges[0][2])]))
def test_loops(edges):
    assume(not has_multiple_edges_between_nodes(edges) and 
        not is_disconnected(edges))
    with pytest.raises(ValueError):
        impl.all_pairs_shortest_paths(edges)


def test_empty_graph():
    assert len(impl.all_pairs_shortest_paths([])) == 0


def test_invalid_type():
    with pytest.raises(ValueError):
        impl.all_pairs_shortest_paths({1 : 3})


def test_invalid_weights():
    with pytest.raises(ValueError):
        impl.all_pairs_shortest_paths([(1, 2, 'a')])


def is_valid_edges(edges):
    return not (has_loops(edges) or 
        has_multiple_edges_between_nodes(edges) or
        is_disconnected(edges))


valid_edges_generator = st.integers(min_value=0, max_value=10).flatmap(
    lambda n: st.lists(
        st.tuples(
            st.integers(min_value=0, max_value=n), 
            st.integers(min_value=0, max_value=n), 
            st.integers(min_value=1, max_value=50)), 
        min_size=n, max_size=n)).filter(
    lambda edges: is_valid_edges(edges))


@given(valid_edges_generator)
def test_valid_number_of_path_lengths(edges):
    lengths = impl.all_pairs_shortest_paths(edges)
    if not edges:
        assert len(lengths) == 0
    else:
        n = len(get_nodes(edges))
        assert len(lengths) == n * (n-1) / 2


@given(valid_edges_generator)
def test_non_zero_lengths(edges):
    assume(edges)
    lengths = impl.all_pairs_shortest_paths(edges)
    assert all(l[2] > 0 for l in lengths)


@given(valid_edges_generator)
def test_valid_length_type(edges):
    assume(edges)
    lengths = impl.all_pairs_shortest_paths(edges)
    assert all(type(l[2]) == int for l in lengths)


@given(valid_edges_generator)
def test_valid_nodes(edges):
    assume(edges)
    nodes = get_nodes(edges)
    lengths = impl.all_pairs_shortest_paths(edges)
    assert nodes == get_nodes(lengths)


@given(valid_edges_generator)
def test_no_smaller_than_the_length_can_be(edges):
    assume(edges)
    lengths = impl.all_pairs_shortest_paths(edges)
    node_2_min_length = {n:100 for n in get_nodes(edges)}
    for n1, n2, d in edges:
        node_2_min_length[n1] = min(node_2_min_length[n1], d)
        node_2_min_length[n2] = min(node_2_min_length[n2], d)
    edge_2_weight = {(e[0], e[1]):e[2] for e in edges}
    edge_2_weight.update({(e[1], e[0]):e[2] for e in edges})
    for n1, n2, d in lengths:
        if (n1, n2) in edge_2_weight:
            if d < edge_2_weight[(n1, n2)]:
                assert node_2_min_length[n1] < d, (n1, n2)
                assert node_2_min_length[n2] < d, (n1, n2)
            else:
                assert d == edge_2_weight[(n1, n2)], (n1, n2)
        else:
            assert node_2_min_length[n1] <= d, (n1, n2)
            assert node_2_min_length[n2] <= d, (n1, n2)


@given(valid_edges_generator)
def test_no_larger_than_the_length_can_be(edges):
    assume(edges)
    lengths = impl.all_pairs_shortest_paths(edges)
    max_length = sum(e[2] for e in edges)
    assert all(l[2] <= max_length for l in lengths), lengths


@given(valid_edges_generator)
def test_shortest_path(edges):
    assume(edges)
    lengths = impl.all_pairs_shortest_paths(edges)
    nodes = get_nodes(edges)
    dist = {(n, n):0 for n in nodes}
    dist.update({(e[0], e[1]):e[2] for e in lengths})
    dist.update({(e[1], e[0]):e[2] for e in lengths})
    for n1, n2, d in lengths:
        assert min(dist[(n1, n)] + dist[(n, n2)] for n in nodes) == d



