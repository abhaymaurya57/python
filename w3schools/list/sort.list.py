list = ['a','j','c','x','e','f']
list.sort()
print(list)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

###############33

# sort descending
thislist = [100, 50, 500, 82, 23]
thislist.sort( reverse = True)
print(thislist)

##############
# sort sunction
def myfunct(n):
    return abs(n-50)
list = [100,43,644,242,764]
list.sort(key = myfunct)
print(list)

###########3 case sensitive sorting#3
thislist = ["Banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist.sort(key = str.upper)
print(thislist)

#########reverse order####
thislist = ["banana", "Orange", "Kiwi", "cherry",6,4,7,9,12]
thislist.reverse()
print(thislist)