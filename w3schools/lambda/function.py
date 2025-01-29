def myfunc(n,m):
    return lambda a: a*n-m
x =myfunc(15,2)
print(x(5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))