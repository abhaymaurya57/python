lst=[1,2,3,4,5]

lst.append(6)
print(lst)

# lst.clear()
# print(lst)

newlst = lst.copy()
print(newlst)
print(lst.count(2))

# lst.extend(newlst)
# print(lst)

print(lst.index(6))

lst.insert(0,100)
print(lst)

print(lst.pop())
print(lst)

print(lst.pop(0))
print(lst)

print(lst.remove(5))
print(lst)

print(lst.reverse())
print(lst)

print(lst.sort())
print(lst)