import re
lst_email=['test@gmail.com','werjjf','test123@gmail.com']
pattern= r"^\w+@\w+\.\w+$"                        #^ starting mate  $ ending mate
for i in lst_email:
    ans=re.search(pattern,i)
    print(ans)