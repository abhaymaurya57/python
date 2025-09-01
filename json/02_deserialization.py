import json

# Deserialize JSON string to Python object

# JSON string
json_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "state": "NY"}}'

# Convert JSON string -> dict
new_data=json.loads(json_string)
print("new data",new_data)
print(new_data.get("name"))
print(new_data["age"])
print(new_data["address"]["city"])
city = new_data.get("address", {}).get("city", "Unknown City")
print(city)
address = new_data["address"]
print(address["city"])