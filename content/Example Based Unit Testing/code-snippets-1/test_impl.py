import pytest
import impl

def test_1():
    # give it non-string and check you get TypeError
    pass
    
def test_2():
    # give it a string and check you don't get TypeError
    pass
    
def test_checkId_raises_ValueError_for_non_numerical_values():
    # give it a string w/ alphabets and check you get ValueError
    # try:
    #     tmp1 = impl.checkId("jen123456")  
    #     assert False      
    # except ValueError:
    #     pass
    with pytest.raises(ValueError):
        impl.checkId("jen123456")
    
class TestCheckId:
    
    def test_4(self):
        # give it a string w/ numbers of length != 9 and check you get False
        pass
        
    def test_checkId_succeeds_for_valid_values(self):
        # give it a string w/ numbers of length == 9 and check you get True
        tmp1 = impl.checkId("123456789")
        assert tmp1, "What the hell"
        #if not not tmp1:
        #    raise AssertionError()
        
    def test_6(self):
        # give it a string w/ numbers and check you don't get ValueError
        try:
            impl.checkId("a234123412")
        except ValueError:
            #assert False
            pytest.fail("Boom")
