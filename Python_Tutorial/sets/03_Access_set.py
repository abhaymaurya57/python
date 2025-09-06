#  Access Set Items
#In Python, sets are unordered collections of unique elements,
#  and unlike sequences (such as lists or tuples), sets do not have
#  a positional index for their elements.

# Defining a set
langs = {"C", "C++", "Java", "Python"}
# Accessing set items using a for loop
for lang in langs:
   print (lang)

number = {'a',3,2,6,'b',4,7,9,'s',5,7,8}
print([i for i in number])


#Access Set Items Using List Comprehension
my_set = {1, 2, 3, 4, 5}
# Accessing set items using list comprehension
accessed_items = [item for item in my_set]
print(accessed_items)