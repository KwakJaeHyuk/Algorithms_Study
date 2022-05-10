import numpy as np 
import torch

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

# dot product
ans1 = np.dot(x,y)

# Hadamard product
ans2 = x*y

print(x)
print(y)
print(ans1)
print(ans2) 