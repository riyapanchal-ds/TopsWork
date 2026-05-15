#convert country name into upper case
lst_country=['india','usa','australia']
for i in lst_country:
    print(i.upper())

print(lst_country)

#convert country name into upper case if country name is then 5 letters
lst_country=['india','usa','australia']
for i in lst_country:
    if len(i)>5:
     print(i.upper())

     print(lst_country[0])
     print(lst_country[1:])
     print(lst_country[0][2])     #using double(2) index 
     print(lst_country[0][2:])

#list thur index
lst_country=['india','usa','australia']
for i in range(len(lst_country)):
   print(lst_country[i])
