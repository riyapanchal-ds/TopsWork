def studentdetails(**kwargs):
   # print(kwargs['city'])                 #keyword argument mate **KWARGS
    for k,v in kwargs.items():
     print(k,v)
studentdetails(id=11,name='riya',city='ahmedabad')
studentdetails(id=12,name='mital',city='paldi',age=23)
studentdetails(id=13,name='jenish',city='ahmedabad')