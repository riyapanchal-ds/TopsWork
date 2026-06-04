a=lambda x,y,z:x+y+z
print(a(20,30,20))

square=lambda x:x**2
lst1=[1,2,3]
lst2=[]
for i in lst1:
    lst2.append(square(i))
print(lst2)


#odd even
ans=lambda num:"even" if num%2==0 else "odd"
print(ans(561))