# Arthemetic functions in numpy Array -->

import numpy as np 

a = np.array([1,2,3,13,13,12])
print(np.max(a))



print(np.min(a))

print()

print(np.argmin(a)) # Position of min element inside the array .

print()

print(np.argmax(a)) # Position of max element inside the array . 

print()

var1 = np.array([[2,3,4] , [3,5,2]])
print(np.max(var1 , axis = 1))

print()

print(np.min(var1 , axis = 0 ))

print()

print(np.argmin(var1)) # Position of min element inside the array .

print()

print(np.argmax(var1))

print()

print(np.sqrt(var1))

print()

print(np.sin(var1))

print()

print(np.cumsum(var1))




