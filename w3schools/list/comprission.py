list =['a','b','c','d','e']
# for x in list:
#     print(x)

#Print all items by referring to their index number:
# for i in range(len(list)):
#     print(list[i])

# Using a While Loop
# list = ['a','b','c']
# i =0
# while i<len(list):
#     print(list[i])
#     i=i+1
# list =['a','b','c','d','e']
# [print(x) for x in list]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


#################################

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in range(12)]
print(newlist)
newlist = [x for x in range(10) if x < 3]
print(newlist)

##############################
# expression 
# upper 
newlist = [x.upper() for x in fruits]
print(newlist)


# set all value in the new list to 'hello'
newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

