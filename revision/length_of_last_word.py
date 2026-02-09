class Solution(object):
    def lengthOfLastWord(self, s):
        prev=0
        sum=0
        for i in s:
            if i == " ":
                if sum > 0:
                    prev = sum
                    sum = 0
            elif(i!=" "):
                sum+=1
        return sum if sum!=0 else prev

obj =  Solution()
print(obj.lengthOfLastWord("   fly me   to   the moon  "))

# m-2
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         lst=s.split()
#         return len(lst[-1])