# import time

# def decorator2(func):
#     print(f'enter the ssecound decorator')
#     def wrapper(*args,**kwargs):
#         print('print wrapper')
#         result = func(*args,**kwargs)
#         print(f'rnd the functiom')
#         return result
#     return wrapper




# @decorator2
# def time_decorator(func):
#     print("enter the time decorator")
#     def wrapper(*args,**kwargs):
#         print("enter the wrapper")
#         start_time = time.time()
#         print(start_time)
#         result = func(*args,**kwargs)
#         end_time = time.time()
#         print(end_time)
#         print(f"{func.__name__} took {end_time-start_time:4f} secounds to execute.")
#         return result
#     return wrapper

# @time_decorator
# def heavy_calculation():
#     print("calculation start!")
#     time.sleep(3)
#     print("calculation done!")

# heavy_calculation()

# import sys

# # List vs Generator Memory Check
# my_list = [i for i in range(10000)]
# my_gen = (i for i in range(10000))

# print("List Size:", sys.getsizeof(my_list), "bytes") # Jyada memory lega
# print("Gen Size:", sys.getsizeof(my_gen), "bytes")   # Bahut kam memory lega (sirf object ka size)

# class FileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file.close()
#         print("File safely closed!")

# # Usage
# with FileManager('test.txt', 'w') as f:
#     f.write('Hello World')
# Jaise hi block se bahar niklenge, __exit__ apne aap chal jayega.


class  Ded:

    def __init__(self,a,b):
        self.a = a
        self.b =  b

    def  __add__(self, a,b):
        print(self.a+self.b)
        return self.a+self.b
print(Ded(4,5))
        