# Arthemetic Operations in Array -->

import numpy as np 

var = np.array([1,2,3,4]) # Adding all elements to each element of array -->
varADD = var + 3
print(varADD)

print()

var2 = np.array([1,2,3,4]) # Adding Two arrays -->
TWO_array_add = var + var2
print(TWO_array_add)

print()

a = np.add(var , 10) # Using inbuilt add function .
print (a)

print()

b = np.add(var , var2) # Using inbuilt subtract function .
print(b)

print()

# For 2D array -->

var_n = np.array([[12 , 14 , 3 , 2],[4, 55 , 67 , 89]])
var_n2 = np.array([[2 , 1 , 3 , 2],[4, 5 , 6 , 8]])
varadd = var_n+var_n2
varmulti = var_n*var_n2
print(varadd)

print()

print(varmulti)