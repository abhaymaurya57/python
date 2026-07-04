

def generator(a,b):
    c = a+b;
    yield f'first c : {c}'
    c=c+c;
    yield f'secound c : {c}'
    yield generator(a,b)
    yield generator(a,b)

obj = generator(5,6)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))