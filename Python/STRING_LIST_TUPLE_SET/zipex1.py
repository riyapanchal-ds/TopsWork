#zip()
name=["riya","mital","jenish"]
age=[22,25,19]
result=zip(name,age)
print(list(result))

#zip() using loops
name=["riya","mital","jenish"]
age=[22,25,19]
for n ,a in zip(name,age):
 print(n,a)


# 3 list combines
name=["riya","mital","jenish"]
age=[22,25,19]
course=["python","DS","DA"]
result=zip(name,age,course)
print(list(result))

#second way
name=["riya","mital","jenish"]
age=[22,25,19]
course=["python","DS","DA"]
data=list(zip(name,age,course))
print(data)




#zip function convert into dictionary
name=["riya","mital","jenish"]
age=[22,25,19]
data=dict(zip(name,age))
print(data)


student=['riya','mital','jenish']
marks=[78,89,70]
for s,m in zip(student,marks):
 print(s,"have",m,"marks")