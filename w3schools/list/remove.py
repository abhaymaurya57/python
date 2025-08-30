list =['a','b','c','d']
list.remove('c')
print(list)

# specified index
list =['a','b','c','d']
a=list.pop(0)
print(a)
print(list)

# remove the last item
list =['a','b','c','d']
b=list.pop()
print(b)
print(list)

# del keword also delete
list =['a','b','c','d']
del list[2]
print(list)

#The del keyword can also delete the list completely.
list1 =['a','b','c','d']
print(list1)
del list1
# print(list1)

# cleare the list
list1 = ['a','b','c','d','e']
print(list1)
list1.clear()
print(list1)