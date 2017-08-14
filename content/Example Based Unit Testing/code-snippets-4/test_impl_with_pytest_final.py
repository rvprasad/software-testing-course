# execute with
#    pytest -s --html=report.html test_impl_with_pytest.py

import impl1 as impl
import pytest


class TestPhysicalInfo:

    def setup_method(self):
        self.physical_info = impl.PhysicalInfo()

    def test_set_height_valid_values_1(self):
        try:
            self.physical_info.set_height(17)
            self.physical_info.set_height(48)
            self.physical_info.set_height(72)
            self.physical_info.set_height(84)
        except ValueError as e:
            assert False

    @pytest.mark.parametrize("input", range(1, 100))
    def test_set_height_valid_values_2(self, input):
        if input < 17 or input > 84:
            pytest.skip("skipping")
        try:
            self.physical_info.set_height(input)
        except ValueError as e:
            assert False

    @pytest.mark.parametrize("input", [17, 48, 72, 84])
    def test_set_height_valid_values_3(self, input):
        try:
            self.physical_info.set_height(input)
        except ValueError as e:
            assert False

    @pytest.mark.parametrize("input", range(17, 84))
    def test_set_height_valid_values_4(self, input):
        try:
            self.physical_info.set_height(input)
        except:
            assert False
