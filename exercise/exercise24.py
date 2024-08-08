student_data=[
    {
        "name" : "Ram",
        "roll_no":10,
        "age":20,
        "cource":"python"
     },
     {
        "name":"mohan" ,
        "roll_no":20,
        "age":22,
        "cource":"java"
    }
]
def  add_new_student(name,rollno,age,coucse_opted):
    new_student={}
    new_student["name"]=name
    new_student["roll_no"]=rollno
    new_student["age"]=age
    new_student["course"]=coucse_opted
    student_data.append(new_student)
add_new_student("shyam",22,18,"c++")
print(student_data)