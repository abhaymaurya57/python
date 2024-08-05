student_marks={
    "Abhay":92,
    "harry":78,
    "dimple":56,
    "rahul":41,
    "aniket":99,
    "prem":34
}
student_grades={}
for student in student_marks:   #abhay
    marks=student_marks[student] #92
    if marks>90:
        student_grades[student]="A+"
    elif marks>80:
        student_grades[student]="A"
    elif marks>70:
        student_grades[student]="B+"
    elif marks>60:
        student_grades[student]="B"
    elif marks>50:
        student_grades[student]="C"
    elif marks>50:
        student_grades[student]="F"
print(student_grades)