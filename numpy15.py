# Functions in Nympy array 2 -->
import numpy as np

var = np.array([1,2,3,4,5])

np.random.shuffle(var)
print(var)

print()

var1 = np.array([1,2,3,4,5,4,5,6,7,8])
x = np.unique(var1 , return_index = True , return_counts = True)
print(x)

print()

var2 = np.array([1,2,3,4,5,6])
y = np.resize(var2,(2,3))
print(y)

print()

print(y.flatten())

print()

print(y.flatten(order = 'F'))

print()

print(np.ravel(y,order='A'))

