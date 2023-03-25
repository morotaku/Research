import numpy as np
import matplotlib.pyplot as plt

n1=1.5
n2=1
a=np.linspace(0,np.pi/2,1000)
b=np.arcsin(n1*np.sin(a)/n2)
c=a*180/np.pi

rp=np.tan(a-b)/np.tan(a+b)
Rp=(abs(rp))**2
rs=np.sin(b-a)/np.sin(b+a)
Rs=(abs(rs))**2

plt.plot(c,Rp,color='black')
plt.plot(c,Rs,color='red')
plt.xlim(0,90)
plt.legend()
plt.show()

'''
np.savetxt("C:/Users/maila/OneDrive/デスクトップ/保存先/Rp.txt",Rp)
np.savetxt("C:/Users/maila/OneDrive/デスクトップ/保存先/Rs.txt",Rs)
np.savetxt("C:/Users/maila/OneDrive/デスクトップ/保存先/c.txt",c)
'''