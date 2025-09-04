#Set Operations
# In Python, sets support various set operations, which is used to manipulate and compare sets.
#  These operations include union, intersection, difference, symmetric difference, and subset testing.
#  Sets are particularly useful when dealing with collections of unique elements and performing operations based on set theory.

# Union − It combine elements from both sets using the union() function or the | operator.
# Intersection − It is used to get common elements using the intersection() function or the & operator.
# Difference − It is used to get elements that are in one set but not the other using the difference() function or the - operator.
# Symmetric Difference − It is used to get elements that are in either of the sets but not in both using the symmetric_difference() method or the ^ operator.

#Python Set Comprehensions
# Set comprehensions in Python is a concise way to create sets based on iterable objects,
#  similar to list comprehensions. It is used to generate sets by applying an expression to each item in an iterable.

# Syntax
# The syntax for set comprehensions is similar to list comprehensions,
#  but instead of square brackets [ ], you use curly braces { } to denote a set −

# set_variable = {expression for item in iterable if condition}
a={i for i in range(1000) if i%2==0}
print(a)

b=[]
for i in range(0,55295):
    b.append(chr(i))
    print(b)
print(b)

