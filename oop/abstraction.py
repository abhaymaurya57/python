#hidein unnecesary detail from users through class ,method
class Student:  #student class
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage+1

    def student_details(self):  #method
        print(f'{self.name} is in class { self.grade} and percentage is {self.percentage}%.')

student1 = Student('Abhay',11,96)
student2 = Student('kushwaha',11,97)
student1.student_details()
student2.student_details()
print(student1.percentage)