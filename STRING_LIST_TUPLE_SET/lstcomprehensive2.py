lst_number=[1,2,3,4,33,67]
lst_ans=[i**2 for i in lst_number if i%2==0]
print(lst_number)

#print even if no is even else print odd
ans=["even" if i%2==0 else "odd" for i in lst_number]
print(ans)

#calculate square of no if number is even else calculate cube
ans2=[i**2 if i%2==0 else i**3 for i in lst_number]
print(ans2)

#convert city name into upper if length of city is more then 5 leter else convert into lower
lst_city=['surat','ahmedabad','rajkot']
ans3=[i.upper() for i in lst_city if len(i)>5]
print(ans3)