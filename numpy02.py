# Creating Array in python using numpy -->
import numpy as np
a = np.array([1,4,3,5,2])
for i in a :
    print(i)

x=[1,3,5,2,3] #Converting a list into array -->
y = np.array(x)
print (y) 
print(type(y))

l=[]

for i in range(1 , 5):
     int_1 = int(input("ENter the Value : "))
     l.append(int_1)

diman = np.array(l)
print(diman)
print(diman.ndim) #ndim function to find dimension of array -->

arr_2 = np.array([[1,2,3,4] , [1,2,3,4]])
print(arr_2)
print(arr_2.ndim)

arr_3 = np.array([[[1,2,3,4],[3,2,5,4],[1,3,2,6]]])
print(np.array(arr_3))
print(arr_3.ndim)

n_dim = np.array([1,2,3,4],ndmin = 10)
print(n_dim)
print(n_dim.ndim)