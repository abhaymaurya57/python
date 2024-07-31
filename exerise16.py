number = range(2,101,2)
sum = 0
for i in number:
    sum =sum + i
print(sum)

# or
numbers = range(2,101)
sum = 0 
for i in numbers:
    if i%2==0:
        sum = sum+i
print(sum)  