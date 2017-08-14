def add2(x):  
    y = x * 2 # fault: should be x + 2
    if y == 6: # line A
        y -= 1 # line B
    return y


def search1(ints, element):
    if not (isinstance(element, int) and isinstance(ints, list) and
        all(isinstance(e, int) for e in ints)):
        raise RuntimeError()
    return element in ints

class TestSearch1:
    def test_ints_is_not_list(self):
        with pytest.raises(RuntimeError):
            search1("as", 3)  # element should be valid 
    
    def test_ints_is_not_list_of_integers(self):
        with pytest.raises(RuntimeError):
            search1(['a', 'b'], 3)  # element should be valid
    
    def test_element_is_not_integer(self):
        with pytest.raises(RuntimeError):
            search1([1,3,4], 'a')  # ints should be valid
    
    def test_element_in_ints(self): 
        assert search1([1,5,3], 3)
    
    def test_element_not_in_ints(self): 
        assert not search1([1,5,3], 4)



def search2(ints, element):
    if not (isinstance(element, int) and isinstance(ints, list) and
        all(isinstance(e, int) for e in ints)):
        raise RuntimeError()
    left = 0
    right = len(ints) - 1

    while left <= right:
        mid = (left + right) // 2

        if ints[mid] == element:
            return True
        else:
            if ints[mid] > element:
                right = mid - 1
            else:
                left = mid + 1
    return False

class TestSearch2:
    def test_ints_is_not_list(self):
        with pytest.raises(RuntimeError):
            search2("as", 3)  # element should be valid
    
    def test_ints_is_not_list_of_integers(self):
        with pytest.raises(RuntimeError):
            search2(['a', 'b'], 3)  # element should be valid
    
    def test_element_is_not_integer(self):
        with pytest.raises(RuntimeError):
            search2([1,3,4], 'a')  # ints should be valid
        
    def test_element_in_sorted_ints(self): 
        assert search2([1,3,5], 3)
    
    def test_element_not_in_sorted_ints(self): 
        assert not search2([1,3,5], 4)
    
    def test_existing_element_not_found_in_unsorted_ints(self): 
        assert not search2([1,3,5,4], 4)




import pytest
@pytest.mark.parametrize("ints", [[1,3,4,7], [7,3,10]])
@pytest.mark.parametrize("element", [3,7])
def test_element_in_ints(ints, element):
       assert search1(ints, element) 

@pytest.mark.parametrize("ints", [[1,3,4], [-7,5,10]])
def test_element_in_ints(ints):
    for i in ints:
        assert search1(ints, i)



import random
def permute(values):
    tmp1 = list(values)
    random.shuffle(tmp1)
    return tmp1

import collections
@pytest.mark.parametrize("values", [[1,3,4], [-7,5,10,11,23]])
def test_permute(values):
    tmp1 = list(values)
    result = permute(values)
    assert tmp1 == values
    tmp1 = collections.Counter(result)
    tmp2 = collections.Counter(values)
    assert tmp1 == tmp2