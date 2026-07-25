import numpy as np


#Excercise 1

# Generate a 100 x3 array of random floating-point numbers representing 3D spatial coordinates
# (x, y, z) between -50 and 50

rng = np.random.default_rng()
array_1 = rng.uniform(low = -50.0, high = 50.0, size = (100,3) )
array_2 = rng.integers(low = -50, high = 50, size = (100,3) )
array_3 = rng.integers(low = -50, high = 50, size = (100,3) )
print(array_1)