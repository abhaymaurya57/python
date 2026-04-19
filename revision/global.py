class nums:
    def num(self,nums1,nums2):
        lst =[]
        for i in nums1:
            fil=-1
            find=False
            for j in nums2:
                if i==j:
                    find=True
                    if find:
                        if j>fil:
                            fil=j
                            break
            lst.append(fil)
        return lst
                
obj = nums()
lst1=[1,2,3,4,5]
lst2=[5,6,2,7]
result = obj.num(lst1,lst2)
print(result)