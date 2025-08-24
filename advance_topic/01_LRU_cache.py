import time
import timeit
from functools import lru_cache

# @lru_cache(maxsize=4)
# def slow_add(a,b):
#     time.sleep(3)
#     return a+b

# while True:
#     a=int(input("enter a: "))
#     b=int(input("Enter b: "))
#     print(slow_add(a,b))
    
# example 2

@lru_cache(maxsize=4)
def rec(n):
    if n<2:
        return n
    return rec(n-1)+rec(n-2)

a=rec(343)
# time.sleep(2)
print(timeit.timeit(lambda:rec,number=1))
print(a)