i = 1
while i < 6:
  print(i)
  i += 1
#  break statment
print(50*'-')
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print(50*'-')
#######3 continue statment####
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print(50*'-')
for x in range(100):
  print(x)

for x in range(2, 6):
  print(x)
print(50*'-')
for x in range(2, 30, 3):
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass

