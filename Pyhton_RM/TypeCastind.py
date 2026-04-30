#casting in python
a = 1
print(type(a))

b= "1"
print(type(b))

c = int(b)
print(type(c))
print(a+c)

print(a+int(b))
#all str type can't be casted into numerical type
#all numerical type can be cast into str
mynum = 26
mynum2 = str(mynum)
print(type(mynum2))

f1 = 22.56
f2= int(f1)
print(f2)
print(type(f2))

int1 =26
print(type(float(int1)))
