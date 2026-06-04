
data= [
    {'item':'item1','amount':400},
    {'item':'item2','amount':300},
    {'item':'item1','amount':750},
]

item1=data[0]['amount'] + data[2]['amount']
item2=data[1]['amount']

print("Counter({'item1':",item1,",'item2':",item2,"})")