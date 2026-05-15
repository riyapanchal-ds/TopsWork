#arithmatic operators +,-,*,/,%(modulus reminder)),**(exponent),//(floor division)

# print(f"{4/2} -- {4%2}")
# print(f"{10/2} -- {10/2}")
# print(f"{100/6} -- {100%6}")
# print(f"{20/4} -- {20%4}")
# print(f"{2**5}")
# print(f"{3**6}")
# print(f"{5**2}")
# print(f"{12/5} -- {12//5}")
# print(f"{100/3} -- {100//3}")
# print(f"{100/5} -- {100//5}")


# no1=int(input("Please enter no1 "))
# no2=int(input("Please enter no2 "))
# sum=no1+no2
# sub=no1-no2
# mul=no1*no2
# div=no1/no2
# print(f"Sum of {no1} and {no2} is {sum}")
# print(f"Substraction of {no1} and {no2} is {sub}")
# print(f"multiplication of {no1} and {no2} is {mul}")
# print(f"division of {no1} and {no2} is {div}")

#relational operator(== , < , > , <= ,>= , !=)
# ans=12>20
# print(ans)

# print(f"{12<20}")
 
# num1=int(input("enter number"))
# num2=int(input("enter another number"))
# print(f"{num1} > {num2} = {num1>num2}")
# print(f"num1 < num2 {num1<num2}")

# print(f"{num1}>= {num2} = {num1>=num2}")
# print(f"num1 <= num2 {num1<=num2}")

# print(f"num1 == num2 {num1==num2}")
# print(f"num1 != num2 {num1!=num2}")


#logical operator (AND, OR ,NOT)
#AND OPERATOR    both condition true output true
# print(12>10 and 12<10)
# print(12<10 and 12<10)
# print(12<10 and 12>10)
# print(12>10 and 12>10)
# print(12>20 and 12>10)

#OR OPERATOR     one condirion true output true

# print(12>10 or 12<10)
# print(12<10 or 12>10)
# print(12<10 or 12<10)
# print(12>10 or 12>10)

# print(12>20 or 12>10)
# print(12<20 or 12<10)


#NOT OPERATOR   reverse true=flase, false=true

# print(not(12<20))
# print(not(12>20))



#assignment operators   (+=, -= ,*=, /=)

# num=int(input("enter value"))
# num+=5
# print(num)
# num-=5
# print(num)
# num*=5
# print(num)
# num/=5
# print(num)
# num//=5
# print(num)
# num**=5
# print(num)





# num=int(input("enter value"))
# print(f"{num}",end="")
# num+=5
# print(f"+= 5 ===== {num}")
# num-=5
# print(f"{num} -= 5 ===== {num}")
# num*=5
# print(f"{num} *= 5 ===== {num}")
# num/=5
# print(f"{num} /= 5 ===== {num}")
# num//=5
# print(num)
# num**=5
# print(num)



#MEMBERSHIP OPERATORS        MEMBER CHE KE NAII EE CHECK KARVA
#IN OR NOT IN
#string
name=input("enter your name")
print("a" in name)

#list of number
lst=['riya','hani','kavya']
print("riya" in lst)
print("mital" in lst)

#list of numeric
lst1=[1,2,3,4,5]
print(2 in lst1)
print(22 in lst1)

lst2=[11,22,33,44]
num=int(input("enter number"))
print(num in lst2)

lst3=[11,22,33,44]         #revese true=false, false= true
num=int(input("enter number"))
print(num not in lst3)



#IDENTITY OPERATORS             CHECK EQUALITY
#IS OR NOT IS(reverse)

num1=12
num2=102
num3=num1
num4=12
print(num1 is num2)
print(num1 is num3)
print(num1 is num4)
print(num1 is not num4)
print(id(num1))
print(id(num2))
print(id(num3))
print(id(num4))
