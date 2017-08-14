# Intro to Python

# boolean values
T
t
True


# integer values
1234
-23
0


# float values
3.14
314e-2
.1
-.1


# string values
"Python's"
'she said "Python"'
"""String with <newline>
character"""
"This" "is" "one" "string"


# string operators
i_str = "Python"
i_str[1]
i_str[-1]
i_str[1:3]
i_str[1:7:2]
i_str[7:1:-2]
i_str + i_str
len(i_str)
i_str * 3
"y" in i_str
"yt" in i_str
"y" not in i_str
not "y" in i_str

dir("hey")


# string methods
"I love {0}{1}{0}".format(i_str, "language")
# Type dir('name') into python interpreter


# operators
1 + 1
1 - 1
1 * 2
1 / 2
5 % 3

1 < 2
1 <= 2
1 > 2
1 >= 2
1 == 1
1 != 1

i = [1]
j = [1]
i == j
i is j
i is not j

True == 1
True is 1


1 < 3 < 5
1 < 3 < 2

"2" < "1"
"21" < "5"

True and False
True or False
not (1 > 2)

3 and False
3 or False

not 0
not ""


# control structures
if 1 < 2:
    print("1 < 2")
elif 1 == 2:
    print("What!!")
else:
    print(1/0)
    
i = 0
while i < 10:
    print(i)
    i += 1
    break # see what happens when you comment this line
else:
    print("ha ha")
    
for i in range(1, 10):
    if i % 2:
        continue
    print(i)
    break # see what happens when you comment this line
else:
    print("boom")

try:
    i = 3 / 0  # see what happens when you change 0 to 2
except ZeroDivisionError as e:
    print(e)
else:
    print("Hmm")
finally:
    print("finally")
    

# function
def max3(x, y, z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > x and z > y:
        return z

def upper(s, l=3):
    for i in s[:l]:
        print(i.upper())
upper("spam")
upper("spam", 2)



# complex data type
i = ['s', 'p', 'a', 'm']
j = [x.upper() for x in i] # list - kinda eager
k = (x.upper() for x in i) # generator - kinda lazy
l = [x for x in range(1, 10) if x % 2] # comprehension with filter
m = {x.upper() for x in i}
n = {x:x.upper() for x in i}


# classes
class Sorter(object):
    count = 0

    def __init__(self):
        Sorter.count += 1
        self.name = "Sorter" + str(Sorter.count)
        
    def sort(self, array):
        self.name2 = "Sorter" 
        return sorted(array, reverse=True)

i = Sorter()
i.sort(range(1, 10))


# putting all together
import math
print(math.log(100))

from math import log
print(log(100))

def sort(x):
    if x == 1 or x == ["a", "b"] or x == []:
        raise RuntimeError
    elif x == [6,2,6]:
        return [2,6]
    elif x == [1,2,3]:
        return [1,2,3]
    elif x == [2,6,4,8]:
        return [2,4,6,8]