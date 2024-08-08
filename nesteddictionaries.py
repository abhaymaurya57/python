student_data={
    "Ram" : {"roll_no":10,"age":20,"cource":"python"},
    "mohan" : {"roll_no":20,"age":22,"cource":"java"}
}
print(student_data)
print(student_data["mohan"])
print(student_data["mohan"]["roll_no"])
student_data['mohan']['phone_no']=9999
print(student_data["mohan"])
del student_data["mohan"]["phone_no"]
print(student_data["mohan"])

travel_data={
    "gujrat":["dwarikadhish","somnath","statue of unity"],
    "rajasthan":["jaipur","udaipur"]
} 
print(travel_data)
print(travel_data["rajasthan"])