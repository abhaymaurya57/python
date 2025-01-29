# f = open("demofile.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile.txt", "r")
# print(f.read())

#---------------------
f = open("demofile.txt", "w")
f.write(" Woops! I have deleted the content! ")
f.close()

#open and read the file after the overwriting:
f = open("demofile.txt", "r")
print(f.read())