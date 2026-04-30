import copy

# lst =[[1,2],[3,4]]

# shallow = copy.copy(lst)

# print(shallow)
# shallow[0][0]=100
# print(lst)

# deep = copy.deepcopy(lst)

# deep[0][0]=100
# print(deep)
# print(lst)

lst2 = [1,2,3,4,5]

# shallow = copy.copy(lst2)
# shallow[0] = 100
# print(f'shallow {shallow}')

deep =copy.deepcopy(lst2)
deep[0] =100
print(f'deep {deep}')
print(lst2)