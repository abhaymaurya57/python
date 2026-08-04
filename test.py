class School:

    def __init__(self,student,teacher,grade):
        self.student = student
        self.teacher = teacher
        self.grade = grade
    
class Student(School):

    def __init__(self,name,student,teacher,grade):
        super().__init__(student,teacher,grade)
        self.name = name
        print(grade)

# sch = School('abhay','Vinay','A')
stu = Student('kush','abhay','Vinay','A')
