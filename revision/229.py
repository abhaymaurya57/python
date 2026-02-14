class Solution(object):
    def majorityElement(self, nums):
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        n=len(nums)
        print(n)
        print(dic)
        lis=[]
        print(lis)
        for i in dic:
            print(dic[i]>n/3)
            if dic[i]>n/3:
                lis.append(i)
        print(lis)
        return lis
obj = Solution()
print(obj.majorityElement([3,4,3]))