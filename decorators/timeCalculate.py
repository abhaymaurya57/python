import time
import random
def timer(fun):
    def wrapper(*args):
        start = time.time()
        sum1=0
        for i in range(1,100000000):
            sum1+=i
        print(sum1)
        fun(*args)
        end = time.time()
        return end-start
    return wrapper

@timer
def timecalculate(*args):
    print("hii")
print(timecalculate())