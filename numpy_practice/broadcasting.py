import numpy as np

#Broadcasting allows NumPy to perform operations on arrays 
#with different shapes by virtually expanding dimensions
#so they match the larger array's shape

#The dimensions have the same size.
# OR
# One of the dimensions have a size of 1

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])
array3 = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8]])
print(array1.shape)
print(array2.shape)
print(array3.shape)

print(array1 * array2)
#print(array2 * array3) #Can't broadcast because of a mismatch, 2 and 4 don't match and neither of them are 1

array4 = np.array([[1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]])
array5 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(array4.shape)
print(array5.shape)
print(array4 * array5)