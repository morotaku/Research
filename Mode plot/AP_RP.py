#### Circular geometrical mode
from math import *
import numpy as np
from scipy.special import *
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
plt.xlim([-5, 5])
plt.ylim([-5, 5])

#Parameters
w=0.5 #ビームウェスト
lam=0.64 #波長
k=2*np.pi/lam #波数
zr=w**2*k/2 #レイリー長
z=float(input('position: ')) #z座標 
R=z+zr**2/z #曲率半径
W=w*(1+(z/zr)**2)**0.5 #ビーム径
#Z=z/zr

print("zr=",zr)


#x-y coordinate
N=200
L=5 #表示範囲
X=np.linspace(-L,L,N)
Y=np.linspace(-L,L,N)
x,y=np.meshgrid(X,Y)
#Polar coodinate
r=np.sqrt(x**2+y**2)
phi=np.arctan2(y,x)


#Definition of Laguerre polynominal
def Laguerre(p,l,x):#p<l
    Lag=0
    for k in range(0,p+1):
        Lag += (-1)**(k+abs(l))*((factorial(p+abs(l))**2*x**k)/(factorial(k)*factorial(k+abs(l))*factorial(p-k)))
    return Lag


#Definition of Laguerre Gaussian Mode
def LGMode(p,l,rad,phi,sup):
    def LG(p,l,rad,phi):
        C=(2*factorial(p)/(np.pi*factorial(p+abs(l))))**0.5
        Gouy=-1j*(-(l*phi)-((2*p+abs(l)+1)*np.arctan(z/zr))+k*(rad**2/(2*R))+k*z)
        LG=C/W*(2**0.5*rad/W)**abs(l)*Laguerre(p, l, 2*rad**2/W**2)*np.exp((-1)*rad**2/W**2)*np.exp(Gouy)
        return LG
    if sup=='sup':
        LG=LG(p,l,rad,phi)+LG(p,-l,rad,phi)
    else:
        LG=LG(p,l,rad,phi)
    I=np.real(LG*LG.conjugate())
    Imax=np.amax(I)
    I_n=I/Imax
    #return I_n
    return LG

#Definition of AP Mode
def Azimuth(p,l,rad,phi):
    Ex=(-np.sin(phi))*LGMode(p,l,rad,phi,'')
    Ey=np.cos(phi)*LGMode(p,l,rad,phi,'')
    return Ex,Ey

#FlowerAPmode
def FlowerAP(p,l,rad,phi):
    Ex=(-np.sin(phi))*LGMode(p,l,rad,phi,'sup')
    Ey=np.cos(phi)*LGMode(p,l,rad,phi,'sup')
    return Ex,Ey

#Definition of RP mode
def Radial(p,l,rad,phi):
    Ex=np.cos(phi)*LGMode(p,l,rad,phi,'')
    Ey=np.sin(phi)*LGMode(p,l,rad,phi,'')
    return Ex,Ey

def FlowerRP(p,l,rad,phi):
    Ex=np.cos(phi)*LGMode(p,l,rad,phi,'sup')
    Ey=np.sin(phi)*LGMode(p,l,rad,phi,'sup')
    return Ex,Ey

#polarazer
def Polarizer(X,Y,thita):
    if thita=='none':
        EX,EY=X,Y
    else:
        EX=(np.cos(thita))**2*X+np.cos(thita)*np.sin(thita)*Y
        EY=np.sin(thita)*np.cos(thita)*X+(np.sin(thita))**2*Y
    return EX,EY
angle=input('angle')
thita=int(angle)/180*pi
thita='none'

#Mode intensity
Ex,Ey=Radial(1,1,r,phi)
#jones calculation
ix=Ex
iy=Ey
Ix=np.real(ix*ix.conjugate())
Iy=np.real(iy*iy.conjugate())
I=Ix+Iy
I_n=I/np.amax(I)

#Polarization arrow
N2=20 #Number of arrow
L2=5 #Display range
U=np.linspace(-L2,L2,N2)
V=np.linspace(-L2,L2,N2)
u,v=np.meshgrid(U,V)
r2=np.sqrt(u**2+v**2)#Polar coodinate
phi2=np.arctan2(v,u)

#Arrow power
Ex_p,Ey_p=Radial(1,1,r2,phi2)
EX_p,EY_p=np.real(Ex_p)/np.amax(np.real(Ex_p)),np.real(Ey_p)/np.amax(np.real(Ey_p))
#EY_p=np.zeros((N2,N2))

colors=(EX_p**2+EY_p**2)
#np.sqrt((EX_p**2)+(EX_p**2))
cmax=np.amax(colors)




#rb=LinearSegmentedColormap.from_list('name',['black','#AAB9FF'],N=5000) #color map,N(色の段階)#DB631F(色)
rb=LinearSegmentedColormap.from_list('name',['black','red','red'],N=5000)
im = plt.quiver(u, v, EX_p/cmax*0.5, EY_p/cmax*0.5,colors,cmap=rb,angles='xy', scale_units='xy', scale=1.5) #Arrow polt
im2 = plt.imshow(I_n,vmax=1,vmin=0,cmap='gray',extent=(-5,5,-5,5)) #Intensity plot

ax.set_axis_off()
name=input('name ')
#saving="C:/Users/maila/OneDrive/デスクトップ/paper/simulation/"+'Azi01_'+str(name)+".png" #保存先と保存名指定
#plt.savefig(saving,dpi=600) #画像保存

#plt.grid()
plt.show()