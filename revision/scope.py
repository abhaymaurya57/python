def fun(*num):
    sum1=0;
    for i in num:
        sum1+=i
    def fun2(*num2):
        sum2=0
        for i in num2:
            sum2+=i
        return sum1+sum2
    return fun2

f2 = fun(1,2,3,4,5)
print(f2)
print(f'f2{f2}')
f3 =f2(1,2,3,4,5)
print(f'f3 : {f3}')