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
        
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name should be a string")
        tmp1 = name.lower()
        if re.search(r'[^a-z0-9 ]', tmp1):
            raise ValueError("name should contain letters, numbers, -, and space")
        if len(tmp1.strip()) < 2 or len(tmp1.replace("-", '')) < 2:
            raise ValueError("name should be at least two characters long")
        if not re.search(r'[a-z]', tmp1):
            raise ValueError("name should contain at least one character")
        self.name = name
    
    def set_gender(self, gender):
        if gender != 'M' and gender != 'F':
            raise ValueError("gender should be either M or F")
        self.gender = gender
    
    def set_height(self, height):
        if not isinstance(height, int):
            raise ValueError("height should be an integer")
        if height < 17 or height > 84:
            raise ValueError("height should be an integer between 17 and 84")
        self.height = height

    def set_temperature(self, temperature):
        if not isinstance(temperature, float):
            raise ValueError("temperature should be a float")
        if temperature < 95 or temperature > 104:
            raise ValueError("temperature should be a float between 95 and 104")
        self.temperature = temperature
