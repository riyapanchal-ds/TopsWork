# IF ELSE INSIDE IF ELSE CALLED NESTED IF ELSE
#MULTIPLE CONDTIONS DEPEND ON EACH OTHER
#positive,negative, and positive he to odd/even

number = int(input("enter a number :"))
if number > 0:  #checking positive number
    if number % 2 == 0:    #check 
        print("This is even number")
    else:
        print("This is odd number")
else:
    if number == 0:
        print("This is Zero")
    else:
        print("This number is negative")
