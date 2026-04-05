fo = open("myfile.py",'r')
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
fo.close()

with open('03_data.json','r') as file:
    print(file.read())