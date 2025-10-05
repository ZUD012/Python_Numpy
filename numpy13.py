# Joining and spliting Numpy arrays -->

import numpy as np

# For 1D array -->

a = np.array([1,3,5,4,2])
b = np.array([4,3,6,4,2])
ar = np.concatenate((a,b))
print(ar)
print()

# For 2D array -->
c = np.array([[1,3,5],[1,4,2]])
d = np.array([[4,3,6],[3,4,2]])
ap = np.concatenate((c,d),axis = 1)
ap1 = np.concatenate((c,d),axis = 0)
print(ap)
print()
print(ap1)
print()

# Stack function -->

a_1 = np.array([1,3,5,4,2])
b_1 = np.array([4,3,6,4,2])
ar_1 = np.stack((a,b) , axis = 1 )
ar_3 = np.hstack((a,b))
ar_4 = np.vstack((a,b))
ar_5 = np.dstack((a,b))
print(ar_1)
print()
print(ar_3)
print()
print(ar_4)
print()
print(ar_5)
print()

# Split Array Function -->
a_2 = np.array([1,3,5,4,2])
spl = np.array_split(a_2 , 3)
print(spl)
print(spl[0])

print()

a_3 = np.array([[1,3,5],[1,4,2]])
spl1 = np.array_split(a_3 , 2 , axis = 1 )
print(spl1)
print(spl1[0])