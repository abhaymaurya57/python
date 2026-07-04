def findDifferentBinaryString(nums: list[str]) -> str:
        n=len(nums[0])
        ans=['0']*n
        for i, x in enumerate(nums):
            print(ans)
            if x[i]=='0':
                print(x[i])
                ans[i]='1'
            else:
                ans[i]='0'
        return "".join(ans)
                
nums = ["01","10"]
print(findDifferentBinaryString(nums = ["01","10"]))