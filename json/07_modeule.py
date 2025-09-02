#The json module in Python provides methods for working with 
# JSON (JavaScript Object Notation). It allows you to serialize 
# and deserialize Python objects to and from JSON format, which is 
# a commonly used data interchange format.

#Function & Description
# 1	json.dump()
# Serializes a Python object and writes it to a file-like object.

# 2	json.dumps()
# Serializes a Python object and returns it as a JSON-formatted string.

# 3	json.load()
# Deserializes a JSON-formatted stream into a Python object.

# 4	json.loads()
# Deserializes a JSON-formatted string into a Python object.

#JSON Encoder Methods
# 1	json.JSONEncoder
# Encoder class for converting Python objects to JSON format.

# 2	json.JSONEncoder.encode()
# Encodes a Python object to JSON format as a string.

# 3	json.JSONEncoder.iterencode()
# Encodes a Python object to JSON format in an iterator style.

# 4	json.JSONEncoder.default()
# Override method to handle objects that are not serializable by default.


# #JSON Decoder Methods

# 1	json.JSONDecoder
# Decoder class for converting JSON data to Python objects.

# 2	json.JSONDecoder.decode()
# Deserializes a JSON string into a Python object.

# 3	json.JSONDecoder.raw_decode()
# Deserializes a JSON string with extra information for error handling.

import json

data = {"name": "Abhay", "age": 20, "skills": ["Python", "SQL"]}

# Pretty print JSON with indent
print(json.dumps(data, indent=5))
