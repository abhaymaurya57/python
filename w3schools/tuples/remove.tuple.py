#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ('a','b','c','d','e')
y = list(thistuple)
y.remove('a')
thistuple = tuple(y)
print(thistuple)
####################
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)