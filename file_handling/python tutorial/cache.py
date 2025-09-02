from functools import lru_cache

# @lru_cache
def funct(n):
    # print(n)
    if n<=1:
        return 1
    result =n*funct(n-1)
    return result
a = funct(800)
print(a)