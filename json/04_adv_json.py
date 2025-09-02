#If your JSON data includes objects that need special handling (e.g., custom classes), 
# you can define custom deserialization functions. Use the object_hook parameter of json.loads()
#  or json.load() method to specify a function that will be called with the result of every JSON object decoded.


#In the example below, we are demonstrating the usage of custom object serialization −
import json

# JSON string
json_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "state": "NY"},"like":"you12love"}'

# Custom deserializer function
def custom_decoder(obj):
    if "age" in obj:
        obj["age"] = str(obj["age"])  # convert age to string
    if "is_student" in obj:
        obj["is_student"] = "Yes" if obj["is_student"] else "No"
    if "address" in obj:
        obj["address"]["city"] = obj["address"]["city"].upper()  # uppercase city
    if "like" in obj:
        obj["like"] = str(obj["like"]).upper()
    return obj
# Load JSON with custom deserializer
data = json.loads(json_string, object_hook=custom_decoder)
print('data------->',data)

#************************************

json_string1 = '{"name": "John", "age": 30}'
def allcapital(obj):
    if obj:
        # obj = str(obj).upper()  // key not suport of json
        obj={str(k).upper(): v for k, v in obj.items()}
    obj["clas"]=121
    obj["clasess"]=121232
    return obj

# def allcapital(obj):
#     new_obj = {}
#     for k, v in obj.items():
#         if isinstance(v, str):
#             new_obj[k] = v.upper()
#         else:
#             new_obj[k] = v
#     new_obj["class"] = 12
#     return new_obj

data1=json.loads(json_string1,object_hook=allcapital)
print('data1------->',data1)


#   example -2
# import json
# from datetime import datetime

# # Custom deserialization function
# def custom_deserializer(dct):
#     if 'joined' in dct:
#       dct['joined'] = datetime.fromisoformat(dct['joined'])
#     return dct

# # JSON string with datetime
# json_string = '{"name": "John", "joined": "2021-05-17T10:15:00"}'

# # Deserialize with custom function
# python_obj=json.loads(json_string,object_hook=custom_deserializer)
# print(python_obj)

#object_pairs_hook
json_string = '{"a": 1, "b": 2, "c": 3}'

def hook(pairs):
    return {k: v*2 for k, v in pairs}  # double values

data = json.loads(json_string, object_pairs_hook=hook)
print(data)

#parse_constant
json_string = '[NaN, Infinity, -Infinity]'
data = json.loads(json_string, parse_constant=lambda x: f"Special({x})")
print(data)

#parse_int
json_string = '{"age": 30, "year": 2025}'
data = json.loads(json_string, parse_int=lambda x: int(x) * 10)
print(data)

#parse_float
json_string = '{"pi": 3.14159}'
data = json.loads(json_string, parse_float=lambda x: round(float(x), 2))
print(data)

# or

def floatt(obj):
    for k, v in obj.items():
        if isinstance(v, float):
            obj[k] = round(v, 3)
    return obj
json_string1 = '{"pi": 3.14159}'
data1 = json.loads(json_string1, object_hook=floatt)
print(data1)