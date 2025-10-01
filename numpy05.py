# datatypes in python -->

import numpy as np

var = np.array([1,2,3,4 , 5,6,7,8,9,10,11,12,13,14,15,16,117])
print("Datatype : ", var.dtype)  

var1 = np.array([1.1 ,1.0 , 1,2 ,1.3 , 1.4])
print("Datatype :", var1.dtype)

var2 = np.array(["a" , "b" , "c" , "d"])
print("Datatype : ", var2.dtype)

var3 = np.array([1.1 ,1.0 , 1,2 ,1.3 , 1.4 , "a" ," B"])
print("Datatype : ", var3.dtype)

x = np.array([1,2,3,4],dtype = np.int8) # Changing datatype in python from 32 bit to 8 bit .
print("Datatype : ", x.dtype)

x1 = np.array([1,2,3,4],dtype = "f") # Changing datatype in python from int to float .
print("Datatype : ", x1.dtype)

x3 = np.array([1,2,3,4],)
new = np.float32(x3)
print(new)
print("Datatype : ", x3.dtype)
print("Datatype of new : ", new.dtype)


x4 = np.array([1,2,3,4,5,6,7,8,9,10])
new_1 = x4.astype(float)
print(x4)                                         # Direct Conversion -->
print(new_1)                                         # Direct Conversion -->

