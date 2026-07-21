# s=input("Enter main string:")
# subs=input("Enter sub string")
s="aabfdabfdsfbafdfaa"
subs="a"
Flag=False
pos=-1

n = len(s)

while True:
    pos=s.find(subs,pos+1,n)
    print(pos)
    if pos==-1:
        break
    print("found at position",pos)
    Flag=True
if Flag==False:
    print("Not Found")