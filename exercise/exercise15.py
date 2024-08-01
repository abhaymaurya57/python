numbers=input('Enter the number:')
number = numbers.split()
print(number)
count = 0
for i in number :    #for  i in number 
    count = count+1
print(count)
for i in range(0,count):
    number[i]=int(number[i])
print(number) 

maximum_number = numbers[0]
for num in numbers:
    if num > maximum_number :
        maximum_number = num
print(f"The maximum number is :{maximum_number}")