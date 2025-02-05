#virasat
#allows one class(child ) to reuse the prop and methods of another

#this is parent class - baap
class Student:  #student class
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage+1

    def student_details(self):  #method
        print(f'{self.name} is in class { self.grade} and percentage is {self.percentage}%.')

student1 = Student('Abhay',11,96)
student2 = Student('kushwaha',11,97)
# student1.student_details()
# student2.student_details()
# print(student1.percentage)

# child class - beta
class GraduateStudent(Student): #graduatesstudent child class inherit prop and method from student prent class
    def __init__(self,name,grade,percentage,stream): # parameter from parent class and new parameter in child class
        super().__init__(name,grade,percentage)# class parent class init
        self.stream = stream #this is new attribute in child class
    def student_details(self):
        super().student_details()
        print(f'stream is {self.stream}')


#oject
Grad_student1 = GraduateStudent('abhay',12,96,"PCM")
# print(Grad_student1.stream)
Grad_student1.student_details()
