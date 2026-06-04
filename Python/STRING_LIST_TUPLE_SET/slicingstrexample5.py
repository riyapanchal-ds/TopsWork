#string slicing----part of string

'''
name=input("enter name")
print(name[0:7])

#print 5 to 9
name=input("enter name")
print(name[5:9])

#alternate letter 2 to 10 
name=input("enter name")
print(name[2:11:2])

name=input("enter name")
print(name[:7])

#alternate letter up to 7
name=input("enter name")
print(name[:7:2])

#print from letter 5
name=input("enter name")
print(name[5:])


name=input("enter name")
print(name[-2:])

name=input("enter name")
print(name[:-2])

#reverse without using function
name=input("enter name")
print(name[::-1])'''

#first and last letter swipe
name=input("enter name")
ans=name [-1] + name[1:len(name)-1]+name[0]
print(ans)