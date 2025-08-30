thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

print(50*'*')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = list(thisdict.keys())
print(mydict)

mydict = list(thisdict.items())
print(mydict)
print(dict(mydict).values())