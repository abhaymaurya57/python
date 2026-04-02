a = [1,2,3,4,5]
# b =[2,3,4,5,6]
b ={1,2,3,4,5}
print(type(a))
print(type(b))
c = zip(a,b)
print(type(c))
for i in c:
    print(i)
print(c)