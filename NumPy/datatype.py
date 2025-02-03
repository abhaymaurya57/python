import numpy as np
# arr = np.array([1,2,3,4])
# print(arr.dtype)

# arr = np.array(['apple', 'banana', 'cherry'])

# print(arr.dtype)

# arr = np.array([1, 2, 3,9,8, 4], dtype='S')

# print(arr)
# print(arr.dtype)
# import numpy as np

# arr = np.array([1, 2, 3, 4], dtype='S')

# print(arr)
# datastr = arr.str()
# print(datastr)

#str to byte
# s = '123'
# n= s.encode('utf-8')
# t= n.decode('utf-8')
# print(t)
# print(type(t))

#float to int
# arr = np.array([1.1, 2.1, 3.1],'str')
#newarr = arr.astype('i')
# print(arr)
# print(arr.dtype)
# print(datatype.dtype)
arr = np.array([2, 1, 3])

newarr = arr.astype(float)

print(newarr)
print(newarr.dtype)