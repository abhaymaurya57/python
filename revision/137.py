def singleNumber(nums):
    dic={}
    for i in nums:
        if i not in dic:
            dic[i]=1
        elif i in dic:
            a = dic[i]
            a = a+1
            dic[i]=a
    print(dic)
    for i in dic:
        if dic[i]!=3:
            return i
nums=[0,1,0,1,0,1,99]
print(singleNumber(nums))

#   -_*