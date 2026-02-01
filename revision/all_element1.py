# initialize all elements to 1
tri=[]
for i in range(5):
    row = [1]*(i+1)
    tri.append(row)
for i in range(len(tri)):
    print(tri[i])