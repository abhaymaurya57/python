# modules in python
#single py file

# create a module mymodule.py
import mymodule
mymodule.say_hello('abhay')
mymodule.say_bye('abhay')

#import/use specific part of code
from mymodule import person1
print(person1['name'])

# package: collection module/py files + __init__.py

#library : collection of module and packages

import math
A = 16
A = 9231
print(math.sqrt(A))

# import specific function from lib
from math import factorial
b = 10
print(factorial(b))

#install new module/lib

# pip install<library_name>