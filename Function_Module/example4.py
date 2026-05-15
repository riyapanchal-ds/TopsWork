#create square function ,to return a square or given number
def square(number):
    return number*number
ans=square(8)
print(ans)

lst_sq=[]
lst_no=[1,2,33,55]
for i in lst_no:
   # print(square(i))
   lst_sq.append(square(i))
   print(lst_sq)