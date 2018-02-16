# Importing numpy package as np
import numpy as np

# Initialising an random numpy array with size of 15 between (0-20)
vec = np.random.randint(0,20, size=15)
# Printing the array
print("Randomly generated array:")
print(vec)
# Counting the similar items
counts = np.bincount(vec)
# Priting the ones that appears frequently
print("Number that appears frequently:")
print(np.argmax(counts))