lst = [123,234,345,456,565,678,789,890]
print(lst)

lst.sort()
print("sort  : ",lst)   # None : usi list ko modify karta hai

lst.sort(reverse=True)
print("sort reverse: ",lst)

def fun(key):
    return int(str(key)[::-1])

lst.sort(reverse=True,key=fun)
print("sort reverse: ",lst)

#------------------------------------------------

# lst = [123,234,345,456,565,678,789,890]
# print(lst)

# res = sorted(lst)
# print("sorted  : ",res)  

# res1 = sorted(lst,reverse=True)
# print("sorted reverse: ",res1)
# print(lst[::-1])

# def fun(n):
#     return  int(str(n)[::-1])

# res2= sorted(lst,key=fun)
# print("sortrd reverse: ",res2)