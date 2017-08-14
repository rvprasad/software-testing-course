import re

class PhysicalInfo(object):
    
    def set_date(self, date):  
        if not isinstance(date, str):
            raise ValueError("date should be a string")
        t = date.split("-")
        if len(t) != 3:
            raise ValueError("date should be in MM-DD-YYYY format")
        if re.search(r'[^0-9\-]', date):
            raise ValueError("date should contain only numbers and -")
            
        year = int(t[2])
        if year < 1900 or year > 2100:
            raise ValueError("invalid year {0}".format(year))
        is_leap = year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
        
        month = int(t[0])
        if month < 1 or month > 12:
            raise ValueError("invalid month {0}".format(month))
        day_limit = 31
        if month in [4, 6, 7, 9, 11]:
            day_limit = 30
        elif month == 2:
            if is_leap:
                day_limit = 29
            else:
                day_limit = 28
            
        day = int(t[1])
        if day < 1 or day > day_limit:
            raise ValueError("invalid day {0}".format(day))
            
        self.date = date
