set1={1,2,3,4,5}
set2={1,2,33,44,55,66}
'''set3=set1.union(set2)
print(set3)

set3=set1.intersection(set2)
print(set3)

set3=set1.difference(set2)
print(set3)

set3=set2.difference(set1)
print(set3)

set1.add(44)
print(set1)'''

set3= set1 & set2   #intersection
print(set3)

set3= set1 | set2   #union
print(set3)

set3= set1 - set2   #differance
print(set3)

set3= set2 - set1  #differance
print(set3)