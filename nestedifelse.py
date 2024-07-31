number = int(input('Enter a number:'))
if number%2==0:
    print('number is even')
    if number/2:
        print('number is divisible by 2 ')
        if (number * number == number**2):
            print('true statment')
        else:
            print('false statment')
    else:
        print('number is not divisible by 2')
else:
    print('number is odd')