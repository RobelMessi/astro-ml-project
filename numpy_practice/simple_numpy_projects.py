import numpy as np


#Excercise 1

# Generate a 100 x3 array of random floating-point numbers representing 3D spatial coordinates
# (x, y, z) between -50 and 50

rng = np.random.default_rng()
array_1 = rng.uniform(low = -50.0, high = 50.0, size = (100,3) ) #floating point integers from -50.0 to 50.0

print(array_1)


#Excercise 2
# Compute the 3D Euclidean distance from the origin for all 100 points
squaring = array_1 **2 #squares every number in the array
summation = np.sum(squaring, axis = 1) #axis = 1 sums horizontally down the rows, giving you one-hundred totals
square_root = np.sqrt(summation)
print(square_root)

