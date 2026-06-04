#FOR LOOPS    repeatation
#ex1
'''for m in range(4):
    print("hello")'''
#ex2
'''for m in range(4):
    print("hello",m)'''
#EX3
'''for i in range(11,20):
    print(i)'''

#EX4
'''for i in range(11,20):
    print("hello",i)'''
    
#start from 100 and ends at 150 print alternate number
'''for i in range(100,150,5):
    print(i)'''

#reverse
'''for i in range(150,100,-10):
    print(i) '''

'''sum=0   #initialize value koi bi le sakte he kon se type ki he ye batane ke liye
for i in range(1,11):
    #sum=sum+i
     sum+=i 
print(sum)'''

'''mul=1
for i in range(1,11):
    mul=mul+i
    print(f"multiplication of 1-10 number in {mul}")'''

#FACTORIAL NUMBER
'''num=int(input("enter number"))
ans=1
for i in range(num,0,-1):      #reverse hoga 
#for i in range(1,num+1):
    ans=ans*i
    print(i)
print(f"factorial of {num} is {ans}")'''

#check wherether given number is prime number or not

'''num=int(input("enter number"))
for i in range(2,num):
    if num%i==0:
        print(f"not a prime number{num}")
    else:
        print(f"number is prime number{num}")
        
    break'''


#sum of number is 100 odd or even

'''sum=0
for i in range(2,101,2):
        sum=sum+i
        print(f"number is even{i},total even num {sum}")'''
        

'''i=1
while i<=5:
    print(i)
    i=i+1'''



#list in for loops
'''lst_numbers=[2,56,78,90,56,44]
print(lst_numbers)
for i in lst_numbers:
    print(i)'''

#sum in lst
'''lst_numbers=[2,56,78,90,56,44]
print(lst_numbers)
sum=0
for i in lst_numbers:
  sum=sum+i
  print(i) 
print(f"sum={sum}")



lst_names=['riya','mital','jenish']
for i in lst_names:
   print(i)

lst_names=['riya','mital','jenish']
print(f"Length of list{len(lst_names)}")
for i in lst_names:
   print(i)



lst_names=['riya','mital','jenish']
print(f"{len(i)}")
for i in lst_names:
   print(i)

   
lst_names=['riya','mital','jenish']
print(f"Length of list{len(lst_names)}")
for i in lst_names:
   print(i)
print(f"length of {i} is {len(i)}")



name=input("enter name")
for i in name:
   print(i)'''