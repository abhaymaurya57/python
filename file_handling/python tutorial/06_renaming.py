#In Python, you can rename and delete files using built-in functions from the os module.

#Renaming Files in Python
# To rename a file in Python, you can use the os.rename() function.
#  This function takes two arguments: the current filename and the new filename.

#Syntax
'''    os.rename(current_file_name, new_file_name)    '''

#Parameters
# current_file_name − It is the current name of the file you want to rename.
# new_file_name − It is the new name you want to assign to the file.

import os

os .rename("kush.py","kushwaha.py")
print(f"file rename successfully.")