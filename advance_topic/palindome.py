def palindrome(x):
    print(x)
    x=str(x)
    y=x[::-1]
    print(y)
    print(type(y))
    x=int(y)   # error generste 121-
    print(type(x))

palindrome(12345)
# palindrome(-121)