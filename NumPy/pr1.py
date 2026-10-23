import numpy as np
list = [1,2,3,4]
print(list)

#conver list to array
arr_list1 = np.array(list)
print(arr_list1)

print(type(arr_list1))       #1 diamentional array
print(arr_list1.ndim)
print('------------------------------------------')

list1 = [1,2,3]
list2 =[4,5,6]

arr_list2 = np.array([list1,list2])
print(arr_list2)                                     #2 diamentional array
print(arr_list2.ndim)

print('------------------------------------------')
list1 = [1,2,3]
list2 =[4,5,6]
list3 =[7,8,9]
arr_list3 = np.array([[list1,list2,list3]])
print(arr_list3)                                #3 diamentional array
print(arr_list3.ndim)                               
print('------------------------------------------')

#numpy array attributes
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)

print("shape",arr1.shape)
print("size",arr1.size)
print("dType",arr1.dtype)
print("dim",arr1.ndim)

print('------------------------------------------')

arr3=np.array([[1,2,3],[7,4,5],[7,8,9]])
print(arr3)

print("shape",arr3.shape)
print("size",arr3.size)
print("dType",arr3.dtype)
print("dim",arr3.ndim)


print('------------------------------------------')

zero_arr = np.zeros((2,5))
print(zero_arr)

full_arr = np.full((3,2),7)
print(full_arr)

print('------------------------------------------')
arr = np.empty((2, 2))

print(arr)
