#crate a function which return simple interest prn/100

def interest(p,r,n):
    return p*r*n/100
ans=interest(10000,0.10,10)
print(ans)

#exponent 
def exponent(num1,num2):
    return num1** num2
ans=exponent(2,3)
print(ans)

#create to check number is even odd
def odd_even(no1):
    return no1%2==0              #first way
       
ans=odd_even(44)
print(ans)

#SECOND WAY
def odd_even(no):
    if no%2==0:
        return"even"
    else:
        return"odd"
def iseven(no):
    return no%2==0
print(odd_even(10),iseven(10))
print(odd_even(101),iseven(101))