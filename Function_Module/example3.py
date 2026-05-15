# #create function to perform addition
# def addition(no1,no2):
#     print(no1+no2)
 
# addition(90,120)

#user
'''def addition(no1,no2):
    print(no1+no2)
 
no1=int(input("enter number"))
no2=int(input("enter another number"))
addition(no1,no2)

#create function to perform addition and substrction
def addition(no1,no2):
    print(no1+no2)

def subtrction(no1,no2):
    print(no1-no2)

no1=int(input("enter number"))
no2=int(input("enter another number"))

addition(no1,no2)
subtrction(no1,no2)'''


def addition(no1,no2):
    return(no1+no2)

def subtrction(no1,no2):
    print(no1-no2)

no1=int(input("enter number"))
no2=int(input("enter another number"))

ans=addition(no1,no2)
print("addition",ans)
if no1>=100:
 subtrction(no1,no2)