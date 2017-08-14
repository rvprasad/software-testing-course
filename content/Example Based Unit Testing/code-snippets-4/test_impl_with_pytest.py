# execute with
#    pytest -s --html=report.html test_impl_with_pytest.py


import pytest
import impl2 as impl

class TestPhysicalInfo:
    
    def setup_method(self):
        self.pi = impl.PhysicalInfo()
    
    def test_set_height_valid_values1(self):
        try:
            self.pi.set_height(45)
            assert self.pi.height == 45
            self.pi.set_height(17)
            assert self.pi.height == 17
            self.pi.set_height(84)
            assert self.pi.height == 84
            self.pi.set_height(72)
            assert self.pi.height == 72
        except:
            assert False
        
    def test_set_height_valid_values2(self):
        try:
            for i in [17, 45, 15, 72, 84]:
                self.pi.set_height(i)
                assert self.pi.height == i
        except:
            assert False


    @pytest.mark.parametrize("input", [17, 45, 15, 72, 84])
    def test_set_height_valid_values3(self, input):
        try:
            self.pi.set_height(input)
            assert self.pi.height == input
        except:
            assert False

    @pytest.mark.parametrize("input", range(1, 100))
    def test_set_height_valid_values_2(self, input):
        if input < 17 or input > 84:
            pytest.skip("skipping")
        try:
            self.pi.set_height(input)
        except ValueError as e:
            assert False
