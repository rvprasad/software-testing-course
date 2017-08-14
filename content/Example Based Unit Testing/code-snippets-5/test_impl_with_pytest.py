# execute with
#    pytest -s --html=report.html test_impl_with_pytest.py


import pytest
import impl


class TestPhysicalInfo:

    def setup_method(self):
        self.pi = impl.PhysicalInfo()

    def test_set_date_invalid_date_1(self):
        with pytest.raises(ValueError):
            self.pi.set_date("13-23-2016")
        with pytest.raises(ValueError):
            self.pi.set_date("02-29-2017")
        with pytest.raises(ValueError):
            self.pi.set_date("02-31-2012")
        with pytest.raises(ValueError):
            self.pi.set_date("12-23-16")
        with pytest.raises(ValueError):
            self.pi.set_date("1-32-1996")
            
    @pytest.mark.parametrize("input", ["13-23-2016", "02-29-2017", "02-31-2012",
                                        "12-23-16", "1-32-1996"])
    def test_set_date_invalid_date_2(self, input):
        with pytest.raises(ValueError):
            self.pi.set_date(input)
            
    
    @pytest.mark.parametrize("month", ["13", "02", "02", 12, 1])
    @pytest.mark.parametrize("day", [23, 29, 31, 23, 32])
    @pytest.mark.parametrize("year", [2016, 2017, 2012, 16, 1996])
    def test_set_date_invalid_date_3(self, month, day, year):
        date = "{0}-{1}-{2}".format(month, day, year)
        with pytest.raises(ValueError):
            self.pi.set_date(date)