# Numpy Array Functions -->
import numpy as np 

var1 = np.array([1,2,3,4,5,3,45,2])

x = np.where( var1 == 2 )
print (x) 

print()

var = np.array([1,2,4,5,6,7,8,10,11,15])
c = np.searchsorted(var , 9)
print(c)

print()

var2 = np.array([1,2,3,55,45,2])
x = np.sort(var2)
print(x)

h = np.array([2,3,4,1])
f = [True,False,False,True]
newh = h[f]
print(newh)