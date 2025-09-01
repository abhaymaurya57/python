import json

#python dictionary 
data={"name":"abhay","age":22,"city":"bhaynder"}
print(type(data))
print(data.get("name"))
print(data['city'])

# Convert dict -> JSON string
json_string=json.dumps(data)
print(json_string)
print(type(json_string))

# Convert JSON string -> dict
new_data=json.loads(json_string)
print("new data",new_data)
print(new_data.get("name"))
print(new_data["age"])
print(new_data["city"])