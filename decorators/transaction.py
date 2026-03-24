def transaction(fun):
    def wrapper(*key,**kwargs):
        sum1 = 0
        for i in key:
            sum1+=i
        print("before transaction")
        fun(*key,**kwargs)
        print("after transaction")
        return sum1
    return wrapper


@transaction
def fun(*args):
    print(f"transaction value are : {args}")

result =fun(2,3,4,5,6)
print(result)