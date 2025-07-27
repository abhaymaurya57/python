names = ['abhay','anoop','alok']
for name in names:
    print(name)
    if name=="anoop":
        break

number=[3,5,24,5,2,6,24]
squares=[]
for i in number:
    square = i**3
    squares.append(square)
print(squares)

def fun():
    number=[3,5,24,5,2,6,24]
    squares=[]
    for i in number:
        squares.append(i**2)
    return squares
print(fun())