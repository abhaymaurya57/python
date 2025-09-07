# Directories in Python

# Checking if a Directory Exists
'''We can check if a directory exists or not using the os.path.exists() function'''

#Example
import os

path="D:\\Abhay\python\\file_handling\\python tutorial\\08_directories.py"
path="D:\\Abhay\python\\file_handling\\python tutorial\\08_directories.py"
if os.path.exists(path):
    print(f"The directory '{path}' exists.")
else:
   print(f"The directory '{path}' does not exist.")

#Creating a Directory
#You create a new directory in Python using the os.makedirs() function. 
import os 
try:
    os.makedirs("abhmrya.py")
    print("successfully create")
except OSError as e:
    print(f"Error: Failed to create directory. {e}")

#The mkdir() Method
#You can use the mkdir() method of the os module to 
# create directories in the current directory.
'''os.mkdir("newdir")'''

import os
os.mkdir("testt")
print("directory create successfuly")
print(os.path.exists("test.py"))

#Get Current Working Directory
#To retrieve the current working directory in Python, you can use the os.getcwd() function.
'''os.getcwd()'''

print(os.getcwd())

#Listing Files and Directories
#You can list the contents of a directory using the os.listdir() function.
#This function returns a list of all files and directories within the specified directory path.
#In the example below, we are listing the contents of the specified directory path using the listdir()

import os
directory_path = r"D:\Abhay\python"
try:
   contents = os.listdir(directory_path)
   print(f"Contents of '{directory_path}':")
   for item in contents:
      print(item)
except OSError as e:
   print(f"Error: Failed to list contents of directory '{directory_path}'. {e}")

#Changing the Current Working Directory
#You can change the current directory using the chdir() method.
#  This method takes an argument, which is the name of the directory that you want to make the current directory.
'''os.chdir("newdir")'''
import os

new_directory = r"D:\Abhay\python\test"

try:
    os.chdir(new_directory)
    print(f"Current working directory changed to '{new_directory}'.")
except OSError as e:
    print(f"Error: Failed to change working directory to '{new_directory}'. {e}")

#Removing a Directory
# You can remove an empty directory in Python using the os.rmdir() method.
#  If the directory contains files or other directories, you can use shutil.rmtree() method to delete it recursively.

'''os.rmdir(directory_path)
# or
shutil.rmtree(directory_path)'''
import os
directory_path = r"D:\MyFolder\new_dir"

try:
   os.rmdir(directory_path)
   print(f"Directory '{directory_path}' successfully removed.")
except OSError as e:
   print(f"Error: Failed to remove directory '{directory_path}'. {e}")