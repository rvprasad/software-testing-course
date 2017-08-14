# execute with
#    pytest -s --html=report.html test_impl_with_pytest.py


import impl
import pytest


class TestPhysicalInfo:

    def setup_method(self):
        self.physical_info = impl.PhysicalInfo()

    def test_set_date_invalid_day_1(self):
        with pytest.raises(ValueError):
            self.physical_info.set_date("02-30-2016")
        with pytest.raises(ValueError):
            self.physical_info.set_date("02-29-2015")
        with pytest.raises(ValueError):
            self.physical_info.set_date("01-32-2006")
        with pytest.raises(ValueError):
            self.physical_info.set_date("04-31-2001")
        with pytest.raises(ValueError):
            self.physical_info.set_date("02-29-1900")

    # This PUT generates 5 example-based test cases.
    @pytest.mark.parametrize("input", ["02-30-2016", "02-29-2015",
                                       "01-32-2006", "04-31-2001",
                                       "02-29-1900"])
    def test_set_date_invalid_day_2(self, input):
        with pytest.raises(ValueError) as excinfo:
            self.physical_info.set_date(input)

    # While the purpose of this test is the same as that of
    # test_set_date_invalid_day_2, it may not have the same effect.
    # This is a test case that performs 5 checks.
    # test_set_date_invalid_day_2 generates 5 test cases that perform 1 check.
    def test_set_date_invalid_day_3(self):
        for i in ["02-30-2016", "02-29-2015", "01-32-2006", "04-31-2001",
                  "02-29-1900"]:
            with pytest.raises(ValueError) as excinfo:
                self.physical_info.set_date(i)

    # Unlike the test cases generated in test_set_date_invalid_day_2,
    # some of the test cases generated from this PUT are "broken".
    @pytest.mark.parametrize("day", ["30", "29", "32", "31"])
    @pytest.mark.parametrize("month", ["02", "01", "04"])
    @pytest.mark.parametrize("year", ["2016", "2015", "2006", "2001", "1900"])
    def test_set_date_invalid_day_4(self, day, month, year):
        with pytest.raises(ValueError) as excinfo:
            self.physical_info.set_date("{0}-{1}-{2}".format(month, day, year))
