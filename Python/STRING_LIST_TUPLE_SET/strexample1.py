#list method
name=input("enter name")
ans=name.upper()
print(ans)
ans=name.lower()
print(ans)
print(name.title())      #space ke badd first capital
print(name.capitalize())   #only first capital
print(name.count("e"))  #number of e name me kitne e he vo check karega
print(name.count("private"))
print(name.find("t"))
#index
name = "Riya Panchal"
print(name.index("i"))   #index no use word ni position check karva thay che

#endswith
name = "my name is riya"
print(name.endswith("riya"))    #string word અથવા letters થી અંત થાય છે કે નહીં. it means my name is riya-->true and my-->false

#startswith()
name="my name is riya"
print(name.startswith("my"))       #string કોઈ ખાસ word અથવા letter થી શરૂ થાય છે કે નહીં.

#strip()
name="  riya  "                  #string ના શરૂઆત અને અંતના extra spaces (ખાલી જગ્યા) દૂર કરે છે.
print(name.strip())

#left strip()                  #ફક્ત ડાબી બાજુના spaces દૂર કરે છે.
name=" riya "
print(name.lstrip())

#right strip()                    #ફક્ત જમણી બાજુના spaces દૂર કરે છે.
name="    riya    "
print(name.rstrip())


name="###||riya||###"     #    (#) શરૂઆત અને અંતમાંથી દૂર કર્યું.,strip() middle (વચ્ચે) ના spaces દૂર કરતું નથી.
print(name.strip("#"))

