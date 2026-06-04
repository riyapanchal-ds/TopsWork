#split method
stmt="this is Python world. python is easy learn and python is widely used"
print(stmt)
lst=stmt.split()       #conevrt statement into list
print(lst.count("Python"))


stmt="this is Python world. python is easy learn and python is widely used"
print(stmt)
lst=stmt.split("is")
print(lst)
print(lst.count("Python"))


#join method
lst_names=['riya','hani','kavya']
names="*".join(lst_names)
print(names)

#delete karva
lst_names=['riya','hani','kavya']
del lst_names[1]
print(lst_names)
del lst_names                 #puri list nej delete kari de che etle error aave che ke lst_names is not defined
#print(lst_names)



#convert into list 
name="mital"      
lst=list(name)
print(lst)