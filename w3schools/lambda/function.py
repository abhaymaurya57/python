def myfunc(n):
    return lambda a: a*n
x =myfunc(15)
print(x(5))