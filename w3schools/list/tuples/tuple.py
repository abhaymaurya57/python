thistuple = ("apple", "banana", "cherry")
print(thistuple)

######## allow duplicate######
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

##### length#
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4=tuple1+tuple2+tuple3
print(len(tuple4))
print(type(tuple2))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

############## chek if item exist
list = ('a','c','d')
if 'c' in list:
    print('yes,"a" is present in list')