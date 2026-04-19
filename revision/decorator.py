
def deco(func):
    def wrapper(*args, **kwargs):
        print("before the table.")
        func(*args, **kwargs)
        print("after the table.")
    return wrapper

@deco
def table_print(n):
    for i in range(1,11):
        print(f'{n} X {n} = {n*i}')
        # print(i)

table_print(10)