#access the element index
name=input("enter name")         #index always square bracket ma hoy che
print(name[0])                    #index always start from the 0
print(name[1])
print(name[2])


name=input("enter name")
for i in range(len(name)):
    print(i,name[i])