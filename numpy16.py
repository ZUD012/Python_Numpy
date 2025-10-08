# Insertion and deletion in numpy array -->

import numpy as np 

var = np.array([1,2,3,4])
print(var)
print(var.dtype)
print(type(var))

var = np.insert(var , 2 , 5)
var = np.insert(var , (2,5) , 15)
var = np.append(var , 2)
print(var )

# 2D array -->
var1 = np.array([[1,2,3],[5,4,7]])
var1 = np.insert(var1 ,2 , 6 , axis = 0 )
var1 = np.append(var1 , [[22,33,21]] , axis = 0 )
vark = np.insert(var1 ,2 , 6 , axis = 1 )
print()
print(var1)
print()
print(vark)
print()

# Delete an array -->
d = np.delete(var1 , 2 , axis = 0)
print (d)