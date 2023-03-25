import sympy as sy
from scipy.special import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image
from math import *
import mpl_toolkits.axes_grid1
import numpy as np
from matplotlib.colors import LogNorm
from matplotlib.colors import LinearSegmentedColormap

#データ分割数
N=2000

#座標系定義
x=np.linspace(-20,20,N)
y=np.linspace(-20,20,N)


X,Y=np.meshgrid(x,y)

#極座標の導入
r = np.sqrt(X**2+Y**2)
phi = np.arctan(Y/X)


#Bessel パラメータと振幅
k_n=1
a=1
u = jn(a,k_n*r)*np.exp(1j*a*phi) #jn:scipy.specialの関数

#LG強度
I = np.real(u*u.conjugate())
#規格化定数
Imax = np.amax(I)
#強度規格化
I_n = I/Imax
#og_I =np.log(I_n)

#カラーマップ
rb = LinearSegmentedColormap.from_list('name', ['white', 'red'])


#グラフ出力
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
im=plt.imshow(I_n,extent=(-1,1,-1,1),cmap=rb,vmax=0.3)
ax.set_axis_off()
plt.show()
#norm=mpl.colors.Normalize(0,abs(I).max())
#p=ax.pcolormesh(X,Y,I,norm=norm,cmap=mpl.cm.rainbow)
#p=ax.pcolormesh(X,Y,I)

#カラーバー
#divider = mpl_toolkits.axes_grid1.make_axes_locatable(ax)
#cax = divider.append_axes('right', '5%', pad='3%')
#plt.colorbar(im, cax=cax,norm=LogNorm(vmin=1e1, vmax=1e3))

#画像保存
#plt.savefig("Bessel.png")