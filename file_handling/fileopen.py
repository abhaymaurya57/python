f = open("while.py","r")
print(f.read())
print(50*"-")
#------- read only parts of the file

f = open("while.py","r")
print(f.read(20))
print(50*"-")
#---------  read lines -------
f = open("while.py", "r")
print(f.readline())
print(f.readline())

print(f.readline())
print(f.readline())
print(50*"-")
#------------------------
f = open("while.py","r")
for x in f:
    print(x)

print(50*"-")
#---------------------------
f = open("demofile.txt", "r")
print(f.read())
f.close()