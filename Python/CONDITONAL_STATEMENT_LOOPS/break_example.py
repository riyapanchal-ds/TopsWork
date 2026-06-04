'''i=1
while i<=10:
    if i==9:
        break
    print(i)
    i+=1
print("out of while")'''



num=int(input("enter number"))
temp=0
for i in range(2,num):
    if num%i==0:
        print("prime number")
        temp==1
        break
    else:
        temp==0
if temp==0:
    print("prime number")
        
  
