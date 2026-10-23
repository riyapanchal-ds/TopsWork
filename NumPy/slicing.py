import numpy as np
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr3)

# print(arr3[::,1:2])     #slicing on columns
# print(arr3[::,0:1])

print(arr3[0:2:,0:1])           #rows and columns

print(arr3[2::,1:2])
print(arr3[2::,0:1])

print(arr3)