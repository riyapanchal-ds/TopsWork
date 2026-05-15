#write a python program to sum of the first n positive number.

num=int(input("enter number"))                        
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)  #1+2+3+4+5