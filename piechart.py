import matplotlib.pyplot as plt
import numpy as np
expenses=[4000,2500,3700,4700]
name=['riya','mital','jenish','neha']
plt.figure(figsize=(5,5),dpi=300)
plt.pie(expenses,autopct='%1.2f%%',labels=name,
        colors=['green','yellow','blue','m'],
        explode=(0.0,0.0,0.0,0.1),
        shadow=False,
        pctdistance=0.8,
        labeldistance=0.5)
plt.legend()
plt.show()