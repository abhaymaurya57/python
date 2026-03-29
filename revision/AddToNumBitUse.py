a = 101
b = 10

def sum(a,b):
    while b!=0:
        carry = a&b
        a = a^b
        b=carry<<1
    return a
print(sum(54,2))