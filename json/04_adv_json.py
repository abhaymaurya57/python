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

def allcapital(obj):
    if obj:
        obj = str(obj).upper()
    return obj

# Load JSON with custom deserializer
data = json.loads(json_string, object_hook=custom_decoder)
data1=json.loads(json_string,object_hook=allcapital)
print('data------->',data)
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