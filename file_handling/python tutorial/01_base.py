#File handling in Python involves interacting with files on your computer to 
# read data from them or write data to them. Python provides several built-in
# functions and methods for creating, opening, reading, writing, and closing files. 

#Opening a File in Python

'''To perform any file operation, the first step is to open the file.
 Python's built-in open() function is used to open files in various modes, 
 such as reading, writing, and appending. '''

file = open('abhay.py','r')
with open("abhay.py", "r") as file:
   line = file.readline()
   while line:
      print(line, end='')
      line = file.readline()

wrt = open('kush.py','w+')
a=[]
for i in range(100):
   print()
   print(a)
   a.append(i)
print(wrt.write(str(a)))
print(wrt.read())