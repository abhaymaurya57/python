#Set Operations
# In Python, sets support various set operations, which is used to manipulate and compare sets.
#  These operations include union, intersection, difference, symmetric difference, and subset testing.
#  Sets are particularly useful when dealing with collections of unique elements and performing operations based on set theory.

# Union −           It combine elements from both sets using the union() function or the | operator.
# Intersection −    It is used to get common elements using the intersection() function or the & operator.
# Difference −      It is used to get elements that are in one set but not the other using the difference() function or the - operator.
# Symmetric Difference − It is used to get elements that are in either of the sets but not in both using the symmetric_difference() method or the ^ operator.

#Python Set Comprehensions
# Set comprehensions in Python is a concise way to create sets based on iterable objects,
#  similar to list comprehensions. It is used to generate sets by applying an expression to each item in an iterable.

# Syntax
# The syntax for set comprehensions is similar to list comprehensions,
#  but instead of square brackets [ ], you use curly braces { } to denote a set −

# set_variable = {expression for item in iterable if condition}
a={i for i in range(10) if i%2==0}
print(a)

# do not run this code
# b=[]
# for i in range(0,55295):
#     b.append(chr(i))
#     print(b)
# print(b)

#Nested Set Comprehensions
nested_set={(x,y) for x in range(1,4) for y in range (4,7)}
print(nested_set)

#  Frozen Sets

# In Python, a frozen set is an immutable collection of unique elements,
# similar to a regular set but with the distinction that it cannot be modified after creation

#You can create a frozen set in Python using the frozenset() function 
# by passing an iterable (such as a list, tuple, or another set)
my_frozen_set = frozenset([1, 2, 3])
print(my_frozen_set) 
my_frozen_set.add(4) 