import numpy as np
# arr = [1, 2, 3]
# arr = ([[1, 2, 3],'e', [4, 5, 6]])

# for x in arr:
#   print(x)

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in arr:
#   for y in x:
#     for z in y:
#         print(z)

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#   print(x)

# arr = np.array([1, 2, 3])

# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for x in np.nditer(arr[:, ::2]):
#   print(x)

# arr = ([1,2,3,4,5,6,6])
# data = arr[::3]
# print(data)

# arr = np.array([1, 2, 3])

# for idx, x in np.ndenumerate(arr):
#   print(idx, x)

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.concatenate((arr1, arr2))
# arr1 = np.append(arr1,arr2)
# print(arr1)
# print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2),axis = 1)
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.stack((arr1, arr2),axis = 1)
print(arr)
