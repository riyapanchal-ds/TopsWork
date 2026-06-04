# import datetime
# cur_today=datetime.date.today()
# print(cur_today)

# now=datetime.datetime.now()
# #print(now)
# print(now.strftime("%d-%m-%y"))

x=0
while x<10:
    x+=3
    if x==6:
        break
    print(x,end='')

x=100
y=200
z=300
if x == 100 or y==200:
    if z== 300:
        print("A")
    else:
        print("B")
else:
 print("C")