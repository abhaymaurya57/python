import numpy as np

# arr = np.array([1,2,3,4,5,6])
# x = arr.copy()
# x = arr.view()
# arr[5]=100
# print(arr)
# print(x)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# x[0] = 31

# print(arr)
# print(x)
# arr = np.array([1, 2, 3, 4, 5])

# x = arr.copy()
# y = arr.view()

# print(x)
# print(y)

# print(x.base)
# print(y.base)

# print(int('78341',16))

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr.shape)

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('shape of array :', arr.shape)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(4, 3)

# print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)