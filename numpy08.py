# Learning about shapes and reshaping numpy array -->

import numpy as np


var = np.array([[1,2],[2,4]])

print(var)
print()
print(var.shape) #Tells the row and coloums in array

print()

var1 = np.array([1,2,3,4],ndmin = 4)
print(var1.ndim)
print(var1)
print()
print(var1.shape)

# Reshaping i numpy array -->
var2 = np.array([1,2,3,4,5,6])
print(var2)
print("Dimension : ",var2.ndim)
print()

x = var2.reshape(3 , 2)
print(x)
print("Dimension : ",x.ndim)

v = x.reshape(-1)
print("Dimension : ", v.ndim)
print(v)