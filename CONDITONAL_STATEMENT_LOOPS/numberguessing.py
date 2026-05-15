'''import random
sys_num=random.randint(1,100)
while True:
    user_num=int(input("enter number"))
    if user_num==sys_num:
        print("you win")
        break
    else:
        print("you lost")'''


import random
sys_num=random.randint(1,100)
while True:
    user_num=int(input("enter number"))
    if user_num>sys_num:
        print("enter number is  greater than random number ")
    elif user_num<sys_num:
        print("enter number is lesser than random number")
    elif user_num==sys_num:
        print("you win")
        break
    else:
        print("you lost")