def myfunc(n,m):
    return lambda a: a*n-m
x =myfunc(15,2)
print(x(1))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

def myfunc(m):
    return lambda n: n*n-m
x =myfunc(2)
print(x(3))