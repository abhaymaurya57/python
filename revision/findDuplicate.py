def addToArrayForm(num, k):  
        total=0
        for i in num:
            total=total*10
            total=total+i
            
        total = k+total
        lis=[]
        for i in str(total):
            lis.append(int(i))
        return lis
num=[1,2,0,0]
k=36
print(addToArrayForm(num,k))