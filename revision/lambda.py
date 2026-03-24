add=lambda a : a+10
print(add(2))

a = lambda a: lambda b:lambda c :a*b*c
b=a(2)
c=b(5)
print(c(10))