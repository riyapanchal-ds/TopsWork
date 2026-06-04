dict1={ "riya@gmail.com" : ["riya",20,"C G Road",120] ,
       "mital@gmail.com":["mital",20,"nikol",160] ,
       "jenish@gmail.com":["jenish",22,"S G highway",230]
       
       }

#fetch value from key
print(dict1["jenish@gmail.com"])

#only print marks
sum=0
for i in dict1.values():
   # print(i[3])
   if i[3]>150:
      print(i)
      sum+=i[3]              #total of marks

print(sum)
     
    