thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
set1 = {"abc", 34, True, 40, "male"}
print(set1)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)