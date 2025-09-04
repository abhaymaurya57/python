#In Python, a set is an unordered collection of unique elements.
#  Unlike lists or tuples, sets do not allow duplicate values i.e.
#  each element in a set must be unique. Sets are mutable, meaning you 
# can add or remove items after a set has been created.

#Sets are defined using curly braces {} or the built-in set() function.
#  They are particularly useful for membership testing, removing duplicates 
# from a sequence, and performing common mathematical set operations like union,
#  intersection, and difference.

# Using Curly Braces
a = {1,2,3,4,5}
print(type(a))
print(a)

# Empty set 
empty_set = set()
print(type(empty_set))
print(empty_set)

# # Empty list
empty_list=[]
print(type(empty_list))
print(empty_list)

#Using the set() Function
# Alternatively, you can create a set using the set() 
# function by passing an iterable (like a list or a tuple) 
# containing the elements you want to include in the set −

b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(b))
print (b)

#Duplicate Elements in Set
c = {1, 2, 2, 3, 3, 4, 5, 5} 
print (c)

# Sets can contain elements of different data types,including numbers, 
# strings, and even other sets (as long as they are immutable) −

d = {1,'Abhay',(1,2,3,4,5,6,7)}
print(d)

# Adding Elements in a Set
# To add an element to a set, you can use the add() function.

e = {1, 2, 3, 3}
e.add(4)  
print (e)
# e.append(5)  // error not support error

#Removing Elements from a Set

# You can remove an element from a set using the remove() function.
f={1,2,3,4,5}
f.remove(3)
print(f)

#Alternatively, you can use the discard() function to remove an element from the set if it is present
g={1,2,3,4}
g.discard(1)
print(g)

#Membership Testing in a Set
if 2 in g:
    print("yes 2 is present ")
else:
    print("2 is not present")