#append
lst_names=['kavya','hani','riya']
print(lst_names)
lst_names.append('mital')
print(lst_names)
lst_surname=['panchal','shah']
lst_names.append(lst_surname)
print(lst_names)

#expend method
lst_names=['riya','mital','jenish']
lst_names.extend("meena")
print(lst_names)

lst_names1=lst_names
lst_names1.extend(lst_surname)
print(lst_names)


#clear method
lst_names=['kavya','hani','riya']
print(lst_names)
lst_names.clear()
print(lst_names)

#insert method
lst_names=['kavya','hani','riya']
lst_names.insert(2,'mital')
print(lst_names)

print(lst_names.count('riya'))
print(lst_names.index('riya'))

#pop method                delete last element in list
print(lst_names.pop())
print(lst_names)
print(lst_names.pop())
print(lst_names)
print(lst_names.pop(1))
print(lst_names)

#copy method
lst_names=['kavya','hani','riya']
print(lst_names.copy())
print(lst_names)

#remove method
lst_names=['kavya','hani','riya']
print(lst_names.remove('hani'))
print(lst_names)

#reverse method
lst_names=['kavya','hani','riya']
print(lst_names.reverse())
print(lst_names)

#sort method
lst_names=['kavya','hani','riya']
print(lst_names.sort())
print(lst_names)



lst_numbers=[55,44,33,4,6,5,44,322,43]
print(lst_numbers.sort())
print(lst_numbers)
