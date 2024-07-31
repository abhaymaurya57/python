#problem 1
count=1
while count<=10:
    print(count)
    count+=1
    if count ==4:
        break
    print("hii")
print("out from loop")

#problem 2

list1=["hii","hello","welcome"]
names=["krishna","rama","madhav"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name=="rama":
            break
    print("out from inner loop")
print("out from outer loop")