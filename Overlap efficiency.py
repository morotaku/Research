##python3.8
from math import *
import numpy as np
from scipy.integrate import quad


#Parameters
Wp=112 #Pump beam size(μm) 590のときd=28.5で31の効率Max
#Wl=float(input('Wl=')) #Oscillation mode size
e=2.718
#Pump beam
Pp=0
Lp=0
#Oscillation mode
Pl=0 
#Ll=float(input('Ll=')) #共振モードのトポロジカルチャージ
inf=np.inf
# inf使いたいならnp.infというのがある。

#Definition of Laguerre polynominal
def Laguerre(p,l,x):#p<l
    Lag=0
    for k in range(0,p+1):
        Lag += (-1)**(k+abs(l))*((factorial(p+abs(l))**2*x**k)/(factorial(k)*factorial(k+abs(l))*factorial(p-k)))
    return Lag


#Definition of Laguerre Gaussian Mode
def LGMode(p,l,rad,W):
    C=(2*factorial(p)/(pi*factorial(p+abs(l))))**0.5
    LG=C/W*(2**0.5*rad/W)**abs(l)*Laguerre(p, l, 2*rad**2/W**2)*e**((-1)*rad**2/W**2)
    I=LG**2
    return I

def Phase(phi,l):
    return np.exp(1j*l*phi)

#豊田追記
#scipy.integrate.quad()を使うなら、積分軸は第一引数にする必要あり。
#計算するfuncを作っておく。
def funcA(rad, p1, l1, w1, p2, l2, w2):
    return LGMode(p1,l1,rad,w1)*LGMode(p2,l2,rad,w2)*rad

def funcB(rad, p, l, w):
    return LGMode(p,l,rad,w)**2*rad

def funcC(phi,l):
    return Phase(phi,l)*Phase(phi,l).conjugate()


def Eff(W,L,P):
    A= quad(funcA, 0, np.inf, (Pp, Lp, Wp, P, L, W))[0]*quad(funcC, 0, 2*np.pi, (L))[0]
    B= (quad(funcB, 0, np.inf, (Pp, Lp, Wp))[0]*quad(funcC, 0, 2*np.pi, (L))[0] * quad(funcB, 0, np.inf, (P,L,W))[0]*quad(funcC, 0, 2*np.pi, (L))[0])**0.5
    eff=A/B
    return eff

Pl=[0,0,0,0]
Ll=[1.0,5.0,10.0,15.0]#,20.0,22.0,24.0,26.0,28.0,30.0,31.0]
Wl=[28.3,49,66.3,80]#,91.6,95.9,100,103.9,107.7,111.3,113.1]#[5.64,5.55,5.37,5.18,4.99,4.78,4.57,3.99,3.31,2.44,1.41]
#Wl.sort()


for i in range(11):
    print('Wl=',Wl[i],'','Ll=',Ll[i],'','Pl=','','eff=',Eff(Wl[i],Ll[i],Pl[i]))
