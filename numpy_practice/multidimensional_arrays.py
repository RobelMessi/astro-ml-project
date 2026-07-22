import numpy as np
array = np.array('A') #0-Dimensional array
array_1 = np.array(['A', 'B', 'C']) #1-Dimensional array

array_2 = np.array([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]) #2-Dimensional array

array_3 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', "_"]]]) #3-Dimensional array

word = array_3[0,0,0] + array_3[2,0,0] + array_3[2,0,0]
print(word)


print(array_3.ndim) #Number of dimensions
print(array_3.shape) #Return a tuple representing the depth, # of rows, # of columns
print(array_3[1,1,1])

