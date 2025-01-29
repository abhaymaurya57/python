
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
for x in thisdict:
  print(x)
print(50*'*')
for x in thisdict:
  print(thisdict[x])
print(50*'*')
for x in thisdict.values():
  print(x)
print(50*'*')
for x in thisdict.keys():
  print(x)
print(50*'*')
for x, y in thisdict.items():
  print(x , y)