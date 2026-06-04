scores={'a':50,'b':75,'c':30,'d':90,'e':60}
values=scores.values()
sorted_values=sorted(values,reverse=True)
result=sorted_values[:3]
print("top 3 values ",result)