# class - blueprint or template

class Student:  #student class
    def __init__(self,name,grade,percentage,team):
        self.name = name
        self.grade = grade
        self.percentage = percentage
        self.team = team

    def student_details(self):  #method
        print(f'{self.name} is in class { self.grade} and percentage is {self.percentage}% and is in team {self.team}')
# object - instance of class

team1 = 'A'
team2 = 'B'

student1 = Student('Abhay',11,96,team1)
# print(student1.name,student1.grade)

student2 = Student('madhav',44,99,team2)
# print(student2.name,student2.grade)

student1.student_details()
student2.student_details()
print(student1.__dict__)

# modify object property
student1.percentage = 98
print(student1.__dict__)

# DELETE OBJECT PROPERTY

# del student1.percentage
# print(student1.__dict__)

#delete object 
# del student1
# print(student1.__dict__)

print(student1.team)
print(student2.team)