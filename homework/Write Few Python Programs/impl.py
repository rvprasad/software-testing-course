import re

def anagram_check(str1, str2):
    # check if inputs are strings
    if not isinstance(str1, str):
        raise ValueError("First argument {0} is not a string".format(str1))
    if not isinstance(str2, str):
        raise ValueError("Second argument {0} is not a string".format(str2))
    
    # check if str1 and str2 are made up of valid English words
    flag = False
    with open('words.txt', 'rt') as f:  # Fault1
        words = [word.rstrip("\n") for word in f.readlines()]
        tmp1 = all(map(lambda x: x in words, re.split('[\s,\-]+', str1.lower())))
        tmp2 = all(map(lambda x: x in words, re.split('[\s,\-]+', str2.lower())))
        flag = tmp1 == tmp2
    
    # check if characters in str1 are a permutation of characters in str2
    tmp3 = sorted(re.sub('[\s,\-]+', '', str1).lower())
    tmp4 = sorted(re.sub('[\s,\-]+', '', str2).lower())  # Fault2
    
    return flag and tmp3 == tmp4
    

class ShopInfo(object):
    
    def __init__(self, name, phone, email, website):
        self.name = name
        self.phone = phone
        self.email = email
        self.website = website
        
    def get_name(self):
        # check if name is string
        if not isinstance(self.name, str):
            raise ValueError("Name should be string")
        # check if name is at least 2 characters long
        if len(self.name) < 1:
            raise ValueError("Name should be at least two characters long")
        # check if name contains at least one character from English alphabet
        if not re.search('[a-zA-Z]', self.name):
            raise ValueError("Name should contain at least one character from English alphabet")
        # check if name contains characters other than numbers, _, or those from English alphabet
        if re.search('\W', self.name): # Coverage1
            raise ValueError("Name should contain only numbers, _, or English alphabet characters")
        return self.name 
    
    def get_phone(self):
        # check if phone number is an integer
        if not isinstance(self.phone, int):
            raise ValueError("Phone number should be integer")
        # check if phone number is a 10-digit positive integer 
        if self.phone < 0 or len(str(self.phone)) != 10:  # Fault3
            raise ValueError("Phone number should be 10-digit positive number")
        return self.phone
        
    def get_email(self):
        # check if email is a string
        if not isinstance(self.email, str):
            raise ValueError("Email address should be a string")
        # check if email contains exactly one @ symbol
        if sum(1 for _ in re.finditer('@', self.email)) != 1:
            raise ValueError("Email address should have only one @ symbol")
        # check email is a string followed by @ followed by another string
        # where the string is composed of letters, numbers, -, and .
        if not re.search('^[\w\.-_]+@[\w\.-_]+$', self.email): # Coverage2
            raise ValueError("Email address should have the format <addr>@<domain>")
        # check emails does not contain ".."
        if re.search(".*\.\..*", self.email):
            raise ValueError("Email address cannot have '..' substring")
        return self.email
        
    def get_website(self):
        # check if website is a string
        if not isinstance(self.website, str):
            raise ValueError("Website address should be a string")
        # check website has http or https prefix, starts with letter,
        # and is followed by letters, numbers, -, _, ., ~, and /.
        if not re.search("^https?://\w[\w_\-\.~\/]*$", self.website): # Fault4
            raise ValueError("Website address should 'http[s]://<address>'")
        return self.website
