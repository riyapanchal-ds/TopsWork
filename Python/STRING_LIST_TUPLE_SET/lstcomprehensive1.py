lst1=[1,2,3,4]
ans=[]
for i in lst1:
    ans.append(i**3)
print(ans)



#list comphrehensive        #always start from square bracket
lst1=[1,2,3,4]
ans=[]
ans=[i**2 for i in lst1]
print(ans)


lst_city=['surat','ahmedabad','rajkot']
lst_upper=[i.upper() for i in lst_city]
print(lst_upper)

lst_len=[len(i) for i in lst_city]
print(lst_len)

#squar of element f element is even
ans1=[]
for i in lst1:
    if i%2==0:
     ans1.append(i**2)
print(ans1)


#list cpehhensive
ans1=[]
ans1=[i**2 for i in lst1 if i%2==0]
print(ans1)


#upper of city if city length is more than five
ans2=[]
ans2=[i.upper() for i in lst_city if len(i)>5]
print(ans2)

