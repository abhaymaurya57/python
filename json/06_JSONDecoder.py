#JSONDecoder class

#The JSONDecoder class is used to decode a JSON string 
# back into a Python data structure. The main method in this class is decode()

import json

data = ['Rakesh', {'marks': (50, 60, 70)}]
print(type(data))
e = json.JSONEncoder()
print(type(e))
s = e.encode(data)
print(s)
print(type(s))

d = json.JSONDecoder()
print(type(d))
obj = d.decode(s)
print(obj, type(obj))