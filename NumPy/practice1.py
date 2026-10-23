#np.unique
import numpy as np
arr=np.array([1,2,2,3,3,3,4,4,5])
unique_value=np.unique(arr)
print(np.array(arr))
print("orignal array:",arr)
print("unique values:",unique_value)
print("------------------------------")

#np.sort()
arr=np.array([30,50,40,10,20])
sorted_array=np.sort(arr)
print("orignal array:",arr)
print("sorted array:",sorted_array)
print("------------------------------")

#np.argsort()
arr=np.array([30,50,40,10,20])
indexes=np.argsort(arr)
print("indexes:",indexes)
print("------------------------------")

#np.where()
arr=np.array([10,20,30,40,50])
result=np.where(arr>30,1,0)           #true=1 #false=0
print("result:",result)
print("------------------------------")

#np.nonzero()
arr=np.array([0,5,0,8,10,0])
print(np.nonzero(arr))
print("------------------------------")

#np.any()       #ek true hoy to true j aape
arr=np.array([False,False,False,True])
print(np.any(arr))
arr=np.array([10,20,30,40,50])
print(np.any(arr>25))
print("------------------------------")

#np.all()        #ek false hoy to true j aape
arr=np.array([True,False,True])
print(np.all(arr>20))
arr=np.array([10,20,30,40,50])
print(np.all(arr>20))
print("------------------------------")

#np.clip()
arr=np.array([5,10,15,20,25])
result=np.clip(arr,10,20)
print(result)

