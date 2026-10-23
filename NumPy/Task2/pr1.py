import numpy as np

#1. create a 1D numpy array ([10,20,30,40,50])
#first element
#second element using negative indexing
arr=np.array([10,20,30,40,50])
print(arr[0])
print(arr[-1])

#2.given array arr=np.array([5,10,15,20,25,30])
#extract element from index 1 to 4 using slicing
arr=np.array([5,10,15,20,25,30])
print(arr[1:5])

#3.given array arr=np.array([0,2,4,6,8,10])
#extract every second element using stop slicing
arr=np.array([0,2,4,6,8,10])
print(arr[::2])

#4. create a 2D array :[[1,2,3],[4,5,6],[7,8,9]]
#print the element located ar:rows2,column1 (using proper indexing)
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[2:,1])

#5. using the same 2D array from question,extract the first two rows
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0:2])

#6. using the same 2d array extract the submatrix:[[2,3],[5,6]]
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0:2,1:3])

#7 create array:arr=[10,20,30,40,50]
#using fancy indexing extract
#1st element, 2rd elemen, 5th element

arr=np.array([10,20,30,40,50])
print(arr[[0,2,4]])

#8. create array:arr[5,10,15,20,25]
#using boolean indeing, greater than 12
arr=np.array([5,10,15,20,25])
print(arr>12)
print(arr[arr>12])

#9. given array arr=[3,6,9,12,15]
# use np.where() to find indices where values are greater than 8
arr=np.array([3,6,9,12,15])
print(np.where(arr>8))
print(arr>8)

# 10. create array arr=[1,2,3,4,5]
# reverse the array using slicing
arr=np.array([1,2,3,4,5])
print(arr[::-1])

# 11. create array a=[2,4,6] b= [1,2,3]
# element wise multiplication
# element wise power(a squared)

a=np.array([2,4,6])
b=np.array([1,2,3])
print(a*b)
print(a**b)

# #12. create array arr=[4,9,16,25]
# square root
# mean
# maximun value
arr=np.array([4,9,16,25])
print(np.sqrt(arr))
print(np.mean(arr))
print(np.max(arr))