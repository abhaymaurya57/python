import numpy as np

arr1 = np.array([[1, 2, 3],[2,4,5]])

arr2 = np.array([[4, 5, 6],[3,4,5]])

arr = np.concatenate((arr1, arr2),axis =1)
print(arr)

arr1 = np.stack((arr1, arr2), axis=1)
print(arr1)
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])
arr3 = np.hstack((arr1, arr2))

print(arr3)
arr4 = np.array([1, 2, 3])

arr5 = np.array([4, 5, 6])

arr4 = np.vstack((arr4, arr5))

print(arr4)
arr1 = np.array([7,8,9])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)