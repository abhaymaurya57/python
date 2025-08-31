import numpy as np
arr = np.array([1,2,3,4,5])
print(type(arr))
print(arr.dtype)


#2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.shape)
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(arr.reshape(2,2,-1))
#3d array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

#chek how many dimensions the array
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


arr = np.array([1, 2, 3, 4], ndmin=2)

print(arr)
print('number of dimensions :', arr.ndim)

arr = np.array([1, 2, 3, 4])

print(arr[3]+arr[2])

#Access the element on the first row, second column:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
print( arr[1, 3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[1,1,1])
print(arr[1, 0, 1])



arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

#STEP
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:1])  #[2 3 4 5]
print(arr[1:5:-1])  # []
print(arr[-1:-5:-2])  #[7 5]
print(arr[1:5:2])  #[2 4]
print(arr[-1:-5:-1])  #[7 6 5 4]

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr[0, :])     # first row -> [1 2 3]
print(arr[:, 1])     # second column -> [2 5 8]
print('secound column',arr[1,:])
print('3rd column',arr[2,:])  
print('secound column ',arr[1,::-1])
print('3rd column',arr[2,0:1]) 
print(arr[1:, :2])   # submatrix -> [[4 5]
                     #               [7 8]]

srt=np.array([('abhay',20,12),('kushwaha',12,43),('kush',32,23),('tttrr',12,21)],  dtype=[('name', 'U10'), ('age', 'i4'), ('height', 'f4')])
aa=np.sort(srt,order=['height'])
print(aa)