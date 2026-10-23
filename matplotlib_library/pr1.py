import matplotlib.pyplot as plt
import numpy as np
#2 approch che matplotlib
#plot()#function

x=np.arange(1,11)
y=x**3
plt.plot(x,y)
plt.show()

plt.plot(x,y)
plt.title('X vs Y relationship',fontdict={'color':'Green','size':25,'weight':'bold','font':'cursive'},loc='center')
plt.xlabel('Array=X',fontdict={'color':'red','size':15,'weight':'bold','font':'cursive'},loc='center')
plt.ylabel('Array=X',fontdict={'color':'red','size':15,'weight':'bold','font':'cursive'},loc='center')
plt.show()

plt.plot(x,y,
         color='r',
         marker='o',
         markersize=10,
         markerfacecolor='yellow',
         markeredgecolor='green',
         markeredgewidth=2,
         ls='--',
         lw=1.8)
plt.show()

plt.plot(x,y,
         color='g',
         marker='s',  #
         markersize=10,
         markerfacecolor='yellow',
         markeredgecolor='blue',
         markeredgewidth=2,
         ls='--',
         lw=1.8,
         label='data found')
plt.show()

plt.title('plot-A',fontdict={'color':'r','size':22},loc='center')
plt.legend()
plt.show()


plt.plot(x,y)
plt.plot([100,200,300,400],[150,250,350,450])
plt.show()

#subplot
# plt.subplot(1,2,1)
# plt.subplot(1,2,2)
# plt.show()

#ada aave
plt.subplot(3,5,1)
plt.subplot(3,5,2)
plt.subplot(3,5,3)
plt.subplot(3,5,4)
plt.subplot(3,5,5)
plt.subplot(3,5,6)
plt.subplot(3,5,7)
plt.subplot(3,5,8)
plt.subplot(3,5,9)
plt.subplot(3,5,10)
plt.subplot(3,5,11)
plt.subplot(3,5,12)
plt.show()

#ubha aave
plt.subplot(2,1,1)
plt.subplot(2,1,2)
plt.show()

#
plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.plot(y,x)
plt.subplot(2,2,3)
plt.subplot(2,2,4)
plt.show()

#