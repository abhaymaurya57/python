import numpy as np
# from numpy import random
import random

x = random.randint(1,100+1)
# x=3,4,5,7,5
arr = np.array([x],dtype='S')
print(arr)
print(arr.dtype)

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Integer array indexing 
indices = np.array([1, 3, 5])
print ("Integer array indexing:", arr[indices])

# boolean array indexing 
cond = arr > 0
print ("\nElements greater than 0:\n", arr[cond])