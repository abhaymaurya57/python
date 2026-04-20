class nums:
    def num(self,nums1,nums2):
        lst =[]
        for i in nums1:
            # print(i)
            # break
            fil=-1 #4
            print(fil)
            find=False
            for j in nums2:
                
                if i==j:
                    find=True
                if find:
                    if j>i:
                        fil=j  #4
                        break
            lst.append(fil)
        return lst
                
obj = nums()
lst1=[4,1,2]
lst2=[1,3,4,2]
result = obj.num(lst1,lst2)
print(result)

obj1 = nums()
obj2 = nums()

# address are diffrent
print(id(obj1))
print(id(obj2))

# address are same
a=5
b=5
print(id(a))
print(id(b))

# import keyword
# print(keyword.kwlist)