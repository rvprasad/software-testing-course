import impl
# import correct_bst_lopsided as impl
from hypothesis import given, assume, example

import hypothesis.strategies as st
import pytest


non_none_value_generator = st.one_of(
    st.sets(st.integers(), min_size=1, max_size=15),
    st.sets(st.floats(allow_nan=False, allow_infinity=False), min_size=1,
            max_size=15),
    st.sets(st.booleans(), min_size=1, max_size=15),
    st.sets(st.text(), min_size=1, max_size=15))


def populate_tree(values):
    b = impl.BST()
    for v in values:
        b.insert(v)
    return b


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_successful_insert_of_unique_values(values):
    bst = impl.BST()
    for v in set(values):
        assert bst.insert(v)


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_unsuccessful_insert_of_existing_values(values):
    tmp1 = set(values)
    bst = populate_tree(tmp1)
    for v in tmp1:
        assert not bst.insert(v)


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
    tmp1 = list(values1)[0]
    tmp2 = list(values2)[0]
    assume(isinstance(tmp1, type(tmp2)))
    bst = populate_tree(values1)
    for v in values2:
        if not bst.search(v):
            assert not bst.delete(v)


@given(non_none_value_generator, non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_unsuccessful_search_followed_by_successful_insert(values1, values2):
    tmp1 = list(values1)[0]
    tmp2 = list(values2)[0]
    assume(isinstance(tmp1, type(tmp2)))
    bst = populate_tree(values1)
    for v in values2:
        if not bst.search(v):
            assert bst.insert(v)


@given(non_none_value_generator)
@example([])
@pytest.mark.timeout(5, method="thread")
def test_emptied_bst_should_have_none_root(values):
    bst = populate_tree(values)
    for v in values:
        bst.delete(v)
    assert bst.root is None


def test_new_bst_should_have_none_root():
    bst = impl.BST()
    assert bst.root is None


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_populated_bst_should_have_non_none_root(values):
    bst = populate_tree(values)
    assert bst.root is not None


@given(non_none_value_generator)
@pytest.mark.timeout(5, method="thread")
def test_inserted_element_exists_if_not_deleted(values):
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


def assert_ordering_property(n):
    if n:
        l = assert_ordering_property(n.left)
        assert all(i < n.key for i in l), \
            "left descendant should lesser than root"
        r = assert_ordering_property(n.right)
        assert all(n.key < i for i in r), \
            "right descendant should be greater than root"
        l |= r
        l.add(n.key)
        return l
    else:
        return set()


@given(non_none_value_generator,
    st.lists(st.integers(min_value=0, max_value=2), min_size=1))
def test_bst_is_a_bst(values, op_indices):
    bst = populate_tree(values)
    assert_tree_property(bst.root, set())
    assert_ordering_property(bst.root)
    ops = [bst.insert, bst.delete, bst.search]
    for v, o in zip(values, op_indices):
        ops[o](v)
        assert_tree_property(bst.root, set())
        assert_ordering_property(bst.root)


def test_p1():
    t = populate_tree([3,1,2,4,5])
    t.delete(1)
    assert_tree_property(t.root, set())

