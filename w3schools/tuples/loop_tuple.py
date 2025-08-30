thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
print(20*"-")
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
print(20*"-")
#Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
print(20*"-")
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
x = mytuple.count("apple")
print(x)
print(mytuple)