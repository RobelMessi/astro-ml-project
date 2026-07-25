import numpy as np

rng = np.random.default_rng()

print(rng.integers(low = 1, high = 101, size = (3, 2))) #second number is exclusive
print(np.random.uniform()) #random floating point number from 0 to 1
print(np.random.uniform(low = -1, high = 1, size = (3,2))) 


array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array) #shuffles the array in random order
print(array)

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruit = rng.choice(fruits) #choose one random fruit from the array
fruits = rng.choice(fruits, size = 3) #choose 3 random fruits
print(fruit)
print(fruits)