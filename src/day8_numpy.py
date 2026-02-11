# Task 1: The Normalizer (Broadcasting & Stats)
import numpy as np
arr = np.random.randint(50, 100, size=(5, 3))
m = np.mean(arr,axis=0)
print("Original scores:\n",arr)
sub = arr-m
print("Centered scores:\n",sub)

#Task 2: The Reshaper (Array Manipulation)
ar = np.arange(0,24)
print(ar)
b = ar.reshape(4,3,2)
print("Reshaped: \n",b)
c = b.transpose(0,2,1)
print("Transposed:\n",c)
print("Final shape: ",c.shape)
