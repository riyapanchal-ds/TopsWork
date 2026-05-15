#while loops
#print 1 to 10 with while loops

'''i=1
while i<11:
 print(i)
 i+=1'''


#multiplication table
'''num=int(input("enter number"))
mul=1
for i in range(1,11):
    mul=num*i
    print(f"{num}*{i} = {mul}")'''

#leap year  ---year divided by 4 not divided by 100 or year divided by 400

'''year=int(input("enter year"))
if year%4==0 and year%100!=0 or year%400==0:
    print(f"{year}year is leap year")
else:
     print(f"{year}year is not leap year")'''


'''for year in range(1990,2026):
 if year%4==0 and year%100!=0 or year%400==0:
    print(f"{year}year is leap year")
else:
     print(f"{year}year is not leap year")'''