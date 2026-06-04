# 1---FUNCTION WITHOUT PARAMETERS
#CREATE OR DEFINE FUNCTION
def greetings():
    print("welcome to python")
    #USE OR CALL THIS FUNCTION
greetings()

# 2---FUNCTION WITH PARAMETERS 
def add2numbers(a,b):
    result=a+b
    print("the sum is:",result)
add2numbers(5,3)

#add2numbers(a=10,b=15)

def add3numbers(a,b,c):
    result=a+b+c
    print("the sum is:",result)
add3numbers(5,3,4)


#FUNCTION WITH RETURN STATEMENT
def add2num(a,b):
    return a+b
    #return a-b   --->after return statement function ends
sum=add2num(10,2)
print(sum)

# function to convert to celsius to fahrenheit with return statement
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
#call function
temp_f = celsius_to_fahrenheit(25)
print(temp_f)
print("with return:",type(temp_f))

#with return statement
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    print(fahrenheit)      #print use kriye etle none aave che
#call function
temp_f2=celsius_to_fahrenheit(50)
print("without return:", type(temp_f2))

#PASS FUNCTION
def kucbhi():
    pass
print("hello")
