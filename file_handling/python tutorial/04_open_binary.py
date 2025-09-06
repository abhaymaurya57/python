#Python provides a built-in function open() to handle file operations 
# and various methods for writing data.

# Opening a File in Append Mode
file = open("demofile.txt", "a")
file.write("\nAppending this line.\n")
file.close()
print ("File opened successfully!!")

#Writing to a New File in Binary Mode

#  By default, read/write operations on a file object are performed on text string data.
#  If we need to handle files of different types, such as media files (mp3), executables (exe),
#  or pictures (jpg), we must open the file in binary mode by adding the 'b' prefix to the read/write mode.

#Writing Binary Data to a File
#To write binary data to a file, open the file in binary write mode ('wb'). 
# The following example demonstrates this −

# Open a file in binary write mode
with open('test.bin', 'wb') as f:
   # Binary data
   data = b"Hello World"
   print(type(data))  
   f.write(data)

# Converting Text Strings to Bytes
#Conversion of a text string to bytes can be done using the encode() function.
#This is useful when you need to write text data as binary data −

with open('test.bin', 'wb') as f:
   # Convert text string to bytes
   data = "Hello World".encode('utf-8')  
   print(type(data))
   f.write(data)