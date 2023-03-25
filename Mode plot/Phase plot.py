import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from matplotlib.colors import LinearSegmentedColormap
from math import * 

#Topological charge
l=float(input())

#Certesian coodinate
N=1000
x=np.linspace(-10,10,N)
y=np.linspace(-10,10,N)

X,Y=np.meshgrid(x,y)

def Laguerre(p,l,x):#p<l
    Lag=0
    for k in range(0,p+1):
        Lag += (-1)**(k+abs(l))*((factorial(p+abs(l))**2*x**k)/(factorial(k)*factorial(k+abs(l))*factorial(p-k)))
    return Lag

#Polar coodinate
r = np.sqrt(X**2+Y**2)
phi = np.arctan2(Y,X)

#Phase
E=np.exp(1j*np.pi*0)*np.exp(1j*l*phi)*Laguerre(1,l,r)
E_an=np.angle(E)

#plot
fig = plt.figure(figsize=(3,3))
ax = fig.add_subplot(111)

im=plt.imshow(E_an,vmax=2,extent=(-1,1,-1,1),cmap='gray')
ax.set_axis_off() #軸off


#saving
path='C:/Users/maila/OneDrive/デスクトップ/保存先/phase1.png'
plt.savefig(path)
plt.show()