def check(n):
    if n<=1:
            print("not prime number",i)
    for i in range(2,n):    
        for j in range(i):
            if i%j==0:
                print("this is prime number",i)
        print("this is not prime number",i)         
check(100)

