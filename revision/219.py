class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                if abs(dic[nums[i]]-i)<=k:
                    print(abs(dic[nums[i]]-i))
                    return True
            dic[nums[i]]=i
        print(dic)
        return False
                
obj = Solution()
a =obj.containsNearbyDuplicate([1,2,3,1],3)
print(a)