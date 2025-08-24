import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        print(cache_value)
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(2)
    return a+b

print(long_running_function(2,3))
print(long_running_function(20000,34343))
print(long_running_function(4,3))
print(long_running_function(4,3))
print(long_running_function(4,5))
print(long_running_function(5,3))
print(long_running_function(20000,34343))
print(long_running_function(20000,34343))
print(long_running_function(20000,34343))
print(long_running_function(20000,34343))
print(long_running_function(4,3))
print(long_running_function(4,3))
print(long_running_function(4,3))
print(long_running_function(4,3))
print(long_running_function(4,3))
print(long_running_function(4,3))
