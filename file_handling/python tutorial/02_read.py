# Reading a File in Python
# Reading a file in Python involves opening the file in a mode that allows for reading,
#  and then using various methods to extract the data from the file. Python provides several
#  methods to read data from a file −

# read() − Reads the entire file.

# readline() − Reads one line at a time.

# readlines − Reads all lines into a list.

#*********************************************

#Using read() method
#we are using the read() method to read the whole file into a single string −
with open("Abhay.py", "r") as file:
   content = file.read()
   print(content)

#Using readline() method
# In here, we are using the readline() method to read one line at a time, making 
# it memory efficient for reading large files line by line −

with open("Abhay.py", "r") as file:
   line = file.readline()
   while line:
      print(line, end='')
      line = file.readline()
   
# Using readlines() method
#we are using the readlines() method to read the entire file and splits it into a list
#  where each element is a line −
with open("Abhay.py", "r") as file:
   lines = file.readlines()
   for line in lines:
      print(line, end='')

