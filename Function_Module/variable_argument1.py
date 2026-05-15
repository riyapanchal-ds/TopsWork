#variable arguments'''
'''def studentdetails(*data):
    print(end="\n\n")
    for i in data:
     print(i,end="\t")

studentdetails("riya",22,"commerce")
studentdetails("mital",23,"science","ahemedabad")
studentdetails("jenish",20,"commerce","ahemedabad","jenish@gmail.com")



#ex2        same function name different argument
def addition(*args):
 print(sum(args))
   
addition(1,2,3)
addition(11,22)
addition(2,2,2,2)


def addition(*args):
 sum=0
 for i in args:
   sum+=1
   return sum  
addition((1,2,3))
addition((11,22))
addition((2,2,2,2))

#average
def average(*args):
    avg=sum(args)/len(args)
    return avg

print(addition(11,22,33),average(11,22,33))
print(addition(2,3,8),average(2,3,8))
print(addition(100,200),average(100,200))

'''
'''lab task:--'''#recreate average function as now while calling average function arguments may be string 
#eg:==average(1,2,'riya'3)output--------3
#1st function========employee details may contains id,name,salary,age email
#2nd function========filter/fetch those employee details who got more than 20000''''''
''''''

def average(*args):
  total=0
  count=0
  for i in args:
    if type(i)==int or type(i) == float:
       total+=i
       count+=1

  return total / count
print(average(1,2,3,'riya'))


def empdetails(*args):
    
  if args[2] > 20000:
     print(args)
empdetails(1,"riya",25000,25,"riya@gmail.com")
empdetails(2,"mital",18000,24,"mital@gmail.com")
empdetails(3,"jenish",30000,26,"jenish@gmail.com")