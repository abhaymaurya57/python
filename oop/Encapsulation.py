#restrict access to certain attribute or method to protect data
class Student:  #student class
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.__percentage = percentage+1

    def get_percentage(self):
        return self.__percentage

    def student_details(self):  #method
        print(f'{self.name} is in class { self.grade} and percentage is {self.__percentage}%.')

student1 = Student('Abhay',11,96)
student2 = Student('kushwaha',11,97)
student1.student_details()
student2.student_details()
# print(student1.__percentage)

print(student1.get_percentage())
print(student2.get_percentage())