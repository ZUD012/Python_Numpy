# Iteration In Numpy array In Python -->

import numpy as np 

var = np.array([9,8,7,6,5,4])
print()
for i in var :
    print(i)

print()

# Using For loop -->

var1 = np.array([[1,2,3],[2,3,4]])
print(var1)
print()
for j in var1:
    print(j)

print()
for k in var1 :
    for l in k :
        print(l)
    print()

var3 = np.array([[[1,2,3,5],[1,2,3,4]],[[1,2,3,3],[2,3,4,5]]])
for m in var3:
    for g in m :
        for r in g :
            print(r)
    print()

# Using a function -->
for i in np.nditer(var3):
    print(i)
print()

# also showing indexing while iteration -->
for i,d  in np.ndenumerate(var3):
    print(i , d)
print()

# Changing datatype of output -> 

for i in np.nditer(var3,flags=["buffered"],op_dtypes=["S"]):
    print(i)