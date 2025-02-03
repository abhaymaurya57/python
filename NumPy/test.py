import numpy as np

# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), 
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
           
# Creating array
arr = np.array(values, dtype = dtypes)
# print ("\nArray sorted by names:\n",
#             np.sort(arr, order = 'name'))
            
print ("Array sorted by graduation year and then cgpa:\n",
                np.sort( arr,order = ['grad_year', 'cgpa']))