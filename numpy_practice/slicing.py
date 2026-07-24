import numpy as np

array = np.array([[1, 2, 3 ,4], 
                  [5, 6, 7, 8],
                    [9, 10, 11, 12], 
                    [13, 14, 15, 16]])
#array[start:end:step]


# print(array[0]) #first row 
# print(array[-1]) #last row
# print(array[0:3]) #first three rows
# print(array[0:4:2]) #every second row
# print(array[::-1]) #return the array in reverse 

#Column Selection
# print(array[0, 0]) #first row first column
# print(array[:, 0]) #all rows access column 0
# print(array[:, -1]) #last column
# print(array[:4, :3]) #first three columns
# print(array[:, 1:]) #columns two to four

#Row and Column Selectiom
print(array[0:2, 0:2]) #first two rows, first two columns
print(array[0:2, -2:]) #first two rows, last two columns
print(array[-2:, :2]) #last two rows, first two columns