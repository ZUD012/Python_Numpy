import numpy as np 

a = np.array([1,2,3,4])
b = np.array([1,2,3])

# print(a + b ) This shows broadcasting error . 

c = np.array([[1],[2],[3],[4]])
d = a+c
print(a+c)
print(d.shape)

x = np.array([[1],[2]])
y = np.array([[1,2,3],[1,2,3]])
v = x+y
print(x+y)
print(v.shape)