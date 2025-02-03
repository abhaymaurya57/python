import numpy as np
# arr = np.array([1,2,3,4,5])
# print(type(arr))


#2D array
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

#3d array
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(arr)

# #chek how many dimensions the array
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


# arr = np.array([1, 2, 3, 4], ndmin=2)

# print(arr)
# print('number of dimensions :', arr.ndim)

# arr = np.array([1, 2, 3, 4])

# print(arr[3]+arr[2])

#Access the element on the first row, second column:
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st row: ', arr[0, 1])
# print( arr[1, 3])

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('5th element on 2nd row: ', arr[1, 4])

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr)
# print(arr[1,1,1])
# print(arr[1, 0, 1])

# 

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[4:])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[:4])

#STEP
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:1])