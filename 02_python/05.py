# Library functions in python

import math 

print(math.log(10))
print(math.sin(45))
print(math.sqrt(16))
print(math.factorial(10))
print(math.pow(10,3))

import random

print(random.random)          # It gives number between 0 to 1

a = random.random()

if a<.5:
    print("Heads")
else:
    print("Tail")


import random

print(random.randrange(1,7))     # Here the output range is 1 to 6 


import calendar 

print(calendar.month(2025, 4))
print(calendar.calendar(2025))


from calendar import *

print(calendar(2021))
print(month(2021,10))


from calendar import month

print(month(2021,10))


import calendar as c 
print(c.month(2021, 10))

from calendar import month as m
print(m(2025, 4))