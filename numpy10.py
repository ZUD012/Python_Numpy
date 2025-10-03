# Indexing and slicing in numpy array Python -->
import numpy as np

# Indexing -->

var = np.array([9,8,7,6])
print(var[1])

var2 = np.array([[1,5],[2,3]])
print(var2[1][0])

# SLICING -->
v = np.array([1,2,3,4,5])
print(v[1:4:1])
print(v[1:])
print(v[:5])
print()

vi = np.array([[1,2,3,4],[2,3,4,5]])
print(vi[1,:])

vip = np.array([[[1,2,3],[2,3,4]],[[2,3,4],[3,4,5]]])
print(vip[0,1,-1:-4:-1])