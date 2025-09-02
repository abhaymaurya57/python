#JSONEncoder Class
#The JSONEncoder class in Python is used to encode
# Python data structures into JSON format. Each 
# Python data type is converted into its corresponding
# JSON type, as shown in the following table −

# PYTHON                      JSON

# Dict	                      object
# list, tuple	              array
# Str	                      string
# int, float, int- & 
# float-derived Enums	      number
# True	                      true
# False	                      false
# None	                      null

#The JSONEncoder class is instantiated using the
#  JSONEncoder() constructor. The following important 
# methods are defined in this class −

# encode(obj) −        Serializes a Python object into a JSON formatted string.
# iterencode(obj) −    Encodes the object and returns an iterator that yields the encoded form of each item in the object.
# indent −             Determines the indent level of the encoded string.
# sort_keys −          If True, the keys appear in sorted order.
# check_circular −     If True, checks for circular references in container-type objects.


# In the following example, we are encoding Python list object. We use the iterencode() method to display each part of the encoded string −
import json
data = ['Rakesh', {'marks': (80,90,50, 60, 70)},{'name':'abhay'}]
e = json.JSONEncoder(sort_keys=True)
print(type(e))
print(type(data))
# Using iterencode() method 
for obj in enumerate(data):
   print(obj)
   
for obj in e.iterencode(data):
   print(obj)
