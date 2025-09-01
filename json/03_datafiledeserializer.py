import json

# Read and deserialize from file
with open('03_data.json',"r") as f:
    print(f)
    new_data=json.load(f)
print("new data",new_data)
print(new_data.get("name"))
print(new_data["age"])
print(new_data["address"]["city"])
city = new_data.get("address", {}).get("city", "Unknown City")
print(city)
address = new_data["address"]
print(address["city"])

print(new_data["courses"])
print(new_data["courses"][0])
print(new_data["courses"][1])