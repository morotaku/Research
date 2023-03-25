import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from matplotlib.colors import LinearSegmentedColormap

#Topological charge
l=float(input())

#Certesian coodinate
N=1000
x=np.linspace(-10,10,N)
y=np.linspace(-10,10,N)

X,Y=np.meshgrid(x,y)

#Polar coodinate
r = np.sqrt(X**2+Y**2)
phi = np.arctan2(Y,X)

#Phase
E=np.exp(1j*np.pi*0)*np.exp(1j*l*phi)
E_an=np.angle(E)

#plot
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

im=plt.imshow(E_an,vmax=2,extent=(-1,1,-1,1),cmap='gray')
ax.set_axis_off() #軸off
plt.show()

#saving
#plt.savefig('path')