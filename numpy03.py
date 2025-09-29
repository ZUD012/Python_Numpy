# creatinng an array using diffrent methods -->

import numpy as np

ar_empty = np.empty(4) # Creating an empty array -->
print(ar_empty)

arr_zero = np.zeros(4) # Creating an array with all elements are zero --> 
arr_zero1 = np.zeros((3,4)) 

print(arr_zero)
print()
print(arr_zero1)

print()

arr_ones = np.ones(4) # creating an array with all elements equal to 1 -->
print(arr_ones)

print()

arr_arrange = np.arange(4) # creating an array where num are in order start from 0 to n-1 -->
print(arr_arrange)

print()

arr_dia = np.eye(3) 
print(arr_dia)

print()

arr_diago = np.eye(3,5)
print(arr_diago)

print()

arr_lin = np.linspace(0,10,num = 5) # continuous gaph between the elements -->
print(arr_lin)