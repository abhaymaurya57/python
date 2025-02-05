# allow method in defft classes to have in 

class Student:  #student class
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage+1

    def student_details(self):  #method
        print(f'{self.name} is in class { self.grade} and percentage is {self.percentage}%.')

# child class - beta
class GraduateStudent(Student): #graduatesstudent child class inherit prop and method from student prent class
    def __init__(self,name,grade,percentage,stream): # parameter from parent class and new parameter in child class
        super().__init__(name,grade,percentage)# class parent class init
        self.stream = stream #this is new attribute in child class

    def student_details(self): #method
        print(f'{self.name} in class {self.grade}, with {self.percentage}% and from stream is {self.stream}')

#object
student1 = Student('Abhay',11,96)
student2 = Student('kushwaha',11,97)
Grad_student1 = GraduateStudent('abhay',12,96,"PCM")
student1.student_details()
Grad_student1.student_details()