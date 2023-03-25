import matplotlib.pyplot as plt
from math import *
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

#plot interval
N=1000
x=np.linspace(10,40,N)

x1=-1+x*0
x2=1+x*0
d1=x+5

#parameter(mm)
L=200
d=np.linspace(10,40,N)
n=1.45
L1=5
L2=x
L3=L-5-x
n2=1
n1=1.45
f=25.4

#stable region

def AD(L1,L2,L3,n1,n2,f):
    A=(2*L2*L3*n1+f**2*n1-2*L2*f*n1-2*L3*f*n1+2*L1*L3*n2-2*L1*f*n2)/(f**2*n1)#=D
    F=A*2/2#(A+D)/2
    return F

def AD2(d,f,L,n):
    A=(-2*d**2*n+(2*n*L+10*n-10)*d+n*f**2+(-2*n*L+10*n-10)*f+10*L-10*L*n)/(f**2*n)
    return A

D=d1
A1=AD2(d,f,L,1.4526)
A2=AD2(d,f,L,1.4752)




#np.savetxt("C:/Users/maila/OneDrive/デスクトップ/保存先/D.txt",D)
#np.savetxt("C:/Users/maila/OneDrive/デスクトップ/保存先/A1.txt",A1)
#np.savetxt("C:/Users/maila/OneDrive/デスクトップ/保存先/A2.txt",A2)
#show figure
plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
plt.plot(d1,AD(L1,L2,L3,1.4526,n2,f))
plt.plot(d1,AD(L1,L2,L3,1.4752,n2,f))
plt.ylim(-1,1)
plt.xlim(20,33)
#plt.grid()#グリッド

#axis label
plt.xlabel('d',size=13,)
plt.ylabel('(A+D)/2',size=15)

plt.show()
#グラフ
#fig = plt.figure(figsize=(5,5))
#ax = fig.add_subplot(111)
#im=plt.imshow(F,extent=(-1,1,-1,1))
#ax.set_axis_off() #軸off

#画像保存
#plt.savefig("phase")