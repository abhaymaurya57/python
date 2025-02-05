# class student:
#     def __init__(self,cls,name):
#         self.i=cls
#         self.r =name

# data = student(5,'Abhay')
# print(data.i)
# print(data.r)
##########################
# class table:
    # counter = 1
    # while counter<10:
    # def __init__(self,number):
    #     self.i=number
    

        
class table:

    # def __init__(self):
    #     self.counter  = 1
    
    def print_table(self):
        self.counter  = 1
        while self.counter < 10:
  
            self.counter += 1
            print(self.counter*2)
        # print(self.counter*2)

obj = table()
obj.print_table()


student_1 = ['madhav',10]
student_2 = ['Abhay',10]

 
print(f'{student_1[0]} is in class {student_1[1]}')
print(f'{student_2[0]} is in class {student_2[1]}')

