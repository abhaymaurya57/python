#File handling in Python involves interacting with files on your computer to 
# read data from them or write data to them. Python provides several built-in
# functions and methods for creating, opening, reading, writing, and closing files. 

#Opening a File in Python

'''To perform any file operation, the first step is to open the file.
 Python's built-in open() function is used to open files in various modes, 
 such as reading, writing, and appending. '''

#file = open("filename", "mode")
#Where, filename is the name of the file to open and mode is the mode in which
#  the file is opened (e.g., 'r' for reading, 'w' for writing, 'a' for appending).

#File Opening Modes
	
# r -   opens a file for reading only.
# rb -  Opens a file for reading only in binary format.
# r+ -  Opens a file for both reading and writing. 
# rb+ - Opens a file for both reading and writing in binary format.
# w -   Opens a file for writing only.
# b -   Opens the file in binary mode
# t -   Opens the file in text mode (default)
# +  -  open file for updating (reading and writing)
# wb -  Opens a file for writing only in binary format.
# W+ -  Opens a file for both writing and reading.
# Wb+ - Opens a file for both writing and reading in binary format.
# a -   Opens a file for appending.
# ab -  Opens a file for appending in binary format.
# a+ -  Opens a file for both appending and reading. 
# ab+ - Opens a file for both appending and reading in binary format.
# x -   open for exclusive creation, failing if the file already exists

# Example 1
# Opening a file in read mode
file = open("Abhay.py", "r")
print(file.read())

# Opening a file in write mode

# ***** this line you run then old data is delete and new data is write ********

# file = open("Abhay.py", "w")
# file.write("hii abhay ")
# file = open("Abhay.py", "r")
# print(file.read())

# Opening a file in append mode
file = open("Abhay.py", "a")
file.write("'Hello ,world!'\n")
file = open("Abhay.py", "r")
print(file.read())


# Step 2: Open same file in binary read mode
with open("Abhay.py", "rb") as f:
   data = f.read()
   print("Binary content:", data)
   print("Decoded content:", data.decode("utf-8"))

# Example 2

# Open a file
fo = open("Abhay.py", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
fo.close()
print ("Closed or not: ", fo.closed)

file = open('abhay.py','r')
with open("abhay.py", "r") as file:
   line = file.readline()
   while line:
      print(line, end='')
      line = file.readline()

#  ** old data is crean if this is run you ****

# wrt = open('kush.py','w+')
# a=[]
# for i in range(100):
#    print()
#    print(a)
#    a.append(i)
# print(wrt.write(str(a)))
# print(wrt.read())
