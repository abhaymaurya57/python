#  Writing to a File in Python

# To write data to a file, use the write() or writelines() methods.
# When opening a file in write mode ('w'), the file's existing content is erased.

#Using the write() method
#  we are using the write() method to write the string passed to it to the file.
#********** If the file is opened in 'w' mode, it will overwrite any existing content.********
#  If the file is opened in 'a' mode, it will append the string to the end of the file −

with open("demofile.txt", "w") as file:
   file.write("Hello, World!")
   print ("Content added Successfully!!")

# Using the writelines() method
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("demofile.txt", "w") as file:
   file.writelines(lines)
   print ("Content added Successfully!!")

#Closing a File in Python
#We can close a file in Python using the close() method. 
#It is important to close files after operations are completed
#  to prevent data loss and free up system resources.

file = open("demofile.txt", "w")
file.write("This is an example.")
file.close()
print ("File closed successfully!!")

#Using "with" Statement for Automatic File Closing

# The with statement is a best practice in Python for file operations because
#  it ensures that the file is automatically closed when the block of code is exited,
#  even if an exception occurs.

with open("demofile.txt", "w") as file:
   file.write("This is an example using the with statement.")
   print ("File closed successfully!!")

#Handling Exceptions When Closing a File

# we use a try-finally block to handle exceptions when closing a file.
#  The "finally" block ensures that the file is closed regardless of whether an error occurs in the try block −

try:
   file = open("demofile.txt", "w")
   file.write("This is an example with exception handling.")
finally:
   file.close()
   print ("File closed successfully!!")