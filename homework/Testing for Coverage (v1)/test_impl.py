import impl
#import correct_bst_lopsided as impl
from hypothesis import given, assume

import hypothesis.strategies as st
import pytest


non_none_value_generator = st.one_of(
    st.sets(st.integers(), max_size=15), 
    st.sets(st.floats(allow_nan=False, allow_infinity=False), max_size=15),
    st.sets(st.booleans(), max_size=15), 
    st.sets(st.text(), max_size=15))


def populate_tree(values):
    b = impl.BST()
    for v in values:
        b.insert(v)
    return b


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_successful_insert_followed_by_successful_search(values):
    bst = impl.BST()
    for v in values:
        if bst.insert(v):
            assert bst.search(v)


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_successful_delete_followed_by_unsuccessful_search(values):
    bst = populate_tree(values)
    for v in values:
        if bst.delete(v):
            assert not bst.search(v)


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_successful_search_followed_by_unsuccessful_insert(values):
    bst = populate_tree(values)
    for v in values:
        if bst.search(v):
            assert not bst.insert(v)


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_successful_search_followed_by_successful_delete(values):
    bst = populate_tree(values)
    for v in values:
        if bst.search(v):
            assert bst.delete(v)


@given(non_none_value_generator, non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_unsuccessful_search_followed_by_unsuccessful_delete(values1, values2):
    assume(values1 and values2)
    tmp1 = list(values1)
    tmp2 = list(values2)
    assume(type(tmp1[0]) == type(tmp2[0]))
    bst = populate_tree(values1)
    for v in values2:
        if not bst.search(v):
            assert not bst.delete(v)


@given(non_none_value_generator, non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_unsuccessful_search_followed_by_successful_insert(values1, values2):
    assume(values1 and values2)
    tmp1 = list(values1)
    tmp2 = list(values2)
    assume(type(tmp1[0]) == type(tmp2[0]))
    bst = populate_tree(values1)
    for v in values2:
        if not bst.search(v):
            assert bst.insert(v)


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_emptied_bst_should_have_none_root(values):
    assume(values)
    bst = populate_tree(values)
    for v in values:
        bst.delete(v)
    assert bst.root == None


def test_new_bst_should_have_none_root():
    bst = impl.BST()
    assert bst.root == None


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_populated_bst_should_have_non_none_root(values):
    assume(values)
    bst = populate_tree(values)
    assert bst.root != None


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_inserted_element_exists_if_not_deleted(values):
    assume(values)
    tmp1 = list(values)
    tmp2 = tmp1[:-1]
    k = tmp1[-1]
    bst = populate_tree(tmp2)
    bst.insert(k)
    for v in tmp2:
        bst.delete(v)
    assert bst.search(k)


def assert_tree_property(n, s):
    if n:
        if n.key in s:
            assert False, "Not a tree"
        s.add(n.key)
        assert_tree_property(n.left, s)
        assert_tree_property(n.right, s)


def assert_binary_search_property(n):
    if n:
        l = assert_binary_search_property(n.left)
        assert all(i < n.key for i in l), \
            "left descendant should lesser than root"
        r = assert_binary_search_property(n.right)
        assert all(n.key < i for i in r), \
            "right descendant should be greater than root"
        l |= r
        l.add(n.key)
        return l
    else:
        return set()


@given(non_none_value_generator, 
    st.lists(st.integers(min_value=1, max_value=3)))
def test_bst_is_a_bst(values, op):
    bst = impl.BST()
    assert_tree_property(bst.root, set())
    assert_binary_search_property(bst.root)
    ops = { 1 : bst.insert, 2 : bst.delete, 3 : bst.search }
    for v in values:
        for o in op:
            ops[o](v)
            assert_tree_property(bst.root, set())
            assert_binary_search_property(bst.root)
