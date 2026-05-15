#print even number from list

lst=[11,12,23,44,67]
for i in lst:
    if i%2==0:
        print(i)

#print 5 digit number
lst1=[1,23,34567,78905,123]
for i in lst1:
    if len(str(i))==5:      #convert int into string
        print(i)