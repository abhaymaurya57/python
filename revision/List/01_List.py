lst = [11,2,2,43,96,65,74,87,52]

lst.append(32)
print(lst)

# lst.clear()
# print(lst)

lstcopy = lst.copy()
print(lstcopy)

lstcopy.append(21)
print(f'lst :  {lst}')
print(f'lstcopy : {lstcopy}')

import copy
deep = copy.copy(l)