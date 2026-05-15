import re
name= "Tops Technogies"
ans=re.search(r"Tops",name)
if ans:
    print("string found")
else:
    print("string not found")