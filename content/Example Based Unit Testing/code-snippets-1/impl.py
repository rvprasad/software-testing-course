import re

def checkId(x):
    if not isinstance(x, str):
        raise TypeError("Input needs to be a string")
        
    if not re.search(r"^\d+$", x):
        raise ValueError("Non-numerical values are not supported")
        
    if len(x) != 9:
        return False
    
    return True
