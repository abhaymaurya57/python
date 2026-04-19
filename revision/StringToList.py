s1 = "abhay,"
print(s1)
print(type(s1))
lst=[]
lst=list(s1)
print(lst)

# conversrt string
newstr = ''.join(lst)
print(newstr)
print(type(newstr))
# remove the comma
# return none
newstr1 =lst.remove(',')

print(newstr1)
print(lst)

## ******* Output *********8
''' 
abhay,
<class 'str'>
['a', 'b', 'h', 'a', 'y', ',']
abhay,
None
['a', 'b', 'h', 'a', 'y']
<class 'str'>

'''