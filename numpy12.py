# Copy and View in Numpy Array -->
import numpy as np
var = np.array([1,2,3,4])
co = var.copy()
print(var)                                                                                                                                                                                                 
print()                                                                                                                                                                                                 
print(co)                     
print()                     


x =  np.array([9,8,7,6,5])
vi = x.view()
print(x)
print()
print(vi)

# Diffrence -->
# In copy data copies in new location .
# if data is changed in copy no data change in copied data , 
# whereas in the case of view if we change data in original the changes can be also seen in the original data .