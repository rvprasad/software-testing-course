import impl
import unittest
import nose.tools as nt

def my_assert(exception, method, arg):
    try:
        method(arg)
        assert False
    except exception:
        assert True
    except:
        assert False

class TestPhysicalInfo(unittest.TestCase):
    
    def setUp(self):
        self.physical_info = impl.PhysicalInfo()
        
    def test_set_valid_values(self):
        try:
            self.physical_info.set_date("01-02-2016")
            self.physical_info.set_date("11-09-1992")
            self.physical_info.set_name("Jane")
            self.physical_info.set_gender("F")
            self.physical_info.set_height(54)
            self.physical_info.set_temperature(98.6)
        except:
            assert False
            
    def test_set_name_valid_values(self):
        try:
            self.physical_info.set_name("John Doe")
            self.physical_info.set_name("John-doe")
            self.physical_info.set_name("2Pac")
        except:
            assert False
            
    def test_set_name_non_string(self):
        my_assert(ValueError, self.physical_info.set_name, 1234)
        my_assert(ValueError, self.physical_info.set_name, 1234.3)
        
    def test_set_name_none(self):
        my_assert(ValueError, self.physical_info.set_name, None)
        
    def test_set_name_no_letter_name(self):
        my_assert(ValueError, self.physical_info.set_name, "1234")
        
    def test_set_name_invalid_character_name(self):
        my_assert(ValueError, self.physical_info.set_name, "2Pac#")
        
    def test_set_name_one_character_long_name(self):
        my_assert(ValueError, self.physical_info.set_name, "a")
        my_assert(ValueError, self.physical_info.set_name, "a ")
        my_assert(ValueError, self.physical_info.set_name, "a-")
        
    def test_set_height_valid_values(self):
        try:
            self.physical_info.set_height(17)
            self.physical_info.set_height(48)
            self.physical_info.set_height(72)
            self.physical_info.set_height(84)
        except:
            assert False
    
    def test_set_height_non_integer(self):
        my_assert(ValueError, self.physical_info.set_height, "23")
        my_assert(ValueError, self.physical_info.set_height, 2.3)
        
    def test_set_height_none(self):
        my_assert(ValueError, self.physical_info.set_height, None)
        
    def test_set_height_out_of_range(self):
        my_assert(ValueError, self.physical_info.set_height, -1)
        my_assert(ValueError, self.physical_info.set_height, 0)
        my_assert(ValueError, self.physical_info.set_height, 16)
        my_assert(ValueError, self.physical_info.set_height, 85)
        
    def test_set_temperature_valid_values(self):
        try:
            self.physical_info.set_temperature(95.1)
            self.physical_info.set_temperature(103.9)
            self.physical_info.set_temperature(98.4)
        except:
            assert False
            
    def test_set_temperature_non_float(self):
        my_assert(ValueError, self.physical_info.set_temperature, "23")
        my_assert(ValueError, self.physical_info.set_temperature, 23)
        
    def test_set_temperature_none(self):
        my_assert(ValueError, self.physical_info.set_temperature, None)
        
    def test_set_temperature_out_of_range(self):
        my_assert(ValueError, self.physical_info.set_temperature, 94.9)
        my_assert(ValueError, self.physical_info.set_temperature, 105.1)
        my_assert(ValueError, self.physical_info.set_temperature, 0)
        my_assert(ValueError, self.physical_info.set_temperature, -1)
        
    def test_set_gender_valid_values(self):
        try:
            self.physical_info.set_gender('M')
            self.physical_info.set_gender('F')
        except:
            assert False
        
    def test_set_gender_non_string(self):
        my_assert(ValueError, self.physical_info.set_gender, 23)
        my_assert(ValueError, self.physical_info.set_gender, 23.3)
        
    def test_set_gender_none(self):
        my_assert(ValueError, self.physical_info.set_gender, None)
        
    def test_set_gender_invalid_values(self):
        my_assert(ValueError, self.physical_info.set_gender, "Male")
        my_assert(ValueError, self.physical_info.set_gender, "Girl")
        my_assert(ValueError, self.physical_info.set_gender, "W")
    
    def test_set_date_valid_values(self):
        try:
            self.physical_info.set_date("12-02-2016")
            self.physical_info.set_date("02-29-1996")
            self.physical_info.set_date("01-31-1945")
            self.physical_info.set_date("03-31-1934")
            self.physical_info.set_date("04-30-1945")
        except Exception as e:
            assert False
    
    def test_set_date_non_string(self):
        my_assert(ValueError, self.physical_info.set_date, 23)
        my_assert(ValueError, self.physical_info.set_date, 23.3)

    def test_set_date_none(self):
        my_assert(ValueError, self.physical_info.set_date, None)
        
    def test_set_date_invalid_format(self):
        my_assert(ValueError, self.physical_info.set_date, "02-03")
        my_assert(ValueError, self.physical_info.set_date, "02-03-2016-")
        my_assert(ValueError, self.physical_info.set_date, "02-03--2016")

    def test_set_date_non_numbers(self):
        my_assert(ValueError, self.physical_info.set_date, "Feb-03-2016")
        
    def test_set_date_invalid_year(self):
        my_assert(ValueError, self.physical_info.set_date, "02-03-2101")
        my_assert(ValueError, self.physical_info.set_date, "12-31-1899")

    def test_set_date_invalid_month(self):
        my_assert(ValueError, self.physical_info.set_date, "00-03-2015")
        my_assert(ValueError, self.physical_info.set_date, "13-03-2015")

    def test_set_date_invalid_day(self):
        my_assert(ValueError, self.physical_info.set_date, "02-30-2016")
        my_assert(ValueError, self.physical_info.set_date, "02-29-2015")
        my_assert(ValueError, self.physical_info.set_date, "01-32-2006")
        my_assert(ValueError, self.physical_info.set_date, "04-31-2001")
        my_assert(ValueError, self.physical_info.set_date, "02-29-1900")

    
