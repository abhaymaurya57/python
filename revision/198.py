
def rob(nums):
    sumodd=0
    sumeven=0
    for i in range(0,len(nums)):
        if i%2==0:
            sumodd+=nums[i]
        else:
            sumeven+=nums[i]
    if(sumodd>sumeven):
        return sumodd
    else:
        return sumeven
nums = [2,1,1,2]
print(rob(nums))