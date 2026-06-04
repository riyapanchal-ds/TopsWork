#find compond intrest. amount=p(1+r/100)t compound intrest is =A-p

p=int(input("enter number"))
r=int(input("enter number"))
t=int(input("enter number"))

A=p*(1+r/100)**t
CI=A-p
print(f"amount is {A}")
print(f"compound intrest is {CI}")
